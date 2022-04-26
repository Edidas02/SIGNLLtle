import os
from dotenv import load_dotenv
import discord
from game import Game

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
    
    session_id = fetch_session_id(message)

    command = message.content[1::].lower()
    print(command[0])
    if len(command) == 1 and command[0] == "p":
        game_sessions[session_id] = Game(session_id)
        await message.channel.send("Your game has started")       #initiate a game
    if len(command) >= 2 and command[0] == "g":
        guess = message.content[3::].lower()
        await message.channel.send("Your guess is: " + guess)            #quit game
        if session_id in game_sessions.keys():
            similarity = game_sessions[session_id].make_guess(guess)
            await message.channel.send("The similarity is: " + str(similarity))
        else:
            await message.channel.send("Start a game before guessing")
    if len(command) == 1 and command[0] == "q":
        game_sessions.pop(session_id)
        await message.channel.send("Game has ended!")              #make a guess


    print(message.content)
    print(session_id)
    await message.channel.send("Hello!")

client.run(BOT_TOKEN)


