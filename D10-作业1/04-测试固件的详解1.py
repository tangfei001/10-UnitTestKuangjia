#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 18:46
# @Author  : Aries
# @Site    : 
# @File    : 04-测试固件的详解1.py
# @Software: PyCharm
'''
测试固件1: setUp&tearDown
格式:setUp()  tearDown()
用法:有多少个测试用例就执行多少次
'''
import unittest

class Gujian(unittest.TestCase):
	'''
	测试固件
	'''
	def setUp(self) -> None:
		print('开始执行')
	def tearDown(self) -> None:
		print('结束执行')
	'''要执行的测试用例'''
	def test_001(self):
		print('1')
	def test_002(self):
		print('2')
	def test_003(self):
		print('3')
#主函数
if __name__ == '__main__':
	#这个是固定写法
    unittest.main(verbosity=2)