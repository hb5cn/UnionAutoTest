# !/usr/local/python
# -*- coding: UTF-8 -*-
import unittest
from method.LoginPage import LoginPage
from method.CloseBrowser import CloseBrowser


class TestLoginPage(unittest.TestCase, LoginPage, CloseBrowser):
    def __init__(self, methodname=''):
        unittest.TestCase.__init__(self, methodname)
        LoginPage.__init__(self)
        CloseBrowser.__init__(self)
        self.testloginlog = self.logging.getLogger('TestLoginBoss')
        self.testloginlog.addHandler(self.logscr)

    def instantiation(self):
        pass

    @classmethod
    def tearDownClass(cls):
        teardown = cls('instantiation')
        teardown.testloginlog.info('Logout now')
        teardown.quitboss(teardown.loginbrowser, teardown.topbarstatus, teardown.exitsystem, teardown.topbar,
                          teardown.username)
        teardown.testloginlog.info('Logout now done')

    def test_normallogin(self):
        self.login()

    def test_normallogin2(self):
        self.login()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLoginPage('test_normallogin'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    print(result)
    # a = TestLoginPage()
    # a.test_normallogin()
    # a.tearownclass()
