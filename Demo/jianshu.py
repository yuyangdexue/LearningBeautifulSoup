# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup 
 
import os 
 
import sys

import requests  

# num = 1 
# url = 'http://xiaohua.zol.com.cn/new/'+str(num)+'.html'  

reload(sys)

sys.setdefaultencoding('utf-8') #https://www.cnblogs.com/sundahua/p/7248209.html

all_url = "https://www.jianshu.com/"  

def Gethref(url): 
    list_href = [] 
    headers = { 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"} 
    html = requests.get(url,headers = headers) 
    soup_first = BeautifulSoup(html.text,'lxml') 
    list_first = soup_first.find_all('li',class_='have-img') 
    for i in list_first: 
        soup_second = BeautifulSoup(i.prettify(),'lxml') 
        list_second = soup_second.find_all('a',target = '_blank',class_='wrap-img') 
        for b in list_second: 
            href = b['href'] 
            list_href.append(href) 
            # print  href
    return list_href 
def GetTrueUrl(liebiao): 
    list = [] 
    for i in liebiao: 
        url = 'https://www.jianshu.com/'+str(i) 
        list.append(url) 
        # print  url
    return list 
GetTrueUrl(Gethref(all_url))
def GetText(url): 
    for i in url: 
        headers = { 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"} 
        html = requests.get(i,headers = headers) 
        soup = BeautifulSoup(html.text,'lxml') 
        article = soup.find('div',class_='article') 
        title = article.find('h1',class_ = 'title') 
        p =   article.find('div',class_ = 'show-content-free')
        SaveText(title.text,p.text) 
def SaveText(TextTitle,text): 
    f = open(str(TextTitle)+'.txt','w') 
    f.write(text) 
    f.close() 
# while num<=100: 
#     url = 'http://xiaohua.zol.com.cn/new/' + str(num) + '.html' 
#     GetText(GetTrueUrl(Gethref(url))) 
#     num=num+1  
GetText(GetTrueUrl(Gethref(all_url)))