import os
from dotenv import load_dotenv
load_dotenv()
import discord
import nltk
from nltk.corpus import brown
import gensim
from gensim.models import Word2Vec as w2v
from gensim.test.utils import common_texts
from gensim.models import KeyedVectors
import string

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
    await message.channel.send("Hello!")

nltk.download("brown")
 
# Preprocessing data to lowercase all words and remove single punctuation words
document = brown.sents()
data = []
for sent in document:
  new_sent = []
  for word in sent:
    new_word = word.lower()
    if new_word[0] not in string.punctuation:
      new_sent.append(new_word)
  if len(new_sent) > 0:
    data.append(new_sent)

model = w2v(sentences=data, vector_size=300, window=5, min_count=1, workers=4, epochs=50)


client.run(os.getenv('BOT_TOKEN'))

