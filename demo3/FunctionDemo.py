#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/29 上午 9:41
# @Author  : kevin
# @File    : FunctionDemo.py
# @Software: PyCharm
#基本函数
def printinfo():
    print("-"*30)
    print("hello,dadaliya")
#调用
printinfo()

#带参数
def add2Num(a,b):
    return a+b

c=add2Num(2,6.2)
print(c)

def divid(a,b):
    shang=a//b
    yushu=a%b
    return shang,yushu #多返回值用逗号分割
sh,yu=divid(5,2)
print("sh=%d,yu=%d"%(sh,yu))