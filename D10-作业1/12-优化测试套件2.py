#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 19:55
# @Author  : Aries
# @Site    : 
# @File    : 12-优化测试套件2.py
# @Software: PyCharm
'''
问题:当有多个测试类时如何优化测试套件
解决方法:使用面向对象中的类的静态方法解决
'''
import unittest

#第一个测试类
class F1(unittest.TestCase):
	def setUp(self) -> None:
		print('开始执行')
	def tearDown(self) -> None:
		print('结束执行')
	def test_001(self):
		print('001')
	def test_002(self):
		print('002')

#第二个测试类
class F2(unittest.TestCase):
	def setUp(self) -> None:
		print('开始执行')
	def tearDown(self) -> None:
		print('结束执行')
	def test_003(self):
		print('003')
	def test_004(self):
		print('004')
#解决思路
'''
01:定义一个测试类
02:使用面向对象中的静态方法优化测试套件
'''
class F3(unittest.TestCase):
	@staticmethod
	def suite():
		suite=unittest.TestLoader().loadTestsFromModule('12-优化测试套件2.py')
		return suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(F1.suite(),F2.suite())