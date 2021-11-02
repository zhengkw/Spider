#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/28 下午 2:08
# @Author  : kevin
# @File    : cycle.py
# @Software: PyCharm
'''
for i in range(5):
    print(i)
for i in range(0,11,3):
    print(i)
'''
'''
name="chengdu"
for x in name:
    print(x,end='\t')
'''
'''
a=["a","b","cc","dna"]
for i in range(len(a)):
    print(i,a[i])
'''
i = 1
sum = 0
while i <= 100:
    sum =sum+i
    i+=1

print(sum, end='')
