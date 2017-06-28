
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import os
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
url = 'http://www.mzitu.com/all'
res = requests.get(url)
bsObj = BeautifulSoup(res.text,'lxml')
all_a = bsObj.find('div',class_ = 'all').find_all('a')
for a in all_a:
    title = a.text
    a_url = a['href']
    path = str(title).strip()
    os.makedirs(os.path.join("/home/chris/Picture/newgirl",path))
    os.chdir("/home/chris/Picture/newgirl/"+path)
    for i in range(1,65):
        page_url = a_url+'/'+str(i)
        res_page = requests.get(page_url)
        bsObj_pic = BeautifulSoup(res_page.text,'lxml')
        pic_url = bsObj_pic.find('div',class_ = 'main-image').find('img')['src']
        name = pic_url[-9:-4]
        img = requests.get(pic_url, headers=headers)
        f = open(name+'.jpg', 'ab')
        f.write(img.content) 
        f.close()

