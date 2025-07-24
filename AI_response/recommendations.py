from google import genai
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import configparser
import asyncio

# gemini key from config file
config = configparser.ConfigParser()
config.read('config.ini')
gemini_key = config['Credentials']['GEMINI_API_KEY']
sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = config['Credentials']['SPOTIFY_CLIENT_ID'], client_secret = config['Credentials']['SPOTIFY_CLIENT_SECRET']))

client = genai.Client(api_key = gemini_key)

async def get_recommendations(song_name, artist_name, genres):
    def _sync_recommendation_call():
        try:
            response = client.models.generate_content(
                model = "gemini-2.5-pro",
                contents = (
                    f"Given {song_name} by {artist_name} with {genres} genres listed and figuring out the bpm, "
                    "please give me 5 other songs that would fit this vibe and ONLY SAY those 5 songs."
                    "ONLY list the songs, each on a new line, in this format: '- Song Title by Artist Name'."
                    "No intro, no explanations, no extra words, and make sure each song and artist name are spelled correctly and match Spotify's catalog."
                    )
            )

            recommended_songs = response.text.split('\n')
            song_with_links = []

            for song in recommended_songs: # getting spotify links to every recommendations from gemini
                song = song.lstrip('- ')

                if ' by ' in song:
                    try:
                        song_title, song_artist = song.split(' by ', 1)

                        query = f"{song_title} {song_artist}"
                        sp_track = sp.search(q = query, type = 'track', limit = 1)

                        if sp_track['tracks']['items']:
                            spotify_id = sp_track['tracks']['items'][0]['id']

                            spotify_link = f"https://open.spotify.com/track/{spotify_id}"

                            song_with_links.append(f"- {song_title} by {song_artist} ({spotify_link})")
                        else:
                            song_with_links.append(f"- {song_title} by {song_artist} (No Spotify link found)") # if song isn't on spotify
                    except Exception as e:
                        print(f"Spotify Error: {e}")
                        song_with_links.append(f"- {song_title} by {song_artist} (Error parsing of searching)") # if problem occurred while searching
                else:
                    print(f"Bad format: {song}")
                    song_with_links.append(f" - {song} (Invalid format)") # if gemini somehow doesn't format it correctly

            return '\n'.join(song_with_links)
        except Exception as e:
            print(f"Gemini Error: {e}")
            return "Sorry, didn't catch that. What was that again?"
    
    return await asyncio.to_thread(_sync_recommendation_call)
