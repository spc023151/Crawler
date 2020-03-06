# Crawler

開發中Pytohn簡易爬蟲工具  
將爬蟲變得簡單  

  開發中網站
* https://shopee.tw/

  已開發網站
* https://www.ptt.cc/bbs

## Dependencies
安裝以下套件
* bs4
* requests  
安裝指令
```
pip install bs4
pip install requests
```

## pttCrawler
下載後和程式碼放在同一個資料夾將pttCrawler引入  
```python
from Crawler import pttCrawler
```
返回論壇指定頁數的html網頁  
pttCrawler.getForum(forum, pages)
* forum : 論壇名稱
* pages : 論壇頁數(不給則獲取最新一頁)
```python
html = pttCrawler.getForum("Gossiping")
```
解析html中的資料  
並將獲取的資料轉為dict型態回傳
```python
dict = pttCrawler.forum_to_data(html)
```
dict可以直接轉為Pandas型態  
```python
import pandas as pd

df = pd.DataFrame(dict)
df.head()
```
