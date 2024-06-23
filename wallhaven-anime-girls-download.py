#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import requests


# In[2]:


# api_key
# TODO: get your api key from wallhaven.cc
wallhaven_api_key = "" 


# In[3]:


# save path configuration
save_path = "/home/sinh/Pictures/Wallpapers/"


# In[4]:


# wallhaven url
search_url = "https://wallhaven.cc/api/v1/search"
search_params = {'q': '+anime girls+outdoors type:jpg', 'categories': '010', 'purity': '100', 
          'sorting': 'random', 'atleast': '2560x1600', 'ratios': '16x10',
          'apikey': wallhaven_api_key}
image_params = {'apikey':wallhaven_api_key}


# In[5]:


# get list of images
r = requests.get(search_url, params = search_params)
data = r.json()
image_list = data.get('data')


# In[6]:


# variables to store number of image saving
image_count = 0


# In[7]:


for item in image_list:
    image_id = item.get('id')
    image_path = item.get('path')
    image_resolution = item.get('resolution')
    img_save_path = save_path + 'wallhaven-' + image_id + '-' + image_resolution + '.jpg'
    if (not os.path.exists(img_save_path)):
        r = requests.get(image_path, params = image_params)
        img_data = r.content
        with open(img_save_path, 'wb') as handler:
            handler.write(img_data)
        image_count += 1


# In[ ]:




