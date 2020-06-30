#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :do_path.py
# @Time      :2020/6/12 14:14
# @Author    :江梅
import os

class GetPath:
    Path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
    Config_Path =os.path.join(Path,'test_config','config_file.config')
    Excel_Path_01 = os.path.join(Path,'test_datas','test01.xlsx')
    Excel_Path_02 = os.path.join(Path, 'test_datas', 'test02.xlsx')
    Logging_Path = os.path.join(Path,'test_result','logging_data.txt')
    TestHtml_Path = os.path.join(Path,'test_result','test_result01.html')


if __name__ == "__main__":
    print(GetPath.Config_Path)
