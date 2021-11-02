#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/29 上午 10:11
# @Author  : kevin
# @File    : args.py
# @Software: PyCharm
a=100
#局部&全局变量
def test1():
    a =300
    print(a)
    a =100
    print(a)

def test2():
    print(a)


#关键字 global
def test3():
    global a
    a=400
    print(a)

if __name__ == '__main__':
    test3()
    test2()