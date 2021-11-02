#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/28 下午 1:40
# @Author  : kevin
# @File    : randomdemo.py
# @Software: PyCharm
import random

def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        print("请输入数字1，2，3，请勿输入别的字符！")
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
    return False


while True:
    x=random.randint(0,2)
    y=input("请输入以下整数中的一个(0【剪刀】,1【石头】,2【布】) ：\n")
    if is_number(y) :
        z=int(y)
        if z<0 or z >2 :
            print("非法输入,数值已经越界！！！！！！！")
        elif z-x==0 :
            print("电脑输出的是 %s,你输入的是 %s 平局"%(x,z))
        elif z-x==1 :
            print("电脑输出的是 %s,你输入的是 %s 你赢了"%(x,z))
        else:
            print("电脑输出的是 %s,你输入的是 %s 你输了"%(x,z))
    else:
        continue