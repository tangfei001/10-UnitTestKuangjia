#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 12:10
# @Author  : Aries
# @Site    : 
# @File    : 01-测试套件一练习.py
# @Software: PyCharm
'''
按照测试类执行 addTest()
优化测试套件的方法:使用静态方法
'''
import unittest
from D10lianxi2.gujian import *

class TestLogin(GuJian):
	'''进行登录测试'''
	def test_001(self):
		'''第一个测试用例'''
		print('001')
	def test_002(self):
		'''第二个测试用例'''
		print('002')

	@staticmethod
	def suite():
		suite=unittest.TestSuite()
		suite.addTest(TestLogin)
		return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(TestLogin.suite())

