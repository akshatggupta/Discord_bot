import discord
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define intents to access messages and content
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

# Load keywords from environment variables
ai_keywords = os.getenv("AI_KEYWORDS").split(",")
open_source_keywords = os.getenv("OPEN_SOURCE_KEYWORDS").split(",")
dsa_keywords = os.getenv("DSA_KEYWORDS").split(",")
web_dev_keywords = os.getenv("WEB_DEV_KEYWORDS").split(",")
app_dev_keywords = os.getenv("APP_DEV_KEYWORDS").split(",")

# Load thread IDs from environment variables
keyword_threads = {
    "AI": (ai_keywords, os.getenv("AI_THREAD_ID")),
    "Open Source": (open_source_keywords, os.getenv("OPEN_SOURCE_THREAD_ID")),
    "DSA": (dsa_keywords, os.getenv("DSA_THREAD_ID")),
    "Web Development": (web_dev_keywords, os.getenv("WEB_DEV_THREAD_ID")),
    "App Development": (app_dev_keywords, os.getenv("APP_DEV_THREAD_ID")),
}

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Ignore the bot's own messages
    if message.author == client.user:
        return

    # Standard bot response
    if client.user.mentioned_in(message):
        await message.channel.send(f'Hello! {message.author.mention}')
    if message.content.startswith('$hello'):
        await message.channel.send('Hello! Daddy!!')

    # Check if the bot is mentioned and handle accordingly
    if client.user in message.mentions:
        for category, (keywords_list, thread_id) in keyword_threads.items():
            if any(keyword.lower() in message.content.lower() for keyword in keywords_list):
                thread = client.get_channel(int(thread_id))
                if thread and not isinstance(message.channel, discord.Thread):
                    await message.reply(f"Hey {message.author.mention}, please check out the resources in the {thread.mention}.")
                return  # Exit after handling one category to prevent multiple responses



    

client.run(os.getenv('TOKEN'))

