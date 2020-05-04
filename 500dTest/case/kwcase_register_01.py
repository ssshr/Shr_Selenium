import ddt
import unittest
import HTMLTestRunner
import os
from keyword_mode.kw_excel_handle import KeyWordCase
from tools.excel_tool import ExcelTool
from log.uesr_log import UserLog

# ex = ExcelTool()
# data = ex.get_data()

class TestCaseKw(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.kw = KeyWordCase()
        print("所有case前置")
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        print("所有case后置")


    def setUp(self):
        # webdriver.Chrome()
        print('单条前置')
    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)

        # self.driver.close()

    def test_001_kw(self):
        self.kw.run_main(os.getcwd()+'/config/test_001_kw.xls')
        self.logger.info('Test with wrong username')
    def test_002_kw(self):
        self.kw.run_main(os.getcwd()+'/config/test_002_kw.xls')
        self.logger.info('Test with wrong email')

if __name__ == '__main__':
    # unittest.main()
    # 在目标路径生成测试报告
    file_path = os.path.join(os.getcwd() + "/report/" + "report_kwcase_register_01.html")
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCaseKw)
    runner = HTMLTestRunner.HTMLTestRunner(f, title="测试报告", description="Testing Report===>kwcase_register_01", verbosity=2)
    runner.run(suite)