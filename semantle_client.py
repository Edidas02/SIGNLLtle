import os
from dotenv import load_dotenv
import discord

load_dotenv()

game_sessions = {}

def fetch_session_id(message):
    return str(message.guild.id) + str(message.channel.id)




BOT_TOKEN = os.getenv('BOT_TOKEN')
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    # ignore bot's command
    if message.author == client.user:
        return
    print(message.content)
    print(fetch_session_id(message))
    await message.channel.send("Hello!")

client.run(os.getenv('BOT_TOKEN'))


