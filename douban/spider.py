#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/29 下午 2:32
# @Author  : kevin
# @File    : spider.py
# @Software: PyCharm
def main():
    print("This is main")
    askUrl("https://movie.douban.com/top250?start=0")


from bs4 import BeautifulSoup  # 网页解析，数据获取
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定 URL获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行数据库操作


# 爬取网页
def getData(baseUrl):
    datalist = []
    for i in range(0, 10): #调用获取页面信息的函数,利用分页的API
        url = baseUrl + str(i * 25)
        html=askUrl(url)
         # 逐一解析数据


    return datalist


# 指定一个URL网页内容
def askUrl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def saveData(dbpath):
    pass


if __name__ == '__main__':
    main()
    # baseurl = "https://movie.douban.com/top250"
    # savepath = ".\\Top250.xls"
