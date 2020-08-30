#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 19:06
# @Author  : Aries
# @Site    : 
# @File    : 07-测试套件一.py
# @Software: PyCharm
'''
重点内容1
中文说明:按照测试用例的顺序去执行
格式:addTest()
步骤:
	在主函数中
   01:对测试套件的类进行初始化 TestSuite()-测试套件的类  suite=unittest.TestSuite()
   02:将测试用例添加到addTest集合中  suite.addTest(BaiduTest('test_baidu_news'))
								suite.addTest(BaiduTest('test_baidu_map'))
    03:执行测试套件 unittest.TextTestRunner(verbosity=2).run(suite)

'''
#导包
import unittest

#定义一个测试类,所有的类继承unittest.TestCase类
class TaoJian1(unittest.TestCase):
	#使用测试固件
	def setUp(self) -> None:
		print('开始执行')
	def tearDown(self) -> None:
		print('结束执行')
	'''要执行的测试用例'''
	def test_001(self):
		'''001'''
		print('001')
	def test_002(self):
		'''002'''
		print('002')
#主函数
if __name__ == '__main__':
	#对类进行初始化 suite=unittest.TestSuite()
	suite=unittest.TestSuite()
	#按顺序执行测试用例  suite.addTest(BaiduTest('test_baidu_news'))
	suite.addTest(TaoJian1)
	#固定写法
	unittest.TextTestRunner(verbosity=2).run(suite)