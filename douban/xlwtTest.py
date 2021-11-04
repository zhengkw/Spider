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
worksheet.write(0,0,"第一个单元格内容") #arg1行，arg2列，arg3 写入内容
#定义一个新sheet，打印99乘法表，一个单元格对应一个计算公式+结果
sheet=workbook.add_sheet('99乘法表')

for i in range(0,9):
    i=i+1
    for j in range(0,9):
        if i == j: break
        j=j+1
    #     print(str(i)+'*'+str(j)+'='+str(i*j),end=" ")
    # print('\n')
        #写数据
        sheet.write(i-1,j-1,str(i)+'*'+str(j)+'='+str(i*j))
workbook.save('test.xls')

