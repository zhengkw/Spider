#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/29 上午 9:52
# @Author  : kevin
# @File    : FunctionTest.py
# @Software: PyCharm
def printLine(lineNum,lineLen):
    i=0
    while i<lineNum:
        i+=1
        print("-"*int(lineLen))

def add(a,b,c):
    return a+b+c
def avg(a,b,c):
    return add(a,b,c)/3

printLine(35,50)
print(add(4,5,6))
print(avg(2,4,6))