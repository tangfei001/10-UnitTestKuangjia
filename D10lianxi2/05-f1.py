#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 12:38
# @Author  : Aries
# @Site    : 
# @File    : 05-f1.py
# @Software: PyCharm
'''
01:断言
02:忽略测试用例的执行
03:让用例故意出错
----------------------------------
忽略测试用例思路:在测试用例的上面加装饰器
@unittest.skip('该功能已经取消，忽略该测试用例的执行')
需求:期望他失败
@unittest.expectedFailure
'''
import unittest
from D10lianxi2.gujian import *

def add(a,b):
	return a-b

class TestLogin(GuJian):
	def test_001(self):
		print('001')
	@unittest.skip('test_002用例不执行')
	def test_002(self):
		print('002')
	def test_003(self):
		print('003')
	@unittest.expectedFailure
	def test_004(self):
		self.assertEqual(add(2-3),1)
	@unittest.skip('不执行这个用例')
	def test_005(self):
		print('005')
if __name__ == '__main__':
    unittest.main(verbosity=2)