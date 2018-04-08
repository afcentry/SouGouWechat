#coding:utf-8

import time
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
try:
    import insertdata
except:
    print("导入数据存储模块错误.")


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection": "keep-alive",
    "Cookie": "ABTEST=0|1522401112|v1; IPLOC=CN4403; SUID=485E19744842910A000000005ABDFF58; SUID=485E19745018910A000000005ABDFF59; weixinIndexVisited=1; SUV=005E51ED74195E485ABDFF5994F7C611; sct=1; SNUID=E2F7B3DEAAAFC1340B462D1EAA92BC1E; JSESSIONID=aaaRkvsPzYh_UfPSFVOiw; ppinf=5|1522401185|1523610785|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTozOkFUU3xjcnQ6MTA6MTUyMjQwMTE4NXxyZWZuaWNrOjM6QVRTfHVzZXJpZDo0NDpvOXQybHVDQmFTeTZVdDM2a3hqVmlSUlhDMjMwQHdlaXhpbi5zb2h1LmNvbXw; pprdig=p6IaAxiXz6J9_VoN1BePPGfNJTWyNfX_8LIwis90kgc-LenSFq-kRPWofirBMn5pSm4_HUPBDeQxVSrSwCIyYLPoeu5jV3pKDdPkcVdoOfh4XA88dxt1SxeBx-YD03lGzPoxjpKt5yFjDaEzsvgRKabe6n2qPqEm9YGYOitEo3o; sgid=19-34285717-AVq9ic6GiaGiatPld1EwpMkPNE; ppmdig=1522401185000000d659345a9352ed29df8b142c483d1240",
    "Host": "weixin.sogou.com",
    "Referer": "http://weixin.sogou.com/weixin?type=2&query=%E5%8C%BA%E5%9D%97%E9%93%BE&ie=utf8&s_from=input&_sug_=y&_sug_type_=-1&w=01015002&oq=qukuailia&ri=0&sourceid=sugg&stj=0%3B4%3B0%3B0&stj2=0&stj0=0&stj1=4&hp=40&hp1=&sut=3104&sst0=1522401116196&lkt=9%2C1522401112952%2C1522401114162",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0"
}


headers1 = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Cookie":"SUV=0008178774195EC05A741734D4AF8166; CXID=812FA14808E48825ED688AB2E8E62044; SUID=748D3D3A4C238B0A5A795D14000A205D; ad=Zyllllllll2zoAAnlllllV$A3wclllllNxOWflllll9llllljylll5@@@@@@@@@@; ABTEST=0|1522199705|v1; IPLOC=CN4403; weixinIndexVisited=1; UM_distinctid=16270f4b26847a-04e5f71d0d0587-3b604c04-1fa400-16270f4b26950e; CNZZDATA1266840871=926510625-1522312273-null%7C1522312273; SNUID=1BB60703393F52EE42268CC93A06E77A; JSESSIONID=aaajsyMrbSMW3hUr5JOiw; sct=12; ppinf=5|1522831285|1524040885|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyOkFDfGNydDoxMDoxNTIyODMxMjg1fHJlZm5pY2s6MjpBQ3x1c2VyaWQ6NDQ6bzl0Mmx1QkY2Wm9iY2RSVVhtNHBYQXFjV0VMMEB3ZWl4aW4uc29odS5jb218; pprdig=IxAZYSPAcQsqe2DwL9ffIIpmhGmDClWEYs3C3OtOSbcpOrkRvdf-qdpCKYLjrU0BN7cDtvMFerw9PxKHmkopiRM5UCJT2fEXTfaXWAIs76s4iLssxP-2jfKASbPOMmMeNBx6H3KRAB135Df2MmYsWOtVtMGKtXHn1TOnroO3saY; sgid=05-32173889-AVrEj7XjDeto4HSHGayB5pQ; ppmdig=152283128600000019a1e6ecdb86e36e03060cae6723012e",
    "Host":"weixin.sogou.com",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}


cookie_1 = {
    "ABTEST":"0|1522401112|v1",
    "IPLOC":"CN4403",
    "JSESSIONID":"aaaRkvsPzYh_UfPSFVOiw",
    "ppinf":"5|1522401185|1523610785|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTozOkFUU3xjcnQ6MTA6MTUyMjQwMTE4NXxyZWZuaWNrOjM6QVRTfHVzZXJpZDo0NDpvOXQybHVDQmFTeTZVdDM2a3hqVmlSUlhDMjMwQHdlaXhpbi5zb2h1LmNvbXw",
    "ppmdig":"1522401185000000d659345a9352ed29df8b142c483d1240",
    "pprdig":"p6IaAxiXz6J9_VoN1BePPGfNJTWyNfX_8LIwis90kgc-LenSFq-kRPWofirBMn5pSm4_HUPBDeQxVSrSwCIyYLPoeu5jV3pKDdPkcVdoOfh4XA88dxt1SxeBx-YD03lGzPoxjpKt5yFjDaEzsvgRKabe6n2qPqEm9YGYOitEo3o",
    "sct":"1",
    "sgid":"19-34285717-AVq9ic6GiaGiatPld1EwpMkPNE",
    "SNUID":"E2F7B3DEAAAFC1340B462D1EAA92BC1E",
    "SUID":"485E19745018910A000000005ABDFF59",
    "SUV":"005E51ED74195E485ABDFF5994F7C611",
    "weixinIndexVisited":"1"
}
#设置浏览器需要打开的url
url = "http://weixin.sogou.com/weixin?query=%E5%8C%BA%E5%9D%97%E9%93%BE&type=2&page=50&ie=utf8" #获取文章
url = "http://weixin.sogou.com/weixin?query=%E5%8C%BA%E5%9D%97%E9%93%BE&_sug_type_=&s_from=input&_sug_=y&type=1&page=12&ie=utf8" #获取公众号

def getwebcontent(url):
    """
    :param url: 请求页面Url
    :return:   请求页面详细内容[经过Beautifulsoup解析]
    """
    response = requests.get(url,headers = headers)
    webcontent = BeautifulSoup(response.text, "html.parser")
    return webcontent

def getaccountinfo_from_article(accountname,accountid):
    """
    :param accountname:公众号名称
    :param accountid: 公众号对应微信号
    :return:
    """
    url = "http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E4%BA%AC%E6%B2%AA%E5%8C%BA%E5%9D%97%E9%93%BE&ie=utf8&_sug_=n&_sug_type_=&w=01019900&sut=1762&sst0=1522814146687&lkt=0%2C0%2C0"


def account_web_analysis(url):
    """
    搜索制定公众号或微信号平台的相关信息
    :param url: 公众号搜索显示结果页面
    :return:
    """
    webcontent = getwebcontent(url)
    each = webcontent.find("ul", attrs={"class": "news-list2"}).find_all("li")[0]
    # allli = webcontent.find("div",attrs = {"class":"news-box"})
    # for each in allli:
        # print(each)
    AccountName = each.find("p", attrs={"class": "tit"}).find("a").text.replace("<!--red_beg-->", "")
    # print(AccountName)
    AccountID = each.find("p", attrs={"class": "info"}).find("label").text
    # print(AccountID)
    dls = each.find_all("dl")
    InstructionInfo = dls[0].find("dd").text.replace("<!--red_beg-->", "")
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
    AccountUrlList = each.find("div", attrs={"class": "img-box"}).find("a").get("href")
    # print(AccountUrlList)
    AccountImg = each.find("div", attrs={"class": "img-box"}).find("a").find("img").get("src")
    # print(AccountImg)

    # 执行数据库插入[存储公众号基本信息]
    #return AccountName, AccountID, InstructionInfo, RengZheng, AccountUrlList, AccountImg

    #执行完查询结果直接对其进行入库操作
    insertdata.saveAccountdata(AccountName, AccountID, InstructionInfo, RengZheng, AccountUrlList, AccountImg)

    print(AccountUrlList)
    getarticle_brief_info(AccountUrlList)


def getaccountinfo():
    """
    通过关键字搜索微信公众号
    :param url: 公众号搜索结果页面Url
    :return:
    """
    keywordslist = []
    #阅读txt文件生成关键字列表
    with open("./KeyWords.txt","r",encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace("\n","")
            keywordslist.append(line)

    for eve in keywordslist:
        for pageid in range(1, 21):
            # try:
            sleeptime = random.randint(15, 30)
            print("The Current PageID is:",pageid,"--The KeyWords Is:",eve)
            url = "http://weixin.sogou.com/weixin?query=" + eve + "&_sug_type_=&s_from=input&_sug_=y&type=1&page=" + str(pageid) + "&ie=utf8"  # 获取公众号
            print(url)
            webcontent = getwebcontent(url)
            allli = webcontent.find("ul",attrs = {"class":"news-list2"}).find_all("li")

            # allli = webcontent.find("div",attrs = {"class":"news-box"})
            for each in allli:
                # print(each)
                AccountName = each.find("p",attrs = {"class":"tit"}).find("a").text.replace("<!--red_beg-->","")
                # print(AccountName)
                AccountID = each.find("p", attrs={"class": "info"}).find("label").text
                # print(AccountID)
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

                #执行数据库插入[存储公众号基本信息]
                insertdata.saveAccountdata(AccountName, AccountID, InstructionInfo, RengZheng, AccountUrlList, AccountImg)
            print("sleeping...",sleeptime)
            time.sleep(sleeptime)
        time.sleep(5)

#获取文章大致信息
def getarticle_brief_info(url):
    """
    :param url: 每个公众号对应的文章列表页面Url
    :return:
    """
    webcontent = getwebcontent(url)
    allli = webcontent.find("ul", attrs={"class": "news-list"}).find_all("li")
    for each in allli:
        # print(each)

        sleeptime = random.randint(15, 30)
        #文章标题对应图片url链接
        Articlepic = each.find("div",attrs = {"class":"img-box"}).find("a").find("img").get("src")
        #文章标题
        Articletitle = each.find("div",attrs = {"class":"txt-box"}).find("h3").find("a").text
        #文章url链接
        Articletitleurl = each.find("div",attrs = {"class":"txt-box"}).find("h3").find("a").get("href")
        #文章内容简要
        Articlecontentins = each.find("p",attrs = {"class":"txt-info"}).text
        #获取文章详细内容信息
        article_detail_info_dict = getarticle_detail_info(Articletitleurl)
        # print(Articlepic)
        # print(Articletitle)
        # print(Articletitleurl)
        # print(Articlecontentins)
        PostDate = article_detail_info_dict["postdate"]
        Author = article_detail_info_dict["Author"]
        FromAccountName = article_detail_info_dict["AccountName"]
        FromAccountID = article_detail_info_dict["AccountID"]
        PageSource = article_detail_info_dict["PageSource"]

        #保存文章简要信息
        insertdata.saveArticleBriefData(Articletitle,PostDate,Author,FromAccountName,FromAccountID,Articlepic,Articletitleurl,Articlecontentins)

        #保存文章封面图片信息
        insertdata.saveArticlePicData(FromAccountName,FromAccountID,Articletitle,Articlepic)

        #保存文章源码到数据库
        insertdata.saveArticlePageSource(FromAccountName,FromAccountID,Articletitle,PageSource)
        # break
        time.sleep(sleeptime)

#获取文章详细内容
def getarticle_detail_info(url):
    """
    :param url: 文章详情页面Url
    :return:
    """

    article_detail_info_dict = {}
    # print("ArticleUrl:",url)
    try:
        driver = webdriver.Chrome(executable_path=r'D:\fas\chromedriver.exe')
    except:
        driver = webdriver.Chrome(executable_path=r'E:/googledriver/chromedriver.exe')
    driver.get(url)
    data = driver.page_source
    driver.quit()
    PageSource = data.replace("data-src=","src=")
    # print("dede:",type(PageSource))
    html = BeautifulSoup(data, "html.parser")
    #获取文章发表时间
    postdate = html.find("em",attrs={"id":"post-date"}).text
    # 获取文章发表时间作者
    try:
        Author = html.find_all("em", attrs={"class": "rich_media_meta rich_media_meta_text"})[1].text
    except:
        Author = ""
    #获取公众号名称
    AccountName = html.find("a",attrs={"id":"post-user"}).text
    #获取公众号二维码
    AccountQrcodeurl = html.find("img",attrs={"id":"js_pc_qr_code_img"}).get("src")
    info = html.find("div",attrs={"id":"js_profile_qrcode"}).find_all("span",attrs = {"class":"profile_meta_value"})
    #获取微信号
    AccountID = info[0].text
    #获取公众号简介
    AccountInstruction = info[1].text
    # print("1",postdate)
    # print("2",Author)
    # print("3",AccountName)
    # print("4",AccountQrcodeurl)
    # print("5",AccountID)
    # print("6",AccountInstruction)
    article_detail_info_dict['postdate'] = postdate
    article_detail_info_dict['Author'] = Author
    article_detail_info_dict['AccountName'] = AccountName
    article_detail_info_dict['AccountID'] = AccountID
    article_detail_info_dict['AccountQrcodeurl'] = AccountQrcodeurl
    article_detail_info_dict['AccountInstruction'] = AccountInstruction
    article_detail_info_dict['PageSource'] = PageSource
    time.sleep(2)

    return article_detail_info_dict

if __name__ == "__main__":

    keywordslist = ["区块链","比特币","以太坊","交易所"]
    # 设置浏览器需要打开的url
    for page in range(2,1000):
        try:
            print("The Current Page Is ",page)
            url = "http://weixin.sogou.com/weixin?query=%E5%8C%BA%E5%9D%97%E9%93%BE&type=2&page=" + str(page) + "&ie=utf8"  # 获取文章
            # url = "http://weixin.sogou.com/weixin?query=%E5%8C%BA%E5%9D%97%E9%93%BE&_sug_type_=&s_from=input&_sug_=y&type=1&page=12&ie=utf8"  # 获取公众号
            getarticle_brief_info(url)
            print("页面切换，睡眠30S...")
            time.sleep(30)
            # getarticle_detail_info()
            # getaccountinfo()
            # account_web_analysis(url)
        except Exception as e:
            print(e)