#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :write_test_case.py
# @Time      :2020/6/8 22:11
# @Author    :江梅
import unittest
import json
from tools.http_request import HttpRequest_Mode
from ddt import ddt,data
from tools.get_excel_data import GetDataFromExcel
from tools.get_datas import GetDatas
from tools.do_path import GetPath
from tools.get_my_log import Get_MyLog
from tools.do_mysql import GetDataFromMysql
import time



@ddt
class HttpTestCase(unittest.TestCase):
    recharge_datas = GetDataFromExcel(GetPath.Excel_Path_02, 'recharge').get_test_datas()
    login_datas = GetDataFromExcel(GetPath.Excel_Path_02, 'login').get_test_datas()
    register_datas = GetDataFromExcel(GetPath.Excel_Path_02, 'register').get_test_datas()
    add_datas = GetDataFromExcel(GetPath.Excel_Path_02, 'add').get_test_datas()

    @data(*login_datas)
    def test_loagin_api(self,test_data): #登录测试用例
        res = HttpRequest_Mode().http_requests('post', test_data['url'],eval(test_data['data']))
        try:
            self.assertEqual(str(test_data['code']), res.json()['code'])
            Test_Result = 'PASS'
        except Exception as e:
            Test_Result = 'FAILED'
            Get_MyLog().error("{}".format(e))
            raise e
        finally:
            Get_MyLog().info('把测试结果写入EXCEL！！')
            GetDataFromExcel(GetPath.Excel_Path_02,'login').write_back_result(test_data['case'],str(res.json()),Test_Result)

    @data(*register_datas)
    def test_register_api(self,test_data): #写注册测试用例

        res = HttpRequest_Mode().http_requests('post', test_data['url'],eval(test_data['data']))
        try:
            self.assertEqual(str(test_data['code']), res.json()['code'])
            Test_Result = 'PASS'
        except Exception as e:
            Test_Result = 'FAILED'
            Get_MyLog().error("{}".format(e))
            raise e
        finally:
            Get_MyLog().info('把测试结果写入EXCEL！！')
            GetDataFromExcel(GetPath.Excel_Path_02,'register').write_back_result(test_data['case'],str(res.json()),Test_Result)

    @data(*recharge_datas)
    def test_recharge_api(self,test_data): #写充值测试用例

        head = None
        amount_result=''
        Test_Result = ''
        if test_data['select_sql'] != None:
            sql = eval(test_data['select_sql'])['sql']
            befor_mount = GetDataFromMysql.get_data_from_mysql(sql)[0]
            Get_MyLog().info('充值之前的价格{}'.format(befor_mount))
            res = HttpRequest_Mode().http_requests('post', test_data['url'],eval(test_data['data']),head,getattr(GetDatas,'Cookies'))
            if res.cookies:
                setattr(GetDatas,'Cookies',res.cookies)

            after_mount = GetDataFromMysql.get_data_from_mysql(sql)[0]
            Get_MyLog().info('充值之后的价格{}'.format(after_mount))

            if abs(befor_mount-after_mount) == int(eval(test_data['data'])['amount']):
                amount_result = 'PASS'
                Get_MyLog().info('金额测试通过')
            else:
                amount_result = 'Failed'
                Get_MyLog().info('金额测试不通过')

            try:
                self.assertEqual(str(test_data['code']), res.json()['code'])
                Test_Result = 'PASS'
            except Exception as e:
                Get_MyLog().error("{}".format(e))
                Test_Result = 'FAILED'
            finally:
                GetDataFromExcel(GetPath.Excel_Path_02, 'recharge').write_back_result(test_data['case'],str(res.json()), Test_Result,amount_result)
            print('有sql{}'.format(test_data['case']))
        else:
            res = HttpRequest_Mode().http_requests('post', test_data['url'],eval(test_data['data']),head,getattr(GetDatas,'Cookies'))
            if res.cookies:
                setattr(GetDatas,'Cookies',res.cookies)

            try:
                self.assertEqual(str(test_data['code']), res.json()['code'])
                Test_Result = 'PASS'
            except Exception as e:
                Get_MyLog().error("{}".format(e))
                Test_Result = 'FAILED'
            finally:
                GetDataFromExcel(GetPath.Excel_Path_02,'recharge').write_back_result(test_data['case'],str(res.json()),Test_Result,amount_result)

    @data(*add_datas)
    def test_add_api(self, test_data):  # 写加标测试用例
        add_memberId = str(getattr(GetDatas,'add_memberId'))
        sql = 'SELECT max(Id) FROM loan WHERE MemberID=add_memberId'
        sql=sql.replace('add_memberId',add_memberId)
        mysql_loanId = GetDataFromMysql.get_data_from_mysql(sql)[0]
        if mysql_loanId:
            setattr(GetDatas,'loanId',mysql_loanId)
        if test_data['data'].find('${loanId}') != -1:
            test_data['data'] = test_data['data'].replace('${loanId}',str(getattr(GetDatas,'loanId')))
        head = None
        res = HttpRequest_Mode().http_requests('post', test_data['url'], eval(test_data['data']), head,
                                               getattr(GetDatas, 'Cookies'))
        if res.cookies:
            setattr(GetDatas, 'Cookies', res.cookies)
            print(getattr(GetDatas, 'Cookies'))
        try:
            self.assertEqual(str(test_data['code']), res.json()['code'])
            Test_Result = 'PASS'
        except Exception as e:
            Get_MyLog().error("{}{}".format(e,res.json()))
            Test_Result = 'FAILED'
        finally:
            Get_MyLog().info('把测试结果写入EXCEL！！')
            GetDataFromExcel(GetPath.Excel_Path_02, 'add').write_back_result(test_data['case'],
                                                                                  str(res.json()), Test_Result)


if __name__ == "__main__":
    pass

    # HttpTestCase().test_recharge_api()
