#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 19:29
# @Author  : Aries
# @Site    : 
# @File    : 09-测试套件三.py
# @Software: PyCharm
'''
中文描述:加载测试类
格式:TestLoader()  loadTestsFromTestCase(F11)
步骤:
	1:加载测试类 suite=unittest.TestLoader()
	2:加载测试用例  suite=unittest.TestLoader(). loadTestsFromTestCase(F11)
	3.执行测试用例-固定写法
'''
import unittest

class TaoJian3(unittest.TestCase):
	def setUp(self) -> None:
		print('开始执行')
	def tearDown(self) -> None:
		print('结束执行')
	def test_001(self):
		print('001')
	def test_002(self):
		print('002')
if __name__ == '__main__':
    suite=unittest.TestLoader().loadTestsFromTestCase(TaoJian3)
    unittest.TextTestRunner(verbosity=2).run(suite)
