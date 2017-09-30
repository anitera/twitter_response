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

with open("..\\gather_data\\text.txt") as f:
    data = f.read()
data = data.decode('ascii', 'ignore')
doc_words = re.sub(r'[".,!?()@#$%^&*{}]', '', data)
with open("..\\gather_data\\text_temp.txt", "w") as f:
    f.write(doc_words)    
with open("..\\gather_data\\text_temp.txt") as f:
    dat = f.read()
    
doc_words = nltk.word_tokenize(dat)
words = stemmer(doc_words)
clean_words = remove_stop_words(words)    
collection = collections.Counter(clean_words)
common = collection.most_common(min(len(clean_words), 10000))
most_common = common[ : 15]
indices = np.arange(len(most_common))
fig = plt.figure()
freq = [k[1] for k in most_common]
word = [str(k[0]) for k in most_common]
plt.bar(indices, freq, color='green')
plt.xticks(indices, word, rotation='vertical')
plt.tight_layout()
fig.savefig('..//semantic_output//common_words.jpg')

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
pos_words = []
neg_words = []

for word in common:
    if str(word[0]) in positive_words:
        pos_count += word[1]
        if len(pos_words) < 10:
            pos_words.append((str(word[0]), word[1]))
    if str(word[0]) in negative_words:
        neg_count += word[1]
        if len(neg_words) < 10:
            neg_words.append((str(word[0]), word[1]))
    
freq_pos = []
word_pos = []
for k in pos_words:
    freq_pos.append(k[1])
    word_pos.append(k[0])
indices_pos = np.arange(len(pos_words))
fig = plt.figure()
plt.bar(indices_pos, freq_pos, color='blue')
plt.xticks(indices_pos, word_pos, rotation='vertical')
plt.tight_layout()
fig.savefig('..//semantic_output//good_words.jpg')

freq_neg = []
word_neg = []

for k in neg_words:
    freq_neg.append(k[1])
    word_neg.append(k[0])
indices_neg = np.arange(len(neg_words))
fig = plt.figure()
plt.bar(indices_neg, freq_neg, color='r')
plt.xticks(indices_neg, word_neg, rotation='vertical')
plt.tight_layout()
fig.savefig('..//semantic_output//bad_words.jpg')

colors = ['blue', 'red']
labels = ["Positive meaning", "Negative meaning"]
fig = plt.figure()
plt.pie([pos_count, neg_count],  labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
fig.savefig('..//semantic_output//piechart.jpg')