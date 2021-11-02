#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/11/02 下午 2:01
# @Author  : kevin
# @File    : testBS4.py
# @Software: PyCharm

"""
演示示例用的是百度首页保存的本地html代码！

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
"""
#拿到第一个遇到的标签
print(bs.title)
print(bs.a)
#print(bs.head)
#1.Tag 标签及其内容，默认拿到第一个标签！
print(bs.head.meta)
#标签里的内容 NavigableString
NavigableString=bs.title.string
print(NavigableString)
print(type(NavigableString))
#标签中的属性值
print(bs.a.attrs)
#整个文档 BeautifulSoup
#print(type(bs))

#打印超链接里的内容
print(bs.a.string)
#如果解析到内容有注释符号<!-- --> 类型为 <class 'bs4.element.Comment'>
print(type(bs.a.string))

#还有访问节点前后，或者兄弟节点等，参考bs文档！

#文档的遍历 返回值是一个list
print(bs.head.contents[1])
"""
#文档的搜索
#字符串过滤：会查找与字符串完全匹配的内容
#t_list=bs.find_all("a")

#正则表达式搜索:使用search()方法来匹配内容
import re
# t_list=bs.find_all(re.compile("a"))
# print(t_list)

#方法 ：传入一个函数，根据函数要求搜索
"""
def name_is_exists(tag):
    #print(type(tag)) <class 'bs4.element.Tag'>
    return tag.has_attr("name")

t_list=bs.find_all(name_is_exists)
for item in t_list:
    print(item)
"""
#2.kwargs
#指定id为head
#t_list=bs.find_all(id="head")
#带class
"""    
t_list=bs.find_all(class_=True)

for item in t_list:
    print(item)
"""
# 3.text参数
#t_list=bs.find_all(text=["github","地图"])
"""
t_list=bs.find_all(text=re.compile("\d")) #应用正则表达式查找包含特定文本的内容(标签里的字符串)
for item in t_list:
    print(item)
"""
#4.limit
"""
t_list=bs.find_all("a",limit=3)
for item in t_list:
    print(item)
"""
#5.CSS选择器
#t_list=bs.select('title') #按标签查找
#t_list=bs.select(".mnav")#按类名查找，使用'.'
#t_list=bs.select("#u1") #id选择器 <div class="s-top-right s-isindex-wrap" id="u1"> 及其子内容
#t_list=bs.select("a[class='s-bri c-font-normal c-color-t']") #属性选择器
#t_list=bs.select("head > title") #通过子标签查找 ,<title>百度一下，你就看到全是广告</title>
# for item in t_list:
#     print(item)
t_list=bs.select(".mnav ~ .c-font-normal") #查询兄弟节点 '~'  标签类名为mnav同层次的类名为c-font-normal的所有标签
for item in t_list:
    print(item)
#print(t_list[0].get_text()) #得到数组中第一个元素并打印！