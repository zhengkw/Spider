#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/29 下午 2:32
# @Author  : kevin
# @File    : spider.py
# @Software: PyCharm
# @UpdateTime : 21/10/29 下午 5:32
def main():
    # print("This is main Function")
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    # 2.保存数据
    savepath = '豆瓣Top250.xls'
    dbpath='testMovie.db'
    saveData2xls(datalist, savepath)
    SaveData2DB(datalist,dbpath)

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
    for i in range(0, 10):  # 调用获取页面信息的函数,利用分页的API
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
                otitle = re.sub('\s', " ", otitle)
                otitle = otitle.strip()
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
            # inq可能不存在，所以不用当成一个集合来取值
            inq = re.findall(flindInq, item)
            # 概述
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)
            else:
                data.append(" ")
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>用空格替代
            bd = re.sub('/', ' ', bd)  # 替换掉/
            bd = re.sub("\s", ' ', bd)  # 去掉\xa0
            data.append(bd.strip())  # 去掉前后空格是strip 和trim()类似
            # 将一部处理好的电影信息存放入datalist中
            datalist.append(data)
    # print(datalist)
    return datalist


# 指定一个URL网页内容
def askUrl(url):
    """
    :param url:需要获取文档的URL
    :return: 返回一个HTML
    """
    head = {
        "Cookie":"bid=J7RXdvka-3o; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.747511940.1636094413.1636094413.1636094413.1; __utmb=30149280.0.10.1636094413; __utmc=30149280; __utmz=30149280.1636094413.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmz=223695111.1636094413.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=223695111; __utmb=223695111.0.10.1636094413; __utma=223695111.1779063006.1636094413.1636094413.1636094413.1; dbcl2='249567916:DNoR+zOPAmw'; ck=lxu4; _pk_id.100001.4cf6=53a08c8471158930.1636094413.1.1636094524.1636094413.; __gads=ID=9e5dc260a7d24dfc-22fe39d38dce00ee:T=1636094523:RT=1636094523:S=ALNI_MYxhbcYx9LtY9KfsT3HjnU41_2G1w; push_noty_num=0; push_doumail_num=0" ,
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
def saveData2xls(datalist, path):
    print("saving....")
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)
    # 列抬头
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价人数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
        # 写入电影内容
    for i in range(0, 250):
        print("正在处理第%d条数据" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    try:
        book.save(path)
        print("写入完成，请查看文件！")
    except PermissionError as e:
        print("可能文件已经打开，请关闭文件后重试！\n写入失败，信息没有更新！")
        pass


def SaveData2DB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    # 对每一行的电影信息组装成一个sql语句
    for data in datalist:
        for index in range(len(data)):
            #优化，2个类型为数值型的字段不应该拼接双引号
            if index == 4 or index== 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into movie250(
            info_link, pic_link, cname, ename, score, rated, instroduction, info
            ) values (%s)''' % ",".join(data)  # data是一个list，用逗号将list里的元素添加
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()
    print("Saved!")


def init_db(dbpath):
    """
    :Author:  kevin
    :CreateTime:  21/11/05 上午 10:41
    :UpdateTime:  21/11/05 上午 10:41
    :param dbpath: db名称
    :return: None
    """
    sql = '''
    create table movie250(
    id integer primary key  autoincrement ,
    info_link text,
    pic_link text,
    cname varchar,
    ename varchar,
    score numeric,
    rated numeric,
    instroduction text,
    info text
    )
    '''

    try:
        conn = sqlite3.connect(dbpath)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        pass
    finally:
        conn.close()


if __name__ == '__main__':
    main()
    # init_db("testMovie.db")
