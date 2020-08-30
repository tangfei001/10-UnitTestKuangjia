#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 18:21
# @Author  : Aries
# @Site    : 
# @File    : 02-测试用例的执行顺序.py
# @Software: PyCharm

import unittest
#所有的测试类都必须继承unittest.TestCase类
class Ceshi(unittest.TestCase):
	def test_001(self):
		print('1')
	def test_002(self):
		print('2')

if __name__ == '__main__':
    unittest.main(verbosity=2)