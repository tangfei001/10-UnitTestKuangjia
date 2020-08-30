拓展-生成HTML测试报告

#第一步
import unittest
import os
import HTMLTestRunner
import time

#批量执行测试用例代码-原本就有的
def allTest():
	suite=unittest.TestLoader().discover(start_dir=os.path.dirname(__file__),
	                                     pattern='test_*.py',
	                                     top_level_dir=None)
#定义一个函数-获取当前时间时间
def getNowTime():
	return time.strftime('%y-%m-%d %H_%M_%S',time.localtime(time.time()))

#改造run函数
def run():
	'''
	01:变量fp=
	01:定义一个变量,变量名叫fp
	02:使用os模块的目录拼接和获取目录函数 os.path.dirname(__file__),'report'
	03:创建'testReport.html'文件
	04:把时间戳函数加到fp当中去
    ----------------------------------------------------------------------------
    02:HTMLTestRunner.HTMLTestRunner().run()
	01:stream=open(fp,'wb') 写入文件使用open()吧fp写进去
	02: title='自动化测试报告'  报告的主题
	03:description='自动化测试报告详细信息   报告的描述-可以为空
 
	'''
	fp=os.path.join(os.path.dirname(__file__),'report',getNowTime()+'testReport.html')
	HTMLTestRunner.HTMLTestRunner(stream=open(fp,'wb'),
	                              title='自动化测试报告',
	                              description='').run(allTest())
#主函数中执行run()函数
if __name__ == '__main__':
    run()