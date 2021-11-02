#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/29 上午 11:02
# @Author  : kevin
# @File    : FileOption.py
# @Software: PyCharm
#打开文件  w模式下 不存在文件，则新建文件
f=open("test.txt","r")
content=f.read(5)
print(content)
print(f.read(6))
f.close()

f1=open("test.txt","r")
contents=f1.readlines(5)
print(contents)
for line in contents:
    print(line)
    words=line.split(",")
    for word in words:
        print(word)
f1.close()
# import os
# os.rename("test1.txt","test.txt")