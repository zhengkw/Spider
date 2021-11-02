#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/10/29 上午 11:53
# @Author  : kevin
# @File    : FileRWDemo.py
# @Software: PyCharm

def readFile(filePath):
    try:
        f = open(filePath)
        try:
            lines = f.readlines()

        except Exception:
            pass
        finally:
            f.close()
    except IOError as result:
        print(result)
    return lines


def writeFile(lines, filePath):
    f = open(filePath, "w")
    try:
        f.writelines(lines)
    except Exception as info:
        print(info)
    finally:
        f.close()


def copyFile(source, target):
    lines = readFile(source)
    writeFile(lines, target)
    print("copy success!")


copyFile("test.txt", "copy1.txt")
