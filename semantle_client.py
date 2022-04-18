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
    if message.author == client.user or message.content[0] != '!':
        return
    command = message.content[1::].lower()
    print(command[0])
    if len(command) == 1 and command[0] == "p":
        await message.channel.send("Your game has started")       #initiate a game
    if len(command) >= 2 and command[0] == "g":
        await message.channel.send("Your guess is: " + message.content[3::].lower())            #quit game
    if len(command) == 1 and command[0] == "q":
        await message.channel.send("Game has ended!")              #make a guess


    print(message.content)
    print(fetch_session_id(message))
    await message.channel.send("Hello!")

client.run(os.getenv('BOT_TOKEN'))


