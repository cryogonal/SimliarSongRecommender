import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import configparser
from lastfm_search.lastfm_song_search import get_lastfm_genre

from AI_response.ai_reponses import get_responses

intents = discord.Intents.default()
intents.message_content = True

config = configparser.ConfigParser()
config.read('config.ini')
bot_token = config['Credentials']['DISCORD_BOT_TOKEN']

bot = commands.Bot(command_prefix = '$', intents=intents)

sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = config['Credentials']['SPOTIFY_CLIENT_ID'], client_secret = config['Credentials']['SPOTIFY_CLIENT_SECRET']))


@bot.event
async def on_read():
    print(f'Logged in as {bot.user.name}')

@bot.command(name = 'suggest')
async def test(ctx):
    await ctx.send('i am making a suggestion')

@bot.command(name = 'tellme')
async def tell_me_song(ctx, link):
    try:

        song_id = link.split('/track/')[1].split('?')[0]

        song_info = sp.track(song_id)

        song_name = song_info['name']
        artist_name = song_info['artists'][0]['name']
        
        results = sp.search(q = f'track:{song_name} artist:{artist_name}', type = 'track')
        if results['tracks']['items']:
            artist_id = results['tracks']['items'][0]['artists'][0]['id']
            artist_info = sp.artist(artist_id)
            genres = artist_info['genres']

        if not genres:
            genres = get_lastfm_genre(song_name, artist_name)

        await ctx.send("Let's see what this song's about...")

        gemini_reponse = await get_responses(song_name, artist_name, genres)
        await ctx.send(gemini_reponse)

    except Exception as e:
        await ctx.send(f'Error: {e}')
        
bot.run(bot_token)