import discord
import os
from dotenv import load_dotenv
from resources import get_resource, resources

# Load environment variables from .env file
load_dotenv()

# Define intents to access messages and content
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

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
    if message.content.startswith('$'):
        await message.channel.send('mention me using @Elixir_bot and ask for resources and i will help you out by providing the resources ❤') 

    # Works when someone mentions the bot
    if client.user in message.mentions:
        search_key = message.content.replace(f'<@{client.user.id}>', '').strip()  # Extract the keyword from the message, it may content big text or spaces
        thread_id = get_resource(search_key)  # Get the thread ID from the resources.py file
        
    

        if thread_id:
            thread = client.get_channel(int(thread_id))  # Fetch the channel using the ID
            # Check if the thread exists and is indeed a thread
            if thread and isinstance(thread, discord.Thread):
                await message.reply(f"Hey {message.author.mention}, please check out the resources in the {thread.mention}.")
            else:
                await message.reply(f"Hey {message.author.mention}, I couldn't find the thread related to your request.")
        

client.run(os.getenv('TOKEN'))
