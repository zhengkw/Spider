#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/29 下午 3:06
# @Author  : kevin
# @File    : testurllib.py
# @Software: PyCharm
import urllib.request

# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

# post请求
# import urllib.parse
# data=bytes(urllib.parse.urlencode({"hello":"kevin"}),encoding="utf-8")
# try:
#     response=urllib.request.urlopen("http://httpbin.org/post",data=data,timeout=1)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("timeout!")

# status code
# response=urllib.request.urlopen("http://httpbin.org/get")
# print(response.status)

# 获取header中的信息
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.getheader("Server"))


#封装header
"""
data=bytes(urllib.parse.urlencode({"hello":"kevin"}),encoding="utf-8")
#url = "http://www.douban.com"
url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
"""


url="https://www.douban.com"
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))