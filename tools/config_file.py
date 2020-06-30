#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :config_file.py
# @Time      :2020/6/9 1:15
# @Author    :江梅
import  configparser
from tools.do_path import GetPath

class ReadConfig():

    def read_config(self,file_name,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        return cf.get(section,option)

if __name__ == "__main__":
   res = ReadConfig().read_config(GetPath.Config_Path,'MODE','mode_test')
   print(type(res))