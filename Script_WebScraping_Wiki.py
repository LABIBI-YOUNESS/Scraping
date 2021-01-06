#!/usr/bin/env python
# coding: utf-8

# In[37]:


import requests as rq
from bs4 import BeautifulSoup as bp


# In[38]:


req=rq.get('https://www.wikipedia.org/')
html=req.text


# In[39]:


bs=bp(html,"html.parser")


# In[108]:


list=bs.find_all('a',{'class':"link-box"})

for i in list:
    lang=i.find('strong')
    for j in lang:
        print("la langue:" + j)
    art_num=i.find('bdi',{'dir':"ltr"})
    for e in art_num:
        
        print("a le nombre d'article:" + e)

