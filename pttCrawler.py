# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:32:43 2020

@author: ASUS
"""


import bs4
import requests

def getForum(forum, page=0):

    """
    Get ptt forum html code.
    
    Parameters
    ----------
    forum : string, default None
        Use given forum name to get the forum's page.
    page : int, , default 0
        Number in the URL to get the page of the given forum.
        If not passed, get the newest page of the given forum.
    ----------
    """
    
    url = "https://www.ptt.cc/bbs/" + forum + "/index.html"
    cookies={}
    
    ptthtml = requests.get(url)
    soup = bs4.BeautifulSoup(ptthtml.text, "lxml")

    #  check the forum name is correct or not
    if(soup.title.text=="404"):
        raise ValueError("PTT has no forum " + forum)
    # check if the forum needs over 18 years old 
    if(soup.find("div", "over18-notive")!=-1):
         ptthtml = requests.get(url, cookies={'over18': '1'})
         soup = bs4.BeautifulSoup(ptthtml.text, "lxml")
         cookies = {'over18': '1'}
    
    # get the newest forum page number
    newest_Page_href = soup.find("div", "btn-group btn-group-paging").find_all("a")[1]["href"]
    start = newest_Page_href.find("index") + 5
    end = newest_Page_href.find(".html")
    newest_Page_Number = int(soup.find("div", "btn-group btn-group-paging").find_all("a")[1]["href"][start:end]) + 1

    # ckeck page number is correct
    if (page>newest_Page_Number):
        raise ValueError("page " + str(page) + " not found")
    elif (page==0):
        page = newest_Page_Number
    
    # according to given page number to modify URL
    url = "https://www.ptt.cc/bbs/" + forum + "/index" +  str(page) + ".html"
    ptthtml = requests.get(url, cookies=cookies)
    
    result = bs4.BeautifulSoup(ptthtml.text, "lxml")
    
    return result

def forum_to_data(soup):
    data = {"nrec":[], "title":[], "href":[], "author":[], "date":[], "mark":[]}
    for tag in soup.find("div", "r-list-container action-bar-margin bbs-screen"):
        if isinstance(tag, bs4.element.Tag):
            if(tag["class"][0]=="r-ent"):
                try:
                    data["nrec"].append(tag.find("div", "nrec").string)
                except:
                    data["nrec"].append(None)
                    
                try:
                    data["title"].append(tag.find("a").string)
                except:
                    try:
                        data["title"].append(tag.find("div", "title").string.replace("\t", "").replace("\n", ""))
                    except:
                        data["title"].append(None)
                try:    
                    data["href"].append(tag.find("a")["href"])
                except:
                    data["href"].append(None)
                    
                try:
                    data["author"].append(tag.find("div", "author").string)
                except:
                    data["author"].append(None)
                    
                try:
                    data["date"].append(tag.find("div", "date").string.replace(" ", ""))
                except:
                    data["date"].append(None)
                    
                try:
                    data["mark"].append(tag.find("div", "mark").string)
                except:
                    data["mark"].append(None)
                    
            elif(tag["class"][0]=="r-list-sep"):
                break
        elif isinstance(tag, bs4.element.NavigableString):
            pass
        else:
            print("none of above")
    return data

def getArticle(url):
    # check url format
    if url.find("https://www.ptt.cc")==-1:
        url = "https://www.ptt.cc" + url
    
    ptthtml = requests.get(url)
    soup = bs4.BeautifulSoup(ptthtml.text, "lxml")
    
    #  check the article url is correct or not
    if(soup.title.text=="404"):
        raise ValueError("can not find article " + url)
        
    # check if the forum needs over 18 years old 
    if(soup.find("div", "over18-notive")!=-1):
        ptthtml = requests.get(url, cookies={'over18': '1'})
        soup = bs4.BeautifulSoup(ptthtml.text, "lxml")
    
    return soup

def article_to_data(article):

    data = {"author":[], "title":[], "forum":[], "post_time":[], "content":[]}

    main_content = article.find('div', id='main-content')
    content = main_content.find_all('span')

    try:
        main_content.find("span", "article-meta-tag").text
        data["author"].append(content[1].text)
        data["forum"].append(content[3].text)
        data["title"].append(content[5].text)
        data["post_time"].append(content[7].text)
    except:
        data["author"].append(None)
        data["forum"].append(None)
        data["title"].append(None)
        data["post_time"].append(None)
        
    data["content"].append(main_content.text)
    
    return data