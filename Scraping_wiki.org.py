#!/usr/bin/env python
# coding: utf-8

# In[5]:


#importation
import requests as rq
from bs4 import BeautifulSoup as bp


# In[6]:


#GET request:
req=rq.get('https://www.wikipedia.org/') #All information about our query is now stored in a Response req object
req.encoding     # returns 'utf-8'
req.status_code  # returns 200
req.text #content of the server’s response
html=req.text


# In[7]:


#for extracting data from HTML files:
bs=bp(html,"html.parser") # bs=bp(the current markup,the parser to use)


# In[27]:


list=bs.find_all('a',{'class':"link-box"}) #bs.find_all(the name of the HTML tags,attribute)

for i in list:
    lang=i.find('strong')
    art_num=i.find('bdi',{'dir':"ltr"})
    for j in lang:
        for e in art_num:
            print("la langue:" + j + " " + "a le nombre d'article:" + e)


# In[ ]:




