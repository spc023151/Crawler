# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:32:43 2020

@author: ASUS
"""

import bs4
import requests

def getForum(forum, page=0):
    
    url = "https://www.ptt.cc/bbs/" + forum + "/index.html"
    cookies={}
    
    ptthtml = requests.get(url)
    soup = bs4.BeautifulSoup(ptthtml.text, "lxml")

    #  forum輸入檢查
    if(soup.title.text=="404"):
        raise ValueError("PTT has no forum " + forum)
    # 進入18禁論壇檢查
    if(soup.find("div", "over18-notive")!=-1):
         ptthtml = requests.get(url, cookies={'over18': '1'})
         soup = bs4.BeautifulSoup(ptthtml.text, "lxml")
         cookies = {'over18': '1'}
    
    # 取得最新頁數的頁面
    newest_Page_href = soup.find("div", "btn-group btn-group-paging").find_all("a")[1]["href"]
    start = newest_Page_href.find("index") + 5
    end = newest_Page_href.find(".html")
    newest_Page_Number = int(soup.find("div", "btn-group btn-group-paging").find_all("a")[1]["href"][start:end]) + 1

    # page輸入檢查
    if (page>newest_Page_Number):
        raise ValueError("page " + str(page) + " not found")
    elif (page==0):
        page = newest_Page_Number
    
    # 應對page參數改變網址
    url = "https://www.ptt.cc/bbs/" + forum + "/index" +  str(page) + ".html"
    ptthtml = requests.get(url, cookies=cookies)
    
    result = bs4.BeautifulSoup(ptthtml.text, "lxml")
    
    return result

def getArticles(forum):
    
    ptt_url = "https://www.ptt.cc"
    
    
    return