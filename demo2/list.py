#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/28 下午 5:29
# @Author  : kevin
# @File    : list.py
# @Software: PyCharm
schoolName=[["北京大学","清华大学","北京邮电大学"],["天津大学","南开大学"],["四川大学","西南财经"]]
print(schoolName[1][0])

offices=[[],[],[]]
names=["a","b","c","d","e","f","g","h"]
import random

for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)

for office in offices:
    print(office)
    for name in office:
        print(name)

