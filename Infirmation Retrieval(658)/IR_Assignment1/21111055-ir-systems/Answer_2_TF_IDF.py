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


# In[11]:


docs = []
for i in os.listdir('english-corpora'):
    docs.append(i)
docs.sort()


# In[12]:


file_index={}
all_words={}
all_unique_words=set()


# In[13]:


posting_list={}


# In[2]:


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

temp=open('norm_dict',"rb")
norm_dict=pickle.load(temp)


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

query_file=pd.read_csv(file,sep='\t')
query_file.columns=["QueryId","Query"]


# In[ ]:


def cosine_similarity(doc_vectors, query_vector, norm_dict):
    cosine_similarity=[]
    for i in range(len(doc_vectors)):
        cosine_similarity.append(np.dot(doc_vectors[i], query_vector)/(norm_dict[i]*np.linalg.norm(query_vector)))
    return cosine_similarity


# In[ ]:


#calculating term frequency–inverse document frequency(tfidf), idf ,and term frequency(tf)
def tfidf(query, posting_list, file_index, norm_dict):
    Q_text = query
    doc_vectors = []
    for doc in file_index.keys():
        vector = []
        for word in set(Q_text):
            if word in posting_list.keys() and doc in posting_list[word].keys():
                tf = posting_list[word][doc]
                idf = math.log((len(file_index.keys())+1)/(len(posting_list[word].keys())+1))
                tfidf = tf*idf
                vector.append(tfidf)
            else:
                vector.append(0)
        doc_vectors.append(vector)
        
    query_vector = []
    for word in np.unique(Q_text):
        if word in posting_list.keys():
            tf = query.count(word)
            idf = math.log((len(file_index.keys())+1)/(len(posting_list[word].keys())+1))
            tfidf = tf*idf
            query_vector.append(tfidf)
        else:
            query_vector.append(0)
    cosines=cosine_similarity(doc_vectors, query_vector, norm_dict)
    result=[]
    for i,x in enumerate(cosines):
        result.append((file_index[i][0],x))
    result.sort(key=lambda x:x[1],reverse=True)
    return result


# In[ ]:


result_dataframe = pd.DataFrame(columns = ['QueryID', 'Iteration', 'DocID', 'Relevance'])


# In[ ]:


for item in query_file.values:
    q_id = item[0]
    query_text=item[1]
    
    query_text=clean_query(query_text)

    result=tfidf(query_text, posting_list, file_index, norm_dict)
    for i in range(5):
        score=result[i][1]
        if score==0.0:
            rel=0
        else:
            rel=1
        result_dataframe.loc[len(result_dataframe.index)]=[q_id,1,result[i][0],rel]


# In[10]:


result_dataframe.to_csv('TF_IDF.txt', sep = ',')


# In[ ]:




