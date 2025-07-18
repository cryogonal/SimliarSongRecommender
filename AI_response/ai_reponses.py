from google import genai
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
gemini_key = config['Credentials']['GEMINI_API_KEY']

client = genai.Client(api_key = gemini_key)

async def get_responses(song_name, artist_name, genres):
    try:
        response = client.models.generate_content(
            model = "gemini-2.5-pro",
            contents = (f"Please give your thoughts on {song_name} by {artist_name}, as well as the {genres} and limit it to under 80 words. + \
                        Make it sound natural. Then, give a creative way of saying 'Here are 5 other songs that could vit this vibe'")
        )
        return response.text
    
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, didn't catch that. What was that again?"