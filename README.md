# Similar Song Recommender

Hello, and this is the Simliar Song Recommender Discord bot! This Discord bot utilizes Google's AI Gemini 2.5 Pro to accurately recommend you songs that you could add to your playlist!

## How do you use it?

1. **First, create a Discord bot:**
    - Create a new Discord bot on the developer portal, linked here: [Discord Dev Portal](https://discord.com/developers/applications)
    - Copy your bot token under the "Bot" section in settings.
    - Invite the bot to your Discord server, making sure that you allow it to send messages and read message history.

2. **Configure your Spotify API Key:**
    - Create a Spotify developer account [here](https://developer.spotify.com/dashboard).
    - Obtain both your Spotify client ID and secret key and copy them down.

3. **Configure your Gemini API Key:**
    - Go to Google's AI Studio [here](https://aistudio.google.com/prompts/new_chat).
    - Obtain your Gemini API key and copy it down.

4. **Configure your Last.fm Key:**
    - Go to Last.fm's website and create an account [here](https://www.last.fm/join)
    - Verify your email
    - Go to Last.fm's api applications link [here](https://www.last.fm/api/accounts) and create a new API
    - Obtain both the API key and secret key and copy them down

5. **Create your configuration file:**
    - Create a file called "config.ini"
    - Paste your keys into the file in this format:
    
```plaintext
[Credentials]
DISCORD_BOT_TOKEN = discord-bot-token
SPOTIFY_CLIENT_ID = spotify-client-id
...
```

6. **Run your bot:**
    - Open song_recommender.py
    - Choose between using Gemini's recommendations or Last.fm's get_similar call (note that Gemini will take a little bit to send a message due to using Pro instead of Flash)
    - Run the script to start getting new songs to put into your playlists!

Please use this bot however you'd like and tailor it to your personal experience! If you have any questions, feedback, or suggestions, please feel free to reach out.