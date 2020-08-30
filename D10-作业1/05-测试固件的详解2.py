#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 18:51
# @Author  : Aries
# @Site    : 
# @File    : 05-测试固件的详解2.py
# @Software: PyCharm
'''
测试固件2:setUpClass(cls) tearDownClass(cls)
格式
	@classmethod
	def setUpClass(cls):
		xxx
用法:只执行一次
思路:使用面向对象中的类方法  @classmethod
注意:每个测试用例执行完毕必须初始化 self.driver.back()
'''
import unittest
from selenium import webdriver

class F1(unittest.TestCase):
	'''
	测试估计2
	'''
	@classmethod
	def setUpClass(cls) -> None:
		cls.driver = webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)
		cls.driver.get('http://www.baidu.com')
	@classmethod
	def tearDownClass(cls) -> None:
		cls.driver.quit()
	'''测试用例'''
	def test_baidu_news(self):
		self.driver.find_element_by_link_text('新闻').click()
		self.driver.back()

	def test_baidu_map(self):
		self.driver.find_element_by_partial_link_text('图').click()
		self.driver.back()

	def test_baidu_mbq(self):
		self.driver.find_element_by_partial_link_text('地图').click()
		self.driver.back()

#主函数
if __name__ == '__main__':
    unittest.main(verbosity=2)

