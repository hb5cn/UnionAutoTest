# !/usr/local/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import unittest


class FirstTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def test_normallogin(self):
        """
        用户正常登录
        :return:
        """
        self.login_page.mainlog.info('TestCase-->>用户正常登录')
        # 正常登录boss
        self.login_page.login(self.login_page.operation_login_username())
        # 退出登录boss
        self.login_page.mainlog.info('quit boss')
        self.login_close_boss.quitboss(self.login_page.loginbrowser)

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(FirstTest('testone'))
        return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(FirstTest.suite())
    print(result)
