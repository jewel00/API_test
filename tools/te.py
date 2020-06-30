#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :te.py
# @Time      :2020/6/14 14:56
# @Author    :江梅
from tools.do_mysql import GetDataFromMysql
from tools.get_datas import GetDatas
datas ={'select_sql':'{"sql":"SELECT LeaveAmount FROM member WHERE MobilePhone = ${vip_tel}"}','eee':'2222'}
e = eval(datas['select_sql'])['sql']
print(e)

if __name__ == "__main__":
    pass