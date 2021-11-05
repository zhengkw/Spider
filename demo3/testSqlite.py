#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateTime   : 21/11/04 下午 6:07
# @Author       : kevin
# @File         : testSqlite.py
# @Software     : PyCharm
# @UpdateTime   : 21/11/04 下午 6:07
# @Version      : v1.0.0

import sqlite3

createSQL = '''
         create table emp(
         id int primary key not null ,
         name text not null ,
         age int not null ,
         classId int not null ,
         address char(50),
         salary real
         );
    '''


# 封装一个方法，操作sql
def SQLOption(sql):
    """
    :Author:  kevin
    :CreateTime:  21/11/04 下午 6:52
    :UpdateTime:  21/11/04 下午 6:52
    :param sql: sql语句
    :return: None
    """
    try:
        conn = sqlite3.connect("test.db")  # 当没有db文件，自动创建
        print("opened database successfully")
        cur = conn.cursor()  # 获取游标
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        pass
    finally:
        conn.close()
        print("closed database successfully")

def SelectOption(sql):
    conn = sqlite3.connect("test.db")  # 当没有db文件，自动创建
    print("opened database successfully")
    cur = conn.cursor()  # 获取游标
    rows=cur.execute(sql)
    for row in rows:
        print("id=",row[0],end=',')
        print("name=",row[1],end=',')
        print("age=",row[2],end=',')
        print("classId=",row[3],end=',')
        print("address=",row[4],end=',')
        print("salary=",row[5],end='\n')




# 插入语句
insetSQL = """
insert into emp (id,
         name,
         age,
         classId,
         address,
         salary) values(2,'lucy',18,42,'chengdu',8888.88)
"""

# update语句
updateSQL = """
update emp set age=22 where id=1;
"""
# 查询
selectSQL="""
select id,name,age,classId,address,salary from emp;
"""

if __name__ == '__main__':
    # SQLOption(createSQL)
    #SQLOption(insetSQL)
    #SQLOption(updateSQL)
    SelectOption(selectSQL)