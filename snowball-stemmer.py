from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

text = open("./prideandprejudice", "r")
total = text.read().decode('utf8')
# split_text = total.split(' ')
# print(total)

# print(len(stopwords))
sw = stopwords.words('english')
#print(len(sw))
# print(len(total))
# print(total[:50])
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(total)
tokens = [token for token in tokens if token not in sw]
# print tokens
stemmer = SnowballStemmer("english")

# print(len(tokens))

tokens = [stemmer.stem(token) for token in tokens]

# print(len(tokens))

print(tokens[:50])

# After stemming from 7100 to 4181


