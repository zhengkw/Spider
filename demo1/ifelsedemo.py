#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/28 上午 11:27
# @Author  : kevin
# @File    : ifelsedemo.py
# @Software: PyCharm
while True:
    str_score = input("input your score! :\n")
    if str_score =='':
        str_score = "0"
    score = int(str_score)
    if score > 100 or score < 0:
        print("你这分数不是人得的啊！")
    elif score < 60:
        print("D")
    elif score < 80:
        print("C")
    elif score < 90:
        print("B")
    elif score < 100:
        print("A")
    else:
        print("S!!!!!")
