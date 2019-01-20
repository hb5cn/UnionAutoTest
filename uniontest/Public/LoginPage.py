# !/usr/local/python
# -*- coding: UTF-8 -*-
import unittest
from method.LoginPage import LoginPage
from method.CloseBrowser import CloseBrowser


class TestLoginPage(unittest.TestCase, LoginPage, CloseBrowser):
    # testloginlog = LoginPage().logging.getLogger('TestLoginBoss')
    # testloginlog.addHandler(LoginPage().logscr)
    # @classmethod
    def __init__(self, methodname):
        unittest.TestCase.__init__(self, methodname)
        LoginPage.__init__(self)
        CloseBrowser.__init__(self)
        self.testloginlog = self.logging.getLogger('TestLoginBoss')
        self.testloginlog.addHandler(self.logscr)

    def tearDownClass(self):
        self.testloginlog.info('Logout now')
        self.quitboss(self.loginbrowser, self.topbarstatus, self.exitsystem,
                                self.topbar, self.username)
        self.testloginlog.info('Logout now done')

    def test_normallogin(self):
        self.login()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLoginPage('test_normallogin'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    # print(result)
