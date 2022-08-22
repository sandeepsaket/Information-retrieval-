#!/usr/bin/env python
# coding: utf-8

# In[187]:


file = open(r'hi_language_corpora_Ques3\data\hi\hi.txt',encoding="utf8",errors="replace")


# In[188]:


#dep_vowels = ["ा", "ि", "ी", "ु", "ू", "े", "ो", "ै", "ौ", "ृ", "ॄ", "ॉ", "ं", "्"]
v = [ 'ा',"ि", "ी", "ु", "ू", "े", "ो", "ै", "ौ", "ृ", "ॄ", "ॉ", "ं", "्",'़']
vv = ["अ","इ", "ई", "उ", "ऊ","ए","ओ", "ऐ", "औ", "ऋ", "ॠ","ऑ","अं","अ","अं"]
vowels = ["अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ॠ", "ए", "ऐ", "ओ", "औ", "अं", "अः","ऑ"]
d=dict(zip(v,vv))
punct=["।",";",",",":","!",'"',"?",":-","-","{","(","}",")","_","०","S","―","=","[","]","......",":-",".","॥","","|","“","”","'"]


# In[189]:


uni_cc={}           #unigram character count
bi_cc={}            #bigram character count
tri_cc={}           #trigram character count
quad_cc={}          #Quadgram character count
uni_bc={}           #unigram word count
bi_bc={}            #bigram word count
tri_bc={}           #trigram word count
sylbl_dict={}       #unigram syllables count
sylbl_bi={}         #bigram syllables count
sylbl_tri={}        #trigram syllables count
global_sylbl_list=[] #global syllables list

##############################################################################################################################
count=1000000
while count>0:
    lines = file.readline().replace("\n","")
    #print(lines.split())
    line_list=[]
    for item in lines.split():
        word_list=[]
        for x in item:
            if ord(x) in range(2304,2431) and x not in punct:
                if x in v:
                    x=d[x]
                word_list.append(x)
        #print(word_list)
        #for i in range(len(word_list)-1):
            #print(l)
        #mod_word_list=[]
        for i in range(len(word_list)-1):
            #mod_word_list.append(word_list[i])
            if word_list[i] not in vowels and word_list[i+1] not in vowels :
                word_list.insert(i+1,'अ')
        
            
                
            
        line_list.append(word_list)
        #print(line_list)
    res = list(filter(None, line_list))
    #character(lines)
    #print(res)
    count = count-1
    for lists in res:
        for x in lists:
            if x not in uni_cc.keys():
                uni_cc[x]= int(1)
            else:
                uni_cc[x] += 1
        for i in range(len(lists)-1):
            if (lists[i],lists[i+1]) not in bi_cc:
                bi_cc[(lists[i],lists[i+1])]=int(1)
            else:
                bi_cc[(lists[i],lists[i+1])] += 1
        
        if len(lists)>=3:
            for i in range(len(lists)-2):
                if (lists[i],lists[i+1],list[i+2]) not in tri_cc:
                    tri_cc[(lists[i],lists[i+1],lists[i+2])]=int(1)
                else:
                    tri_cc[(lists[i],lists[i+1],lists[i+2])] += 1
        if len(lists)>=4:
            for i in range(len(lists)-3):
                if (lists[i],lists[i+1],lists[i+2],list[i+3]) not in quad_cc:
                    quad_cc[(lists[i],lists[i+1],lists[i+2],lists[i+3])]=int(1)
                else:
                    quad_cc[(lists[i],lists[i+1],lists[i+2],lists[i+3])] += 1
                    
#############################################################################################################################
    
    #print(lines.split())
    word_list=[]
    for ele in lines.split():
        word=""
        for x in ele:
            if ord(x) in range(2304,2431) and x not in punct:
                word=word+x
        word_list.append(word)
    #print(word_list)
    res1 = list(filter(None, word_list))
    #print(res1)
    for items in res1:
        if items not in uni_bc.keys():
            uni_bc[items]=int(1)
        else:
            uni_bc[items]+=1
    
    for i in range(len(res1)-1):
        if (res1[i],res1[i+1]) not in bi_bc:
            bi_bc[(res1[i],res1[i+1])]=int(1)
        else:
            bi_bc[(res1[i],res1[i+1])]+=1
    
    for i in range(len(res1)-2):
        if (res1[i],res1[i+1],res1[i+2]) not in tri_bc:
            tri_bc[(res1[i],res1[i+1],res1[i+2])]=int(1)
        else:
            tri_bc[(res1[i],res1[i+1],res1[i+2])]+=1
            
############################################################################################################################

    for listing in res:
        sylbl_list=[]
        ##wording=""
        ##for i in range(len(listing)):
        if len(listing)>=2:
            i=0
            while i<(len(listing)):
                ##wording=""
                if listing[i] in vowels:
                    wording=""
                    wording=wording+listing[i]
                    sylbl_list.append(wording)
                    if wording not in sylbl_dict.keys():
                        sylbl_dict[wording]=int(1)
                    else:
                        sylbl_dict[wording]+=1
                    i=i+1
                else:
                    wording=""
                    wording=wording+listing[i]
                    #sylbl_list.append(wording)
                    if(i<len(listing)-1):
                        while(listing[i+1] in vowels):
                            i=i+1
                            wording=wording+listing[i]
                            if(i>=len(listing)-1):
                                break;
                        sylbl_list.append(wording)        
                        if wording not in sylbl_dict.keys():
                            sylbl_dict[wording]=int(1)
                        else:
                            sylbl_dict[wording]+=1
                        i=i+1
                    else:
                        sylbl_list.append(wording)
                        if wording not in sylbl_dict.keys():
                            sylbl_dict[wording]=int(1)
                        else:
                            sylbl_dict[wording]+=1
                        i=i+1
        global_sylbl_list.append(sylbl_list)
                        
                


# In[190]:


#print(global_sylbl_list)
#global syllable dictionary

for item in global_sylbl_list:
    for i in range(len(item)-1):
        if(len(item)>=2):
            if (item[i],item[i+1]) not  in sylbl_bi.keys():
                sylbl_bi[(item[i],item[i+1])]=int(1)
            else:
                sylbl_bi[(item[i],item[i+1])]+=1
    for i in range(len(item)-2):
        if(len(item)>=3):
            if (item[i],item[i+1],item[i+2]) not  in sylbl_bi.keys():
                sylbl_tri[(item[i],item[i+1],item[i+2])]=int(1)
            else:
                sylbl_tri[(item[i],item[i+1],item[i+2])]+=1
            
            
        


# # Question 3(a) Answer

# In[191]:


l=(sorted(uni_cc.keys(), key = lambda x:uni_cc[x], reverse = True)[:100])


# In[192]:


with open('top_100_charcter_unigram.txt', 'w',encoding='utf-8') as f:
    for item in l:
        f.write("%s\n" % item)


# In[193]:


l=(sorted(bi_cc.keys(), key = lambda x:bi_cc[x], reverse = True)[:100])


# In[194]:


with open('top_100_charcter_bigram.txt', 'w',encoding='utf-8') as f:
    for item in l :
        f.write("%s%s\n" % item)


# In[195]:


l=(sorted(tri_cc.keys(), key = lambda x:tri_cc[x], reverse = True)[:100])


# In[198]:


with open('top_100_charcter_trigram.txt', 'w',encoding='utf-8') as f:
    for item in l:
        f.write("%s%s%s\n"%item)


# In[199]:


l=(sorted(quad_cc.keys(), key = lambda x:quad_cc[x], reverse = True)[:100])


# In[201]:


with open('top_100_charcter_quadgram.txt', 'w',encoding='utf-8') as f:
    for item in l:
        f.write("%s%s%s%s\n"%item)


# # Question 3 (b) Answer

# In[202]:


l=(sorted(uni_bc.keys(), key = lambda x:uni_bc[x], reverse = True)[:100])


# In[203]:


with open('top_100_word_unigram.txt', 'w',encoding='utf-8') as f:
    for item in l:
        f.write("%s\n" % item)


# In[204]:


l=(sorted(bi_bc.keys(), key = lambda x:bi_bc[x], reverse = True)[:100])


# In[205]:


with open('top_100_word_bigram.txt', 'w',encoding='utf-8') as f:
    #print(type(l))
    for item in l:
        f.write("%s%s\n"%item)


# In[206]:


l=(sorted(tri_bc.keys(), key = lambda x:tri_bc[x], reverse = True)[:100])


# In[207]:


with open('top_100_word_trigram.txt', 'w',encoding='utf-8') as f:
    for item in l:
        f.write("%s%s%s\n"%item)


# # Question 3 (c) Answer

# In[208]:


l=(sorted(sylbl_dict.keys(), key = lambda x:sylbl_dict[x], reverse = True)[:100])


# In[209]:


with open('top_100_syllable_unigram.txt', 'w',encoding='utf-8') as f:
    for item in l:
        f.write("%s\n" % item)


# In[210]:


l=(sorted(sylbl_bi.keys(), key = lambda x:sylbl_bi[x], reverse = True)[:100])


# In[211]:


with open('top_100_syllable_bigram.txt', 'w',encoding='utf-8') as f:
    for item in l:
        f.write("%s%s\n"%item)


# In[212]:


l=(sorted(sylbl_tri.keys(), key = lambda x:sylbl_tri[x], reverse = True)[:100])


# In[213]:


with open('top_100_syllable_trigram.txt', 'w',encoding='utf-8') as f:
    for item in l:
        f.write("%s%s%s\n"%item)


# # Question 3(d)

# In[233]:


#!pip install matplotlib
from matplotlib import pyplot as plt


# In[243]:


lists=list(uni_cc.values())
lists.sort(reverse=True)
#print(lists)
num2list=list(range(1,len(lists)+1))
plt.xlabel('characters')
plt.ylabel('Frequency')
plt.bar(num2list,lists)
plt.savefig('character_frequency.png')
#plt.show()


# In[244]:


lists=list(uni_bc.values())
lists.sort(reverse=True)
#print(lists)
num2list=list(range(1,len(lists)+1))
plt.xlabel('words')
plt.ylabel('Frequency')
plt.bar(num2list,lists)
plt.savefig('word_frequency.png')

#plt.show()


# In[245]:


lists=list(sylbl_dict.values())
lists.sort(reverse=True)
#print(lists)
num2list=list(range(1,len(lists)+1))
plt.xlabel('syllable')
plt.ylabel('Frequency')
plt.bar(num2list,lists)
plt.savefig('syllable_frequency.png')
#plt.show()


# In[ ]:




