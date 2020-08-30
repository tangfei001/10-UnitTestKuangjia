#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 12:24
# @Author  : Aries
# @Site    : 
# @File    : 03-测试套件三练习.py
# @Software: PyCharm
'''
加载测试类(TestLoader)--单类测试
'''
import unittest
from D10lianxi2.gujian import *

class TestLogin(GuJian):
	'''要执行的测试用例'''
	def test_001(self):
		'''第一个测试用例'''
		print('001')
	def test_002(self):
		'''第二个测试用例'''
		print('002')

	@staticmethod
	def suite():
		suite=unittest.TestLoader().loadTestsFromTestCase(TestLogin)
		return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(TestLogin.suite())

