**课时120-UnitTest中测试固件的详解**

setUpClass&tearDownClass
----------------------------------------------

步骤 

01:导入包

02:类  F2(unittest.TestCase)

03:测试固件(使用类方法-第二种用法) --类方法
	@classmethod
	setUpClass(cls):
		xxxxxx
    @classmethod
	tearDownClass(cls)
		xxxxxx
	#测试用例
	test_xxx(self)
		xxxxx
04:主函数	
	
if __name__ == '__main__':
    unittest.main(verbosity=2)

------------------------------------------
import  unittest
from selenium import  webdriver

class F2(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)
		cls.driver.get('http://www.baidu.com')

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def test_baidu_news(self):
		self.driver.find_element_by_link_text('新闻').click()
		self.driver.back()

	def test_baidu_map(self):
		self.driver.find_element_by_partial_link_text('图').click()
		self.driver.back()

	def test_baidu_mbq(self):
		self.driver.find_element_by_partial_link_text('地图').click()
		self.driver.back()

if __name__ == '__main__':
    unittest.main(verbosity=2)