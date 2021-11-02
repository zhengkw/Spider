#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/28 下午 6:48
# @Author  : kevin
# @File    : dict.py
# @Software: PyCharm
#字典 同 map
info={"name":"kevin","age":19,"sex":"man"}
name=info.get("name")
print(name)
print(type(info))
u=info.get("u","hello")
print(u)