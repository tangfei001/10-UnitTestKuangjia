#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 19:03
# @Author  : Aries
# @Site    : 
# @File    : 06-测试用例的编写事项.py
# @Software: PyCharm
'''
01:测试用例的命令
02:测试用例的注释
03:断言
'''
import  unittest
from selenium import  webdriver

class F4(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)
		cls.driver.get('http://www.baidu.com')

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	'''百度首页链接测试'''
	def test_user_del(self):
		'''首页链接测试:验证新闻的链接'''
		self.driver.find_element_by_link_text('新闻').click()
		self.driver.back()

	def test_user_add(self):
		'''首页链接测试：验证地图的链接'''
		self.driver.find_element_by_partial_link_text('sadfyu').click()
		self.driver.back()

if __name__ == '__main__':
    unittest.main(verbosity=2)
