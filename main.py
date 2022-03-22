import discord
import nltk
import gensim
from gensim.models import Word2Vec as w2v
from gensim.test.utils import common_texts
from gensim.models import KeyedVectors

model = w2v(sentences=common_texts, vector_size=100, window=5, min_count=1, workers=4)

print(model.similarity('hello', 'goodbye'))