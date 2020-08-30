#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 19:21
# @Author  : Aries
# @Site    : 
# @File    : 08-测试套件二.py
# @Software: PyCharm
'''
思路:按照测试类执行
格式: unittest.makeSuite()
步骤:
	01:对类进行初始化unittest.TestSuite
	02:unittest.TestSuite(unittest.makeSuite(F10))
	03:执行测试套件.固定写法
'''
import unittest

class TaoJian2(unittest.TestCase):
	def setUp(self) -> None:
		print('开始执行')
	def tearDown(self) -> None:
		print('结束执行')
	'''要执行的测试用例'''
	def test_001(self):
		print('001')
	def test_002(self):
		print('002')

if __name__ == '__main__':
	#第一步&第二步
	suite=unittest.TestSuite(unittest.makeSuite(TaoJian2))
	#第三步
	unittest.TextTestRunner(verbosity=2).run(suite)