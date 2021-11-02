#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/28 下午 4:17
# @Author  : kevin
# @File    : DBoption.py
# @Software: PyCharm
#对数据进行持久化操作
# append
'''
print("---"*15 +"before"+"---"*15)
namelist=["12","233","2323"]
print(namelist)
namelist.append("kevin")
b=["kevin","king"]
print("---"*15 +"after"+"---"*15)
print(namelist)
namelist.append(b)
print(namelist)
namelist.extend(b) #将B拆开加入到namelist中
print(namelist)
'''
'''
#【insert】
a=["123",213123,22]
b=["kevin"]
c='23'
a.insert(3,c)
b.insert(1,c)
print(a)
print(b)
'''
'''
#delete
a=["123",213123,22]
b=["123",213123,22]
del a[1]#指定索引删除
print(a)
a.pop() #弹出末尾
print(a)
b.remove("123") #从前往后，删掉找到的第一个！
print(b)
'''
'''
#update
namelist=["12","233","2323"]
namelist[0]='kevin'
print(namelist)
'''
'''
#query
namelist=["12","233","2323"]
findname='233'
if findname in namelist:
    print("here is it!")
'''

a=["a","b","c","d","e","for","f","h","c","b","c","b","c"]
print(a.index("f",2,7))
a.reverse()
print(a)
a.sort(reverse=True)
print(a)
print(a.count("c"))

