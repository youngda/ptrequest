
# coding: utf-8

# In[474]:

import requests
import urllib
import os
import re
from bs4 import BeautifulSoup
for i in range(1,6):
    url = 'http://www.27270.com/ent/meinvtupian/2016/168618_{}.html'
    url = url.format(i)
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    picurl = soup.select('#picBody a img')[0]['src']
    urllib.request.urlretrieve(picurl,'/home/chris/girlpic/%sd.jpg' % i) 


# In[421]:

import requests
import urllib
import os
from bs4 import BeautifulSoup
url1 = 'http://www.27270.com/ent/meinvtupian/2017/203558_1.html'
res = requests.get(url1)
soup = BeautifulSoup(res.text,'lxml')
res.encoding = 'GB2312'
picurl = soup.select('#picBody a img')[0]['src']
def get_images(content):      
        urllib.request.urlretrieve(picurl,'/home/chris/girlpic/%s.jpg' % 2) 
get_images(picurl)
picurl = soup.select('.articleV4Page')
print(picurl)


# In[ ]:




# In[ ]:



