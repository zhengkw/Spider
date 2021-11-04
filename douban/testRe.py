#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/11/03 下午 2:42
# @Author  : kevin
# @File    : testRe.py
# @Software: PyCharm
import re
#创建模式对象
pat=re.compile("AA") #括号内是正则表达式
res=pat.search("ssAAdafaaAA") #search参数为被校验字符串
#<re.Match object; span=(2, 4), match='AA'> 只能找到第一次匹配到的
print(res)

#没有模式对象
m=re.search("asd","AHBads") #前面第一个参数为规则，第二个参数为被校验对象。

n=re.findall("[A-Z]+","adsTTdafAAbbba") #匹配所有出现的第一个参数中的内容！
print(n)

#sub
print(re.sub("a","A","adsfasliihia")) #找到a用A替换，目标为第三个参数

# r 原始字符串 用法:字符串前面加上r，不转义字符串内的内容
a=r"\aabd-\'"
print(a)