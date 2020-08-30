#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 19:46
# @Author  : Aries
# @Site    : 
# @File    : 11-优化测试套件.py
# @Software: PyCharm
'''
思路:使用面向对象中的静态方法的思路去解决
拓展:
	静态方法的特征
    01:引用 @staticmethod
	02:没有self参数,需自己定义一个参数 def conn(uesr)
	03:调用的时候直接使用类名来进行调用  Per.conn('duod')
优化的步骤:
	01:在测试类中分离第一步和第二步
	02:在主函数中写第三步-固定写法
	03:run()中 如F13.suite 直接使用类名进行调用
'''
import unittest

class YouHua(unittest.TestCase):
	def setUp(self) -> None:
		print('开始执行')
	def tearDown(self) -> None:
		print('结束执行')
	def test_001(self):
		print('001')
	def test_002(self):
		print('002')
	'''
	01:使用面向对象的静态方法进行优化测试组件
	步骤:
		01:@staticmethod
		02:
			def suite():
			suite=unittest.TestLoader().loadTestsFromTestCase(YouHua)
	'''
	@staticmethod
	def suite():
		suite=unittest.TestLoader().loadTestsFromTestCase(YouHua)
		return suite
if __name__ == '__main__':
	#03
    unittest.TextTestRunner(verbosity=2).run(YouHua.suite())