#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :suite_testcase.py
# @Time      :2020/6/9 0:44
# @Author    :江梅
import unittest
import HTMLTestRunner
from tools.write_test_case_cookies import HttpTestCase
from tools.do_path import GetPath

class SuiteTestCase:
    def suite_testcase(self):
        suite = unittest.TestSuite()
        loder = unittest.TestLoader()
        suite.addTest(loder.loadTestsFromTestCase(HttpTestCase))

        with open(GetPath.TestHtml_Path,'wb') as file:
            runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2,
                                                   title='我的第一个项目', description='我的的第一个实战项目测试结果')
            runner.run(suite)

if __name__ == "__main__":
    SuiteTestCase().suite_testcase()
