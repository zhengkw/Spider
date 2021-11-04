#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime   : 21/11/04 下午 2:18
# @Author       : kevin
# @File         : xwltTest.py
# @Software     : PyCharm
# @UpdateTime   : 21/11/04 下午 2:18
# @Version      : v1.0.0

import xlwt
#定义一个excel中的book对象
workbook =xlwt.Workbook(encoding='utf-8')
#获取sheet对象
worksheet=workbook.add_sheet('sheet1')
worksheet.write()