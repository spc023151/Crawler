# 旅遊網站爬蟲

以下兩家旅遊網站為一樣的套版，一個爬蟲解析方式可以抓取大部分資料

* https://www.4p.com.tw/EW/GO/GroupList.asp
* https://www.newamazing.com.tw/EW/GO/GroupList.asp

-----------------------------------------------------------------------------------
* 爬蟲一開始以國外旅程作為樣板設計，時間關係沒辦法重新設計完整的方法以及正規化資料庫 (故國內會缺少可售空位)  
* 故此儲存架構中國外旅團才有的資料會有許多空值，及沒有Foreign key
* 爬取國內樣板時幾乎沒有缺少面試測驗文件中提到的資料，若有缺少的部分直接以try except跳過  
(groupDetail中沒有缺少值)  

* 觀察其網站發現可以直接post後端伺服器網址取得某些行程資料，但還是採用取得網頁內容比較方便解析  
(url = "https://www.newamazing.com.tw/EW/Services/SearchListData.asp")  
* 若網頁有詳細行程介紹圖片，爬蟲會將圖片抓下存於Images中(不包含詳細文字行程介紹中的圖片)
* 所有資料以csv檔儲存，國外旅團的出發日及可售空位以旅程編號作為檔名存於同一資料夾中

臨時資料結構如下圖:



![Alt text](https://github.com/spc023151/Crawler/blob/interview/TACrawler/Untitled%20Diagram.jpg)
