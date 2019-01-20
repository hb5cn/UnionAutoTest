# !/usr/local/python
# -*- coding: UTF-8 -*-
import unittest
from method.LoginPage import LoginPage
from method.CloseBrowser import CloseBrowser


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.a = LoginPage()
        cls.testloginlog = cls.a.logging.getLogger('TestLoginBoss')
        cls.testloginlog.addHandler(cls.a.logscr)

    @classmethod
    def tearDownClass(cls):
        cls().testloginlog.info('Logout now')
        CloseBrowser.quitboss(cls().a.loginbrowser, cls().a.topbarstatus, cls().a.topbar, cls().a.exitsystem,
                              cls().a.username)
        cls().testloginlog.info('Logout now done')

    def test_normallogin(self):
        self.a.login()


# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(TestLoginPage('test_normallogin'))
#     runner = unittest.TextTestRunner()
#     result = runner.run(suite)
#     print(result)
    # a = TestLoginPage()
    # a.test_normallogin()
    # a.tearownclass()
