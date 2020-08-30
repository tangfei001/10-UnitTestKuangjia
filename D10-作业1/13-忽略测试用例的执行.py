#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 20:23
# @Author  : Aries
# @Site    : 
# @File    : 13-忽略测试用例的执行.py
# @Software: PyCharm
'''
思路:在测试用例的上面加载函数装饰器
具体内容:
	01:@unittest.skip('该功能已经取消，忽略该测试用例的执行') 忽略这个用例
	02:@unittest.expectedFailure 期望他失败
'''
import unittest

def add(a,b):
	return a-b
class F1(unittest.TestCase):
	def test_001(self):
		print('这个用例继续执行')
	@unittest.skip('这个功能已被取消')
	def test_002(self):
		print('忽略这个用例的执行')
	@unittest.expectedFailure
	def test_003(self):
		self.assertEqual(add(2,3),1)
if __name__ == '__main__':
    unittest.main(verbosity=2)