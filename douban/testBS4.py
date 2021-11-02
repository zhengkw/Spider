#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/11/02 下午 2:01
# @Author  : kevin
# @File    : testBS4.py
# @Software: PyCharm

"""
BeautifulSoup4将复杂的HTML文档转换成一个树形结构，每个节点都是Python对象，所有对象可以分为下面4种
1.Tag
2.NavigableString
3.BeautifulSoup
4.Comment
"""

from bs4 import BeautifulSoup
file=open("./baidu.html","rb")
html=file.read()
bs=BeautifulSoup(html,"html.parser")
print(bs.title)
