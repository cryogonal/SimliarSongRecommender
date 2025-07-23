from google import genai
import configparser

# gemini key from config file
config = configparser.ConfigParser()
config.read('config.ini')
gemini_key = config['Credentials']['GEMINI_API_KEY']

client = genai.Client(api_key = gemini_key)

async def get_recommendations(song_name, artist_name, genres):
    try:
        response = client.models.generate_content(
            model = "gemini-2.5-pro",
            contents = (
                f"Given {song_name} by {artist_name} with {genres} genres listed and figuring out the bpm, "
                "please give me 5 other songs that would fit this vibe and ONLY SAY those 5 songs. Please make sure you start each listed song with a dash."
                "Limit this message to under 30 words."
                )
        )

        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, didn't catch that. What was that again?"
