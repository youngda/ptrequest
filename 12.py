
# coding: utf-8

# In[173]:

import requests
from bs4 import BeautifulSoup
res = requests.get("http://news.sina.com.cn/china/")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'lxml')
for news in soup.select('.news-item'):
    if len(news.select('h2'))>0:
        h2 = news.select('h2')[0].text
        a = news.select('a')[0]['href']
        time = news.select('.time')[0].text
        print(time,h2,a)


# In[316]:

import requests
from bs4 import BeautifulSoup
from datetime import datetime
#article =[]
res = requests.get('http://news.sina.com.cn/c/nd/2017-06-20/doc-ifyhfnrf9362371.shtml')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'lxml')
title = soup.select('#artibodyTitle')[0].text
time = soup.select('.time-source')[0].contents[0].strip()
dt = datetime.strptime(time,'%Y年%m月%d日%H:%M')
source = soup.select('.time-source span a')[0].text
#artibody = soup.select('#artibody p')[:-1]
#for p in artibody:
#    article.append(p.text.strip())
#article = ''.join(article)
article = '@@'.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
editor = soup.select('.article-editor')[0].text.lstrip('责任编辑：')
argue = soup.select('#commentCount1')
print(editor,title,dt,source,article)


# In[303]:

import requests
import json
comments = requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fyhfnrf9362371&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&jsvar=loader_1497929432017_59906153')
comments = comments.text.strip('var loader_1497929432017_59906153=')
jd = json.loads(comments)                                                                                                                                                                                                                                                        
total = jd['result']['count']['total']
print(total)


# In[166]:

newsurl = 'http://news.sina.com.cn/c/nd/2017-06-20/doc-ifyhfnrf9362371.shtml'
newsid = newsurl.split('/')[-1].rstrip('.shtml').lstrip('doc-i')
newsid


# In[175]:

import re
newsurl = 'http://news.sina.com.cn/c/nd/2017-06-20/doc-ifyhfnrf9362371.shtml'
m = re.search('doc-i(.+).shtm',newsurl) 
print(m.group(1))


# In[305]:

import requests
import json
CommentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
comments = requests.get(CommentURL.format(newsid))
comments.encoding = 'utf-8'
comments = BeautifulSoup(comments.text,'lxml')
comments = comments.text.strip('var loader_1497929432017_59906153=')
print(comments)
jd = json.loads(comments)                                                                                                                                                                                                                                                        
total = jd['result']['count']['total']
print(total)


# In[198]:

import re
import json
newsurl = 'http://news.sina.com.cn/c/nd/2017-06-20/doc-ifyhfnrf9362371.shtml'
CommentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
def getCommnentCouts(newsurl):
    m = re.search('doc-i(.+).shtm',newsurl) 
    newsid = m.group(1)
    comments = requests.get(CommentURL.format(newsid))
    comments = comments.text.strip('var loader_1497929432017_59906153=')
    jd = json.loads(comments)
    total = jd['result']['count']['total']
    return total
getCommnentCouts(newsurl)


# In[190]:

newsurl = 'http://news.sina.com.cn/c/nd/2017-06-20/doc-ifyhfnrf9362371.shtml'
getCommnentCouts(newsurl)


# In[ ]:



