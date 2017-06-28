
# coding: utf-8

# In[10]:

from urllib.request import urlopen
import urllib.error.HTTPError
from bs4 import BeautifulSoup
html = urlopen('http://zhihu.com')
bsObj = BeautifulSoup(html.read(),'lxml')
print(bsObj.h1)


# In[33]:

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except urllib.error.HTTPError as e:
    print(e.code)
except urllib.error.URLError as e:
    if hasattr(e,'reason'):
        print(e.reason)
else:
    bsObj = BeautifulSoup(html.read(),'lxml')
    print(bsObj.h1)

