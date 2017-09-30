import nltk
import re
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
from nltk.corpus import stopwords
import collections

def stemmer(doc_words):
    doc_words = [w.lower() for w in doc_words]
    stemmer_ = nltk.PorterStemmer()
    stemmed_words = [stemmer_.stem(k.lower()) for k in doc_words] 
    return stemmed_words

def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))
    filtered_words = list(filter(lambda x: x not in stop_words, text))
    return filtered_words

nltk.download("popular")
with open("..\\gather_data\\text.txt") as f:
    data = f.read()
doc_words = re.sub(r'[".,!?()@#$%^&*{}]', '', data)
doc_words
with open("..\\gather_data\\text_temp.txt", "w") as f:
    f.write(doc_words)    
with open("..\\gather_data\\text_temp.txt") as f:
    dat = f.read()
    
doc_words = nltk.word_tokenize(dat)
words = stemmer(doc_words)
clean_words = remove_stop_words(words)    
collection = collections.Counter(clean_words)
common = collection.most_common(min(len(clean_words), 10000))
positive_words = []
with open(".\\\opinion-lexicon-English\\positive-words.txt") as f:
    positive_words = f.read()
    positive_words = positive_words.split("\n")
    
negative_words = []
with open(".\\\opinion-lexicon-English\\negative-words.txt") as f:
    negative_words = f.read()
    negative_words = negative_words.split("\n")
    
neg_count = 0
pos_count = 0

for word in common:
    if str(word[0]) in positive_words:
        pos_count += word[1]
    if str(word[0]) in negative_words:
        neg_count += word[1]
        
colors = ['blue', 'red']
labels = ["Positive meaning", "Negative meaning"]
fig = plt.figure()
plt.pie([pos_count, neg_count],  labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
fig.savefig('..//semantic_output//piechart.png')