import sys
sys.path.append(r'D:\bsssss\500dTest')
import unittest
import os
import HTMLTestRunner


class RunCase(unittest.TestCase):
    def test_case01(self):
        case_path = os.path.join(os.getcwd()+"/case/")
        suite = unittest.defaultTestLoader.discover(case_path,'case_*.py')
        unittest.TextTestRunner().run(suite)

    # def test_case02(self):
    #     case_path = os.path.join(os.getcwd()+"/case/")
    #     suite = unittest.defaultTestLoader.discover(case_path,'kw_case_*.py')
    #     unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()
    # file_path = os.path.join(os.path.abspath('..') + "\\report\\" + "report01.html")
    # f = open(file_path,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(f,title="测试报告",description="Testing Report",verbosity=5).run()
