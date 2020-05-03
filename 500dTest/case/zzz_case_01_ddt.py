import sys
sys.path.append(r'D:\bsssss\500dTest')
import time
import ddt
import unittest
import HTMLTestRunner
import os
from selenium import webdriver
from business.register_business import RegisterBusiness
from tools.excel_tool import ExcelTool
from log.uesr_log import UserLog



ex = ExcelTool()
data = ex.get_data()

@ddt.ddt
class FirstCaseDdt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        print("执行case_01")
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        print("所有case后置")


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.showapi.com/auth/reg")
        self.logger.info('open url')
        self.login = RegisterBusiness(self.driver)
    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)

        self.driver.close()


    #用户名，邮箱，密码，验证码，定位信息，提示信息
    # @ddt.data(
    #     ['name001', 'email','password','file_name','user_email_error','请输入正确的邮箱账号'],
    # )
    #
    # @ddt.unpack

    @ddt.data(*data)
    def test_01_ddt(self,data):
        name, email, password, code, assertCode, assertText = data
        email_error = self.login.register_function(name,email,password,code,assertCode,assertText)
        self.assertFalse(email_error)


if __name__ == '__main__':
    # unittest.main()

    # 在目标路径生成测试报告
    file_path = os.path.join(os.getcwd() + "/report/" + "report001.html")
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstCaseDdt)
    runner = HTMLTestRunner.HTMLTestRunner(f, title="测试报告", description="Testing Report 001 With Excel", verbosity=2)
    runner.run(suite)