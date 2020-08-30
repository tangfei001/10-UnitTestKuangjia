#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 12:10
# @Author  : Aries
# @Site    : 
# @File    : gujian.py
# @Software: PyCharm
'''
分离测试固件
'''
import unittest

class GuJian(unittest.TestCase):
	def setUp(self) -> None:
		print('开始执行')
	def tearDown(self) -> None:
		print('结束执行')