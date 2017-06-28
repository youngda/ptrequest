
# coding: utf-8

# In[81]:

import requests
import re
import json
from bs4 import BeautifulSoup
from datetime import datetime
newsurl = 'http://news.sina.com.cn/c/nd/2017-06-20/doc-ifyhfnrf9362371.shtml'
CommentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
res = requests.get("http://news.sina.com.cn/china/")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'lxml')
for news in soup.select('.news-item'):
    if len(news.select('h2'))>0:
        h2 = news.select('h2')[0].text
        a = news.select('a')[0]['href']
        time = news.select('.time')[0].text
        print(time,h2,a)
def getCommnentCouts(newsurl):
    m = re.search('doc-i(.+).shtm',newsurl) 
    newsid=m.group(1)
    comments = requests.get(CommentURL.format(newsid))
    comments = comments.text.strip('var data=')
    jd = json.loads(comments)                                                                                                                                                                                                                                                        
    total = jd['result']['count']['total']
    return(total)
def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'lxml')
    result['title'] = soup.select('#artibodyTitle')[0].text
    result['newssource'] = soup.select('.time-source span a')[0].text
    time = soup.select('.time-source')[0].contents[0].strip()
    result['dt'] = datetime.strptime(time,'%Y年%m月%d日%H:%M')
    article = ''.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
    article = ''.join(article.split())
    result['article'] = article
    result['editor'] = soup.select('.article-editor')[0].text.lstrip('责任编辑：')
    result['comments'] = getCommnentCouts(newsurl)
    return result


# In[83]:

getNewsDetail(newsurl)


# In[97]:

import requests
import json
url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=5&callback=newsloadercallback&_=1497949898654'
def parseListLink(url):
    newsdetail = []
    res = requests.get(url)
    jd = json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))
    for ent in jd['result']['data']:
        newsdetail.append(getNewsDetail(ent['url']))
    return newsdetail
parseListLink(url)


# In[106]:

url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1497949898654'
news_total = []
for i in range(1,3):
    url.format(i)
    newsary = parseListLink(url)
    news_total.append(newsary)
    print(news_total)


# In[ ]:




# In[ ]:



