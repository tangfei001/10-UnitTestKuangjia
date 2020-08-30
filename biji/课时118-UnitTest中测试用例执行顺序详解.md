**课时118-UnitTest中测试用例执行顺序详解**

# 01-需要安装的第三方库 #
unittest
py.test
mock
---------------------------------------
## 02-测试固件 ##
 a.setUp&tearDown     (有多个测试用例就执行几次)
 b.setUpClass&tearDownClass           (执行一次)  
	每一个测试用例执行完毕必须进行初始化 self.driver.back()

03
类:F1(unittest.TestCase):
方法
	setUp(self):
	tearDown(self):
	test_001(self)
主函数
	if __name__ == '__main__':
    unittest.main(verbosity=2)
-------------------------------------------
### 编写的步骤 ###
01:import unittest

02:定义类-固定写法 F1(unittest.TestCase)

03:测试固件 setUp(self) tearDpwn(self) 测试用例(测试用例必须以test开头)若干 test_xxx()

04:主函数
	if __name__ == '__main__':
    unittest.main(verbosity=2) 默认是1括号里面可以不写
----------------------------------------------------
#### 代码演示 ####

import unittest

class F1(unittest.TestCase):
	def setUp(self):
		print('我已经做好了准备')
	def tearDown(self):
		print('已处理')
	def test_001(self):
		print('test')
	def test_002(self):
		print('test')
	def test_003(self):
		print('test')

if __name__ == '__main__':
    unittest.main(verbosity=2)
