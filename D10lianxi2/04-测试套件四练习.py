#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 12:28
# @Author  : Aries
# @Site    : 
# @File    : 04-测试套件四练习.py
# @Software: PyCharm
'''
按测试模块来执行(TestLoader)
'''
import unittest
from D10lianxi2.gujian import *

class TestLogin_01(GuJian):
	'''要执行的测试用例'''
	def test_001(self):
		'''第一个测试用例'''
		print('001')
	def test_002(self):
		'''第二个测试用例'''
		print('002')

class TestLogin_02(GuJian):
	'''要执行的测试用例2'''
	def test_003(self):
		'''第三个测试用例'''
		print('003')
	def test_004(self):
		'''第四个测试用例'''
		print('004')

class TestRunner(GuJian):
	'''优化测试套件'''
	@staticmethod
	def suite():
		suite=unittest.TestLoader().loadTestsFromModule('04-测试套件四练习.py')
		return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(TestRunner.suite())