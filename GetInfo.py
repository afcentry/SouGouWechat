#coding:utf-8

import requests
from bs4 import BeautifulSoup
import insertdata
import time
import random
from selenium import webdriver
import os
from lxml import etree

def getpagecontent(baseurl):

    # 引入chromedriver.exe
    chromedriver = "E:/googledriver/chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    # options = webdriver.ChromeOptions(    "User-Agent": "Mozilla/5.0(WindowsNT10.0;WOW64) AppleWebKit/537.36(KHTML,likeGecko)Chrome/64.0.3282.119Safari/537.36")
    browser = webdriver.Chrome(chromedriver)

    # 设置浏览器需要打开的url
    browser.get(baseurl)
    # 单击搜索按钮
    time.sleep(1)
    # browser.find_element_by_xpath("//input[@class = 'swz2'][1]").click()
    time.sleep(3)
    webcontent = BeautifulSoup(browser.page_source, "html.parser")

    browser.quit()
    return webcontent

def getaccountinfo():
    # baseurl = "http://weixin.sogou.com/weixinwap?ie=utf8&s_from=input&type=1&t=1522207444459&pg=webSearchList&_sug_=n&_sug_type_=&query=%E5%8C%BA%E5%9D%97%E9%93%BE"

    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q = 0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "zh-CN,zh;q = 0.9",
    "Cache - Control": "max-age = 0",
    "Connection": "keep-alive",
    "Cookie":"SUV = 0008178774195EC05A741734D4AF8166;CXID = 812FA14808E48825ED688AB2E8E62044;SUID = 748D3D3A4C238B0A5A795D14000A205D;ad = Zyllllllll2zoAAnlllllV$A3wclllllNxOWflllll9llllljylll5 @ @ @ @ @ @ @ @ @ @;ABTEST = 0 | 1522199705 | v1;IPLOC = CN4403;weixinIndexVisited = 1;JSESSIONID = aaaDH5LnhEsG6fyCHNOiw;PHPSESSID = f937v1bcbi04bf3lpglk0tics0;SUIR = 2FEFA8C6B2B7D9DF0FFD9995B2641C94;SNUID = 3EFFB8D4A1A5C9D12859C37CA1E46B5A;ppinf = 5 | 1522223354 | 1523432954 | dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyOkFDfGNydDoxMDoxNTIyMjIzMzU0fHJlZm5pY2s6MjpBQ3x1c2VyaWQ6NDQ6bzl0Mmx1QkY2Wm9iY2RSVVhtNHBYQXFjV0VMMEB3ZWl4aW4uc29odS5jb218;pprdig = KWm9t9fGgAsCJn9DoMJxTQBhGP0iA8y3IVs_8Ev5aMDFC2v3GmGDV0WtD9ot4s4YocLyN2GJ1iRoK0w_pPspDsIW3QO8RDqlRlKyPGtXt9egyNeh0lVfpyc2i - ujIiWVHbG1dAvwjRfjQ3OcYBch - pIxj3QviFvYvuLr3b_ZZng;sgid = 05 - 32173889 - AVq7SPrvmCDFEDYzpSfpNZc;sct = 1;ppmdig = 1522286733000000bb6bbe05024889be9032a2055f240612",
    "Host": "weixin.sogou.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0(WindowsNT10.0;WOW64) AppleWebKit/537.36(KHTML,likeGecko)Chrome/64.0.3282.119Safari/537.36"
    }

    # for pageid in range(11,20):
    keywordslist = ["区块链","比特币","以太坊","交易所"]
    for eve in keywordslist:
        for pageid in range(1, 11):
            # try:
            print("The Current PageID is ",pageid)
            # baseurl = "http://weixin.sogou.com/weixin?query=%E5%8C%BA%E5%9D%97%E9%93%BE&type=1&page=" + str(pageid) + "&ie=utf8"
            #关键词列表[区块链，比特币，以太坊，交易所，共识机制]
            baseurl = "http://weixin.sogou.com/weixin?query=" + eve + "&_sug_type_=&s_from=input&_sug_=n&type=1&page=" + str(pageid) + "&ie=utf8"
            print(baseurl)

            webcontent=getpagecontent(baseurl)
            allli = webcontent.find("ul",attrs = {"class":"news-list2"}).find_all("li")

            # allli = webcontent.find("div",attrs = {"class":"news-box"})

            for each in allli:
                # print(each)
                sleeptime = random.randint(5,10)
                AccountName = each.find("p",attrs = {"class":"tit"}).find("a").text.replace("<!--red_beg-->","")
                # print(AccountName)
                AccountID = each.find("p", attrs={"class": "info"}).find("label").text
                # print(AccountID)
                QrcodeUrl = ""
                dls = each.find_all("dl")
                InstructionInfo = dls[0].find("dd").text.replace("<!--red_beg-->","")
                try:
                    if "最近文章" in dls[1].find("dt").text:
                        RengZheng = ""
                    else:
                        RengZheng = dls[1].find("dd").text
                except Exception as e:
                    print(e)
                    RengZheng = ""
                # print(InstructionInfo)
                # print(RengZheng)
                AccountUrlList = each.find("div",attrs = {"class":"img-box"}).find("a").get("href")
                # print(AccountUrlList)
                AccountImg = each.find("div",attrs = {"class":"img-box"}).find("a").find("img").get("src")
                # print(AccountImg)

                insertdata.saveAccountdata(AccountName,AccountID,InstructionInfo,RengZheng,AccountUrlList,AccountImg,QrcodeUrl)
                time.sleep(sleeptime)
            # except Exception as e:
            #     print(e)
            time.sleep(15)

def getarticleinfo():
    articleurllist = insertdata.getaccountinfo()
    for each in articleurllist:
        AccountName = each[0]
        AccountID = each[1]
        ArticleUrlList = each[2]
        webcontent = getpagecontent(ArticleUrlList)
        break


if __name__ == "__main__":
    getaccountinfo()
    # getarticleinfo()