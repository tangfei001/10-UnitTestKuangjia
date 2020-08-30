#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 18:44
# @Author  : Aries
# @Site    : 
# @File    : 03-UnitTest中verbosity关键字的详解.py
# @Software: PyCharm
'''
0-代表得到执行的测试总数和全局结果
1.代表得到成功的显示,失败的显示F,错误的显示E E.F  .表示成功
2-得到详细的信息
'''
import unittest

class F1(unittest.TestCase):
	def test_001(self):
		print('1')
	def test_002(self):
		print('2')
	def test_003(self):
		print('3')

if __name__ == '__main__':
    #unittest.main(verbosity=0)
	#unittest.main(verbosity=1)
	unittest.main(verbosity=2)