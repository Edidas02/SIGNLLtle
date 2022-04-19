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

def get_random_word():
    num = np.random.randint(0, len(data))
    return data[num]
def similarity_calc(guess,target):
    if (guess not in model.wv):
        return None
    a = model.wv[guess]
    b = model.wv[target]
    return (np.dot(a, b))/(np.linalg.norm(a)*np.linalg.norm(b))


