#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 12:18
# @Author  : Aries
# @Site    : 
# @File    : 02-测试套件2练习.py
# @Software: PyCharm
'''
按测试类执行 makeSuite()
'''
import unittest
from D10lianxi2.gujian import *

class TestLogin(GuJian):
	'''要执行的测试用例'''
	def test_001(self):
		'''第一个测试用例'''
		print('001')
	def test_002(self):
		'''要执行的测试用例2'''
		print('002')

	@staticmethod
	def suite():
		suite=unittest.TestSuite(unittest.makeSuite(TestLogin))
		return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(TestLogin.suite())
