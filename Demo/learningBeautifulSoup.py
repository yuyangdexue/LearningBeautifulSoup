# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup 
 
import os 
 
import sys

import requests  

num = 1 
url = 'http://xiaohua.zol.com.cn/new/'+str(num)+'.html'  

reload(sys)

sys.setdefaultencoding('utf-8') #https://www.cnblogs.com/sundahua/p/7248209.html

all_url = "http://xiaohua.zol.com.cn/new/5.html"  

def Gethref(url): 
    list_href = [] 
    headers = { 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"} 
    html = requests.get(url,headers = headers) 
    soup_first = BeautifulSoup(html.text,'lxml') 
    list_first = soup_first.find_all('li',class_='article-summary') 
    for i in list_first: 
        soup_second = BeautifulSoup(i.prettify(),'lxml') 
        list_second = soup_second.find_all('a',target = '_blank',class_='all-read') 
        for b in list_second: 
            href = b['href'] 
            list_href.append(href) 
    return list_href 
def GetTrueUrl(liebiao): 
    list = [] 
    for i in liebiao: 
        url = 'http://xiaohua.zol.com.cn'+str(i) 
        list.append(url) 
    return list 
def GetText(url): 
    for i in url: 
        html = requests.get(i) 
        soup = BeautifulSoup(html.text,'lxml') 
        content = soup.find('div',class_='article-text') 
        title = soup.find('h1',class_ = 'article-title') 
        SaveText(title.text,content.text) 
def SaveText(TextTitle,text): 
    f = open(str(TextTitle)+'txt','w') 
    f.write(text) 
    f.close() 
while num<=100: 
    url = 'http://xiaohua.zol.com.cn/new/' + str(num) + '.html' 
    GetText(GetTrueUrl(Gethref(url))) 
    num=num+1  
