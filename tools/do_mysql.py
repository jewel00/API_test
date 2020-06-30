#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :do_mysql.py
# @Time      :2020/6/11 16:57
# @Author    :江梅
import pymysql
from tools.config_file import ReadConfig
from tools.do_path import GetPath


class GetDataFromMysql:

    @staticmethod
    def get_data_from_mysql(sql):

        db_config=eval(ReadConfig().read_config(GetPath.Config_Path,'MYSQL','db_config'))

        #创建一个数据库链接
        cnn = pymysql.connect(**db_config)

        #游标cursor
        cursor = cnn.cursor()

        #写sql语句
        query_sql = sql

        #执行语句
        cursor.execute(query_sql)

        #获取结果
        res = cursor.fetchone() #只能获取一个数据
        # res = cursor.fetchall() #能获取多个数据

        #关闭游标
        cursor.close()

        #关闭连接
        cnn.close()

        return res
if __name__ == "__main__":
    mysql_res = GetDataFromMysql.get_data_from_mysql('SELECT max(mobile_phone) FROM member')
    mysql_res = mysql_res[0]
    print(mysql_res)