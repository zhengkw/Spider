#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/29 下午 2:32
# @Author  : kevin
# @File    : spider.py
# @Software: PyCharm
def main():
    # print("This is main Function")
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)


import re  # 正则表达式，进行文字匹配

# 正则匹配规则，根据同包target.html结果做正则匹配
# 匹配影片链接
findLink = re.compile(r'<a href="(.*?)">')  # 创建一个正则表达式对象，表示规则（字符串的模式）
# 匹配影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # 获取图片资源链接,re.S忽略这里可能出现的换行符，因为`.`不包含换行符
# 匹配片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概况
flindInq = re.compile(r'<span class="inq">(.*)</span>')
# 相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)
from bs4 import BeautifulSoup  # 网页解析，数据获取
import urllib.request, urllib.error  # 指定 URL获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行数据库操作


# 爬取网页
def getData(baseUrl):
    datalist = []
    for i in range(0, 1):  # 调用获取页面信息的函数,利用分页的API
        url = baseUrl + str(i * 25)
        html = askUrl(url)
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item)
            data = []  # 保存一部电影的所有信息
            item = str(item)
            # 链接
            link = re.findall(findLink, item)[0]  # re库用来通过正则表达式查找指定的字符串 有可能同时找到2个一模一样的，只取第一个
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            # 片名
            titles = re.findall(findTitle, item)  # 片名一般只有中文名，有部分是有外文
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  # 去掉无关符号
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')  # 没有外国名字的站位留空
            # print(link)
            # 评分
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            # 评价数
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            inq = re.findall(flindInq, item)[0]
            # 概述
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)
            else:
                data.append(" ")
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>用空格替代
            bd = re.sub('/', ' ', bd)  # 替换掉/
            data.append(bd.strip())  # 去掉前后空格是strip 和trim()类似
            # 将一部处理好的电影信息存放入datalist中
            datalist.append(data)
    print(datalist)
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
        # print(html)
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
