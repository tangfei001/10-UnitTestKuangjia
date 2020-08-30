#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 20:05
# @Author  : Aries
# @Site    : 
# @File    : test_baidu_link.py
# @Software: PyCharm
import unittest
from testCase.gujian import *

class TestBaiduLink(GuJian):
	'''百度搜索'''
	def test_001(self):
		'''第一个测试用例'''
		print('001')
	def test_002(self):
		'''第二个测试用例'''
		print('002')
	def test_003(self):
		'''第三个测试用例'''
		print('003')

if __name__ == '__main__':
    unittest.main(verbosity=2)