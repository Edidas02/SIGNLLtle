import nltk
from nltk.corpus import brown
import gensim
from gensim.models import Word2Vec as w2v
from gensim.test.utils import common_texts
from gensim.models import KeyedVectors
import string
import gensim.downloader
import numpy as np

corpus = gensim.downloader.load('text8')
model = w2v(corpus)
data = [word for sent in corpus for word in sent]


