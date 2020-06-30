#!/usr/bin/env python

# -*- coding:utf-8 -*-
# @FileName  :get_my_log.py
# @Time      :2020/6/11 1:33
# @Author    :江梅
import logging
import os
from tools.do_path import GetPath

class Get_MyLog:
    def get_mylog(self,msg,level):
        path = GetPath.Logging_Path
        #定义一个日志收集器my_log
        my_log = logging.getLogger("接口自动化")
        #设定级别
        my_log.setLevel('DEBUG')
        #设置日志输入格式
        formatter = formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')
        #创建一个我们自己输出的渠道
        ch = logging.StreamHandler()
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter)
        fh = logging.FileHandler(path,encoding="utf-8")
        fh.setLevel("DEBUG")
        fh.setFormatter(formatter)
        #两者对接
        my_log.addHandler(ch)
        my_log.addHandler(fh)

        #收集日志
        if level == 'DEBUG':
           my_log.debug(msg)
        elif level == 'INFO':
           my_log.info(msg)
        elif level == 'WARNING':
            my_log.warning(msg)
        elif level == 'ERROR':
            my_log.error(msg)
        elif level == 'CRITICAL':
            my_log.critical(msg)

        #关闭渠道
        my_log.removeHandler(ch)
        my_log.removeHandler(fh)

    def debug(self,msg):
        self.get_mylog(msg,'DEBUG')
    def info(self,msg):
        self.get_mylog(msg,'INFO')
    def wring(self,msg):
        self.get_mylog(msg,'WARNING')
    def error(self,msg):
        self.get_mylog(msg,'ERROR')
    def critical(self,msg):
        self.get_mylog(msg,'CRITICAL')

if __name__ == '__main__':
    # Get_MyLog().get_mylog('这是我的第一条打印出来的日志','CRITICAL')
    Get_MyLog().info('这是我的第二条打印出来的日志')
    # print(os.getcwd())
