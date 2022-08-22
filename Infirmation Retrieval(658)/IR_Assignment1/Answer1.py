#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import pickle
import  math
from nltk.corpus import stopwords
from nltk.stem import  PorterStemmer
from nltk.tokenize import  word_tokenize,sent_tokenize
import re
import os
import numpy as np
import pandas as pd
from numpy import linalg as LA
import sys
import glob
Stopwords = list(set(stopwords.words('english')))


# In[2]:


docs = []
for i in os.listdir('english-corpora'):
    docs.append(i)
docs.sort()


# In[3]:


file_index={}
all_words={}
all_unique_words=set()


# In[4]:


posting_list={}


# In[5]:


# function for uper to lower case 
def uper_to_lower_case(docs):
    return str(np.char.lower(docs))

# function for remove punctuation 
def delete_punctuation(docs):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
    for i in range(len(symbols)):
        docs = str(np.char.replace(docs, symbols[i], ' '))
        docs = str(np.char.replace(docs, "  ", " "))
    data = str(np.char.replace(docs, ',', ''))
    return data

# function for remove stop words
def remove_stop_words(filelist):
    return [t for t in filelist if t not in Stopwords and len(t)>1]

# function for stemminng
def stemSentence(docs):
    stem_sentence = []
    porter=PorterStemmer()
    for word in docs:
        stem_sentence.append(porter.stem(word))
    return stem_sentence

# function to remove non asciii character 
def remove_non_ascii_1(docs):
    return ''.join(i for i in docs if ord(i)<128)


# In[ ]:


idx=0
for file in docs:
    file_text=open('english-corpora/'+file,'r',encoding='utf-8').read()
    file_text.replace('\n',' ')
    file_text.replace('\t',' ')
    file_text=uper_to_lower_case(file_text)
    file_text=delete_punctuation(file_text)
    file_text=remove_non_ascii_1(file_text)
    tokens=word_tokenize(file_text)

    file_text=remove_stop_words(tokens)
    file_text=stemSentence(file_text)
    
    file_index[idx]=(file,len(file_text))
    all_words[idx]=file_text
    idx+=1
    all_unique_words.update(set(file_text))


# In[ ]:


for word in all_unique_words:
    posting_list[word]={}
    
for idx in all_words.keys():
    words=all_words[idx]
    for w in set(words):
        posting_list[w][idx]= words.count(w)


# In[ ]:


#making norm dict dictionary wich will be used to normalize document vectors. 
norm_dict={}
for idx in all_words.keys():
    filelist = []
    words=all_words[idx]
    N=len(file_index.keys())
    for word in set(words):
        tf=posting_list[word][idx]
        df=len(posting_list[word])
        idf=math.log((N+1)/df)
        tfidf=tf*idf
        filelist.append(tfidf)
    norm_dict[idx] = LA.norm(filelist)
    


# In[ ]:


with open("posting_list", 'wb') as f:
    pickle.dump(posting_list, f)
with open("norm_dict", 'wb') as f:
    pickle.dump(norm_dict, f)
with open("file_index", 'wb') as f:
    pickle.dump(file_index, f)


# In[ ]:




