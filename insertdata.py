#coding:utf-8

import pymysql
import time
import os

def getcon():
    try:
        con = pymysql.connect(
            host="localhost",
            user="root",
            password="lin123456*",
            db="blockchain",
            port=3306,
            charset="utf8"
        )
    except Exception as e:
        con = None
        print(e)
    return con

def saveAccountdata(AccountName,AccountID,InstructionInfo,RenZhengInfo,ArticleUrlList,ImgUrl,QrcodeUrl = ""):
    con = getcon()
    try:
        getcountsql = "select count(*) from accountinfo where AccountName='%s'" % (AccountName)
        ArticleUrlList = pymysql.escape_string(ArticleUrlList)

        ImgUrl = pymysql.escape_string(ImgUrl)
        QrcodeUrl = pymysql.escape_string(QrcodeUrl)
        save_sql = "insert into AccountInfo(AccountName,AccountID,InstructionInfo,RenZhengInfo,ArticleUrlList,ImgUrl,QrcodeUrl,GetTime) value ('%s','%s','%s','%s','%s','%s','%s',now())" \
                   % (AccountName,AccountID,InstructionInfo,RenZhengInfo,ArticleUrlList,ImgUrl,QrcodeUrl)
        with con:
            cur = con.cursor()
            cur.execute(getcountsql)
            count = cur.fetchall()[0][0]
            if count == 1:
                print(AccountName,"-->",AccountID,"数据存在，不进行存储.")
            else:
                cur.execute(save_sql)
                con.commit()
                print(AccountName,"-->",AccountID,"存储完成.")
    except Exception as e:
        print("存储",AccountName,"-->",AccountID,"时出现异常，信息如下:",e)
        print(AccountName)
        print(AccountID)
        print(InstructionInfo)
        print(RenZhengInfo)
        print(ArticleUrlList)
        print(ImgUrl)
        print(QrcodeUrl)

def saveArticleBriefData(Articletitle,PostDate,Author,FromAccountName,FromAccountID,Articlepic,Articletitleurl,Articlecontentins):
    """
    :param Articletitle:
    :param PostDate:
    :param Author:
    :param FromAccountName:
    :param FromAccountID:
    :param Articlepic:
    :param Articletitleurl:
    :param Articlecontentins:
    :return:
    """
    print("正在存储公众号文章简要信息...")
    con = getcon()
    try:

        getcountsql = "select count(*) from articlebriefinfo where FromAccountName='%s' and FromAccountID = '%s' and ArticleTitle = '%s'" % (FromAccountName,FromAccountID,Articletitle)
        Articlepic = pymysql.escape_string(Articlepic)
        Articletitleurl = pymysql.escape_string(Articletitleurl)
        save_sql = "insert into articlebriefinfo(ArticleTitle,PostDate,Author,FromAccountName,FromAccountID,ArticlePicUrl,ArticleUrl,ArticleContentIns,GetTime) value ('%s','%s','%s','%s','%s','%s','%s','%s',now())" \
                   % (Articletitle,PostDate,Author,FromAccountName,FromAccountID,Articlepic,Articletitleurl,Articlecontentins)
        with con:
            cur = con.cursor()
            cur.execute(getcountsql)
            count = cur.fetchall()[0][0]
            if count == 1:
                print(FromAccountName, "<-->", FromAccountID,"<-->",Articletitle, "数据存在，不进行存储.")
            else:
                cur.execute(save_sql)
                con.commit()
                print(FromAccountName, "<-->", FromAccountID,"<-->",Articletitle, "存储完成.")
    except Exception as e:
        print("存储",FromAccountName, "<-->", FromAccountID,"<-->",Articletitle, "时出现异常，信息如下:", e)

def saveArticlePicData(FromAccountName,FromAccountID,Articletitle,Articlepic):
    """
    :param FromAccountName:
    :param FromAccountID:
    :param Articletitle:
    :param Articlepic:
    :return:
    """
    print("正在存储公众号文章封面图片信息...")
    con = getcon()
    try:

        getcountsql = "select count(*) from articlepicinfo where AccountName='%s' and AccountID = '%s' and ArticleTitle = '%s'" % (FromAccountName,FromAccountID,Articletitle)
        Articlepic = pymysql.escape_string(Articlepic)
        PicContent = ""
        save_sql = "insert into articlepicinfo(AccountName,AccountID,ArticleTitle,PicUrl,PicContent,GetTime) value ('%s','%s','%s','%s','%s',now())" \
                   % (FromAccountName, FromAccountID, Articletitle, Articlepic, PicContent)
        with con:
            cur = con.cursor()
            cur.execute(getcountsql)
            count = cur.fetchall()[0][0]
            if count == 1:
                print(FromAccountName, "<-->", FromAccountID,"<-->",Articletitle, "图片数据存在，不进行存储.")
            else:
                cur.execute(save_sql)
                con.commit()
                print(FromAccountName, "<-->", FromAccountID,"<-->",Articletitle, "图片数据存储完成.")
    except Exception as e:
        print("存储", FromAccountName, "<-->", FromAccountID,"<-->",Articletitle, "图片数据时出现异常，信息如下:", e)

def saveArticlePageSource(FromAccountName,FromAccountID,Articletitle,PageSource):
    """
    :param FromAccountName:
    :param FromAccountID:
    :param Articletitle:
    :param PageSource:
    :return:
    """
    print("正在存储公众号文章源码信息...")
    con = getcon()
    try:

        getcountsql = "select count(*) from articlepagesource where AccountName='%s' and AccountID = '%s' and ArticleTitle = '%s'" % (
        FromAccountName, FromAccountID, Articletitle)
        PageSource = pymysql.escape_string(PageSource)
        save_sql = "insert into articlepagesource(AccountName,AccountID,ArticleTitle,PageSource,GetTime) value ('%s','%s','%s','%s',now())" \
                   % (FromAccountName, FromAccountID, Articletitle, PageSource)
        with con:
            cur = con.cursor()
            cur.execute(getcountsql)
            count = cur.fetchall()[0][0]
            if count == 1:
                print(FromAccountName, "<-->", FromAccountID, "<-->", Articletitle, "源码数据存在，不进行存储.")
            else:
                cur.execute(save_sql)
                con.commit()
                print(FromAccountName, "<-->", FromAccountID, "<-->", Articletitle, "源码数据存储完成.")
    except Exception as e:
        print("存储", FromAccountName, "<-->", FromAccountID, "<-->", Articletitle, "源码数据时出现异常，信息如下:", e)

def getaccountinfo():
    con = getcon()
    with con:
        getsql = "select AccountName,AccountID,ArticleUrlList from AccountInfo"
        cur = con.cursor()
        cur.execute(getsql)
        datas = cur.fetchall()
        if len(datas) >=1:
            return datas
        else:
            print("未检索到相关公众号数据")
            return None

if __name__ == "__main__":
    getaccountinfo()
