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


# In[12]:


docs = []
for i in os.listdir('english-corpora'):
    docs.append(i)
docs.sort()


# In[13]:


file_index={}
all_words={}
all_unique_words=set()


# In[14]:


posting_list={}


# In[15]:


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


temp=open('posting_list',"rb")
posting_list=pickle.load(temp)

temp=open('file_index',"rb")
file_index=pickle.load(temp)


# In[ ]:


# function for cleaning query data 
def clean_query(query):
    Q_text=query
    Q_text=uper_to_lower_case(Q_text)
    Q_text=delete_punctuation(Q_text)
    Q_text=remove_non_ascii_1(Q_text)
    tokens=word_tokenize(Q_text)
    Q_text=remove_stop_words(tokens)
    Q_text=stemSentence(Q_text)
    return Q_text


# In[ ]:


file=sys.argv[1]
query_file=pd.read_csv(file,sep='\s\s\s\s',header=None)
query_file.columns=["QueryId","Query"]


# In[ ]:


total = 0
for item in file_index.keys():
    total += file_index[item][1]
L = total/len(file_index.keys())


# In[ ]:


re_dict = []


# In[ ]:


#basic functions to implement BM25
def norm(d_j):
    return len(all_words[d_j])/L

def TF(q_i, d_j):
    temp_list = all_words[d_j]
    # print("No of words are ", temp_list.count(q_i))
    return temp_list.count(q_i)

def DF(q_i):
    return len(posting_list[q_i])

def IDF(q_i):
    return np.log(1+(len(docs)-DF(q_i)+0.5)/(DF(q_i)+0.5))

def BM25(d_vec, q_vec,k=1.2,b=0.75):
    re_dict = []
    for d_j in d_vec.keys():
        result = 0
        for q_i in q_vec:
            if q_i in posting_list.keys() and d_j in posting_list[q_i].keys():
                idf = IDF(q_i)
                tf = TF(q_i, d_j)
                l = norm(d_j)
                result += idf * ((tf*(k+1))/(tf+k*(1-b+b*l)))
        re_dict.append((d_j, result))
    
    re_dict.sort(key = lambda x: x[1], reverse = True)
    return re_dict


# In[ ]:


result_dataframe = pd.DataFrame(columns = ['QueryID', 'Iteration', 'DocID', 'Relevance'])


# In[ ]:


for item in query_file.values:
    q_id = item[0]
    query_text=item[1]
    
    query_text=clean_query(query_text)
    k = 1.2
    b = 0.75
    result=BM25(file_index, query_text,k,b)
    for i in range(5):
        score=result[i][1]
        did=result[i][0]
        if score==0.0:
            rel=0
        else:
            rel=1
        result_dataframe.loc[len(result_dataframe.index)]=[q_id,1,file_index[did][0],rel]


# In[ ]:


result_dataframe.to_csv('BM25.txt', sep = ',')


# In[ ]:





# In[ ]:




