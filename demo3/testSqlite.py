#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime   : 21/11/04 下午 6:07
# @Author       : kevin
# @File         : testSqlite.py
# @Software     : PyCharm
# @UpdateTime   : 21/11/04 下午 6:07
# @Version      : v1.0.0

import sqlite3
conn=sqlite3.connect("test.db")
print("Opened database successfully")