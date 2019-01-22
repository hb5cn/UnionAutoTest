# !/usr/local/python
# -*- coding: UTF-8 -*-
import unittest
from method.LoginPage import LoginPage
from method.CloseBrowser import CloseBrowser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


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
        CloseBrowser.quitandclose(cls().login_page.loginbrowser, cls().login_page.topbarstatus, cls().login_page.topbar,
                                  cls().login_page.exitsystem, cls().login_page.username)
        cls().testloginlog.info('Logout now done')

    def test_normallogin(self):
        # 正常登录boss
        self.login_page.login()
        # 退出登录boss
        CloseBrowser.quitboss(self.login_page.loginbrowser, self.login_page.topbarstatus, self.login_page.topbar,
                              self.login_page.exitsystem, self.login_page.username)

    def test_enterlogin(self):
        # 用户名输入内容
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.username).send_keys(
            self.login_page.operation_login_username())
        # 密码输入内容
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.password).send_keys(
            self.login_page.login_password())
        # 验证码输入内容
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.verificationcode).send_keys(
            self.login_page.verification_code())
        # 点击登录
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.confirm).click()
        self.login_page.loginlog.info('Begin Login Boss')
        # 等待刷新按钮出现
        WebDriverWait(self.login_page.loginbrowser, 20, 0.5).until(ec.presence_of_element_located(
            (By.XPATH, self.login_page.refresh)))
        # 退出登录boss
        # CloseBrowser.quitboss(self.login_page.loginbrowser, self.login_page.topbarstatus, self.login_page.topbar,
        #                       self.login_page.exitsystem, self.login_page.username)


# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(TestLoginPage('test_normallogin'))
#     runner = unittest.TextTestRunner()
#     result = runner.run(suite)
#     print(result)
    # a = TestLoginPage()
    # a.test_normallogin()
    # a.tearownclass()
