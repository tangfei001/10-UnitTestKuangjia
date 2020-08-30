#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 20:11
# @Author  : Aries
# @Site    : 
# @File    : allTestRun.py
# @Software: PyCharm
import unittest
import os
import HTMLTestRunner
import time

def allTest():
	suite=unittest.TestLoader().discover(start_dir=os.path.dirname(__file__),
	                                     pattern='test_*.py',
	                                     top_level_dir=None)
	return suite

def getNowTime():
	return time.strftime('%y-%m-%d %H_%M_%S',time.localtime(time.time()))

def run():
	fp=os.path.join(os.path.dirname(__file__),'report',getNowTime()+'testReport.html')
	HTMLTestRunner.HTMLTestRunner(stream=open(fp,'wb'),title='百度系统自动化测试',description='').run(allTest())

if __name__ == '__main__':
    run()