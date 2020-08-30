#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 19:35
# @Author  : Aries
# @Site    : 
# @File    : 10-测试套件4.py
# @Software: PyCharm
'''
中文描述:按测试模块来执行(针对多个测试类)
格式:TestLoader()  loadTestsFromModule('f8.py')
步骤:
	1:进行初始化 suite=unittest.TestLoader()
	2:加载测试模块 suite=unittest.TestLoader().loadTestsFromModule('f8.py')
	3:执行测试固定写法
'''
import unittest

#第一个测试类
class F1(unittest.TestCase):
	def setUp(self) -> None:
		print('准备执行')
	def tearDown(self) -> None:
		print('执行完毕')
	def test_001(self):
		print('001')
	def test_002(self):
		print('002')

#第二个测试类
class F2(unittest.TestCase):
	def setUp(self) -> None:
		print('开始执行')
	def tearDown(self) -> None:
		print('完成任务')
	def test_003(self):
		print('003')
	def test_004(self):
		print('004')
#主函数
if __name__ == '__main__':
    #第一步$第二步
    suite = unittest.TestLoader().loadTestsFromModule('10-测试套件4.py')
    unittest.TextTestRunner(verbosity=2).run(suite)
