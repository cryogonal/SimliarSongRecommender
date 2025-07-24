import pylast
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
lastfm_key = config['Credentials']['LASTFM_API_KEY']
lastfm_secret_key = config['Credentials']['LASTFM_SECRET_KEY']

network = pylast.LastFMNetwork(api_key = lastfm_key, api_secret = lastfm_secret_key)

def get_lastfm_recommendations(song_name, artist_name, limit = 5):
    try:
        track = network.get_track(artist_name, song_name)
        similar_tracks = track.get_similar(limit = limit) # uses simple api call to get similar tracks 
        recommendations = [f"{match.item.title} by {match.item.artist.name}" for match in similar_tracks]
        return recommendations

    except Exception as e:
        print(f"last.fm Error: {e}")
        return []