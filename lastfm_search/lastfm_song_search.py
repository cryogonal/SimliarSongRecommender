import pylast
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
lastfm_key = config['Credentials']['LASTFM_API_KEY']
lastfm_secret_key = config['Credentials']['LASTFM_SECRET_KEY']

network = pylast.LastFMNetwork(api_key = lastfm_key, api_secret = lastfm_secret_key)

def get_lastfm_genre(song_name, artist_name):
    try:
        track = network.get_track(artist_name, song_name)
        tags = track.get_top_tags()
        genres = [tag.item.name.lower() for tag in tags if float(tag.weight) > 0]
        return genres[:5]

    except Exception as e:
        print(f"last.fm Error: {e}")
        return []