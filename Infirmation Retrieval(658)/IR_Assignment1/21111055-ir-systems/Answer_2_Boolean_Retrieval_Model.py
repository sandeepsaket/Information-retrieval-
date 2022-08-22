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

file=sys.argv[1]

query_file=pd.read_csv(file,sep='\t')
query_file.columns=["QueryId","Query"]


# In[ ]:


temp=open('posting_list',"rb")
posting_lists=pickle.load(temp)

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


def boolean_retreival(query):
    n=len(file_index)
    dictionary = []
    for words in set(query):
        array = [0]*n
        if word in posting_lists.keys():
            temp_d = posting_lists[word]
            for key in temp_d.keys():
                array[key] = 1
        dictionary.append(array)
    operators=[]
    for i in range(1,len(query)):
        operators.append('and')

    for op in operators:
        result=[b1&b2 for b1,b2 in zip(dictionary[0],dictionary[1])]
        dictionary.pop(0)
        dictionary.pop(0)
        dictionary.insert(1,result)
    ans=dictionary[0]
    final_result=[]
    for i,x in enumerate(ans):
        final_result.append((file_index[i][0],x))
    final_result.sort(key=lambda x:x[1],reverse=True)
    return final_result


# In[ ]:


result_dataframe = pd.DataFrame(columns = ['QueryID', 'Iteration', 'DocID', 'Relevance'])


# In[ ]:


for item in query_file.values:
    q_id = item[0]
    query_text=item[1]
    
    query_text=clean_query(query_text)

    result=boolean_retreival(query_text)
    for i in range(5):
        score=result[i][1]
        if score==1:
            rel=1
        else:
            rel=0
        result_dataframe.loc[len(result_dataframe.index)]=[q_id,1,result[i][0],rel]


# In[ ]:


result_dataframe.to_csv('Boolean.txt', sep = ',')


# In[ ]:




