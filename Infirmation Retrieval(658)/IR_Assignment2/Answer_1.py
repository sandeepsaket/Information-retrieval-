#!/usr/bin/env python
# coding: utf-8

# In[56]:


from gensim.models import KeyedVectors
import gensim
from gensim.models import Word2Vec


# In[57]:


get_ipython().system('pip install numpy')


# In[58]:


dimensions=[50,100]
models_name=['cbow', 'fasttext','sg']
# models_name=['cbow', 'fasttext', 'glove', 'sg']
threshold=[0.4,0.5,0.6,0.7,0.8]


# In[59]:


def load_model(dimensions,models_name):
    path = 'hi'+'/' +str(dimensions)+'/'+str(models_name)+'/hi-d'+str(dimensions)+'-m2-'+str(models_name)+'.model' 
    load_model = Word2Vec.load(path)
    return load_model
    # else:
    #     with open(path, 'rb') as f:
    #         mod_load = pickle.load(f)
    #     return load_model
#     #hi/50/cbow/hi-d50-m2-cbow.model


# In[60]:


import pandas as pd
x1=pd.read_csv("hi/hindi.txt",sep=",",header=None)
x1.columns=['a1','a2','a3']


# In[61]:


Word1=[]
for i in x1.a1:
    Word1.append(i)
Word2=[]
for i in x1.a2:
    Word2.append(i)
list3=[]
for i in x1.a3:
    list3.append(i)


# In[62]:


import math
def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)
#print( cosine_similarity(v1,v2))


# In[63]:


def final_models(Word1,Word2,model,threshold):
    ans = {"Word1":[],"Word2":[],"Similarity_score":[],"Ground_truth_similarity_score":list3,"label":[]}

    for w1, w2 in zip(Word1, Word2):
        v1=model.wv[w1]
        v2=model.wv[w2]
        ans["Word1"].append(w1)
        ans["Word2"].append(w2)
        ans["Similarity_score"].append(cosine_similarity(v1,v2))
        if(cosine_similarity(v1,v2)>threshold):
            ans["label"].append(1)
        else:
            ans["label"].append(0)
    
    return pd.DataFrame.from_dict(ans)


# In[64]:


def ground_labels(t,list3):
    ground_truth_labels=[]
    for i in list3:
        if (i>t*10):
            ground_truth_labels.append(1)
        else:
            ground_truth_labels.append(0)
    return ground_truth_labels


# In[65]:


def accuracy(label,ground_labels):
    count=0
    for a1, a2 in zip(label, ground_labels):
        if(a1==a2):
            count+=1
    accuracy=(count/(len(label)))*100
    return accuracy


# In[66]:


# final_model=final_models(Word1,Word2,model,0.4)


# In[67]:


# final_model=final_models(Word1,Word2,model,0.4)
# final_model1=final_models(Word1,Word2,model,0.5)
# final_model2=final_models(Word1,Word2,model,0.6)
# final_model3=final_models(Word1,Word2,model,0.7)
# final_model4=final_models(Word1,Word2,model,0.8)


# In[68]:


import numpy as np
for di in dimensions:
    i=0
    for md in models_name:
        i=i+1
        if i==1:
            name=f"{di}_Fasttext_similarity"
        elif i==2:
            name=f"{di}_Cbow_similarity"
        else:
            name=f"{di}_SG_similarity"
        model = {}
        print(md)
        model=load_model(di,md)
        
        for t in threshold:
            final_model=final_models(Word1,Word2,model,t)
            similarity_cosine_label=final_model["label"]
            name += f"_{t}"
            final_model.to_csv(name+".csv")
            
            
           
            ground_truth_labels=ground_labels(t,list3)
            ground_labels(t,list3)
            accuracy(similarity_cosine_label,ground_truth_labels)


# In[75]:


get_ipython().system('pip install pickle')


# In[76]:


import pickle


# In[77]:


for i in dimensions:
    path=('hi/50/glove/hi-d50-m2-glove.model')
with open(path, 'rb') as f:
    mod_load = pickle.load(f)


# In[1]:


# for i in dimensions:
#     path=('hi/'+str(i)+'/glove/hi-d'+str(i)+'-m2-glove.model')
# with open(path, 'rb') as f:
#     mod_load = pickle.load(f)
# for t in threshold:
#     final_model=final_models(Word1,Word2,model,t)
#     similarity_cosine_label=final_model["label"]
#     name += f"_{t}"
#     final_model.to_csv(name+".csv")
    
    
    
#     ground_truth_labels=ground_labels(t,list3)
#     ground_labels(t,list3)
#     accuracy(similarity_cosine_label,ground_truth_labels)


# In[ ]:




