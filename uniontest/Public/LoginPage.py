# !/usr/local/python
# -*- coding: UTF-8 -*-
import unittest
from method.LoginPage import LoginPage
from method.CloseBrowser import CloseBrowser


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 实例化引用的类
        cls.login_page = LoginPage()
        # 创建日志句柄
        cls.testloginlog = cls.login_page.logging.getLogger('TestLoginBoss')
        cls.testloginlog.addHandler(cls.login_page.logscr)

    @classmethod
    def tearDownClass(cls):
        cls().testloginlog.info('Logout now')
        # 正常退出boss
        CloseBrowser.quitboss(cls().login_page.loginbrowser, cls().login_page.topbarstatus, cls().login_page.topbar,
                              cls().login_page.exitsystem, cls().login_page.username)
        cls().testloginlog.info('Logout now done')

    def test_normallogin(self):
        # 正常登录boss
        self.login_page.login()


# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(TestLoginPage('test_normallogin'))
#     runner = unittest.TextTestRunner()
#     result = runner.run(suite)
#     print(result)
    # a = TestLoginPage()
    # a.test_normallogin()
    # a.tearownclass()
