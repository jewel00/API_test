#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :token_or_cookies.py
# @Time      :2020/6/8 20:41
# @Author    :江梅
#反射
from tools.do_path import GetPath #获取配置文件的路径
import pandas as pd

#保存数据（反射）
class GetDatas:
    Cookies = None
    Token = None
    loanId = None
    Phone = int(pd.read_excel(GetPath.Excel_Path_02,sheet_name='init').iloc[0,0]) #利用padans对数据进行分析
    add_memberId = int(pd.read_excel(GetPath.Excel_Path_02, sheet_name='init').iloc[1, 0])
    normal_tel = int(pd.read_excel(GetPath.Excel_Path_02, sheet_name='init').iloc[2, 0])
    admin_tel = int(pd.read_excel(GetPath.Excel_Path_02, sheet_name='init').iloc[3, 0])
    memberId = int(pd.read_excel(GetPath.Excel_Path_02, sheet_name='init').iloc[4, 0])
    vip_tel = int(pd.read_excel(GetPath.Excel_Path_02, sheet_name='init').iloc[5, 0])


if __name__ == "__main__":
    w = getattr(GetDatas,'tel_toubiao')
    print(w)