# !/usr/local/python
# -*- coding: UTF-8 -*-
import os
import unittest
from method.LoginPage import LoginPage
from method.CloseBrowser import CloseBrowser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestLoginPage(unittest.TestCase):
    def tearDown(self):
        png_floder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                       'ScreenShots', 'screennow')
        png_path = os.path.join(png_floder_path, '%s.png' % self._testMethodName)
        self.login_page.loginbrowser.get_screenshot_as_file(png_path)

    @classmethod
    def setUpClass(cls):
        # 实例化引用的类
        cls.login_page = LoginPage()
        # 创建日志句柄
        cls.testloginlog = cls.login_page.logging.getLogger('LoginBoss')
        cls.testloginlog.addHandler(cls.login_page.logscr)
        global driver
        driver = cls.login_page.loginbrowser

    @classmethod
    def tearDownClass(cls):
        cls().testloginlog.info('close browser now')
        # 关闭浏览器
        cls().login_page.loginbrowser.quit()

    def test_normallogin(self):
        """
        用户正常登录
        :return:
        """
        self.testloginlog.info('TestCase-->>用户正常登录')
        # 正常登录boss
        self.login_page.login(self.login_page.operation_login_username())
        # 退出登录boss
        CloseBrowser.quitboss(self.login_page.loginbrowser, self.login_page.topbarstatus, self.login_page.topbar,
                              self.login_page.exitsystem, self.login_page.username)

    def test_enterlogin(self):
        """
        用户按回车键正常登录
        :return:
        """
        self.testloginlog.info('TestCase-->>用户按回车键正常登录')
        # 用户名输入内容
        self.testloginlog.info('Input username')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.username).send_keys(
            self.login_page.operation_login_username())
        # 密码输入内容
        self.testloginlog.info('Input password')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.password).send_keys(
            self.login_page.login_password())
        # 验证码输入内容
        self.testloginlog.info('Input verification')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.verificationcode).send_keys(
            self.login_page.verification_code())
        # 按回车登录
        self.testloginlog.info('put enter')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.verificationcode).send_keys(Keys.ENTER)
        self.login_page.loginlog.info('Begin Login Boss')
        # 等待刷新按钮出现
        WebDriverWait(self.login_page.loginbrowser, 60, 0.5).until(ec.presence_of_element_located(
            (By.XPATH, self.login_page.refresh)))
        # 退出登录boss
        self.testloginlog.info('quit boss')
        CloseBrowser.quitboss(self.login_page.loginbrowser, self.login_page.topbarstatus, self.login_page.topbar,
                              self.login_page.exitsystem, self.login_page.username)

    def test_reset(self):
        """
        登录页面重置按钮正常清除
        :return:
        """
        # 用户名输入内容
        self.testloginlog.info('TestCase-->>登录页面重置按钮正常清除')
        self.testloginlog.info('Input username')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.username).send_keys(
            self.login_page.operation_login_username())
        # 密码输入内容
        self.testloginlog.info('Input password')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.password).send_keys(
            self.login_page.login_password())
        # 验证码输入内容
        self.testloginlog.info('Input verification')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.verificationcode).send_keys(
            self.login_page.verification_code())
        # 点击重置按钮
        self.testloginlog.info('Click reset')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.reset).click()
        username_text = self.login_page.loginbrowser.find_element_by_xpath(self.login_page.username).text
        unittest.TestCase.assertEqual(self, username_text, "")

    def test_verificationcode_picture(self):
        """
        登录页面验证码点击后正常更换图片
        :return:
        """
        self.testloginlog.info('TestCase-->>登录页面验证码点击后正常更换图片')
        # 获取旧的验证码链接地址
        self.testloginlog.info('get old img src')
        old_src = self.login_page.loginbrowser.find_element_by_xpath(self.login_page.verificationcodepicture
                                                                     ).get_attribute('src')
        self.testloginlog.info('click img')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.verificationcodepicture).click()
        # 获取新的验证码链接地址
        self.testloginlog.info('get new img src')
        new_src = self.login_page.loginbrowser.find_element_by_xpath(self.login_page.verificationcodepicture
                                                                     ).get_attribute('src')
        # 判断两个地址不相同
        unittest.TestCase.assertNotEqual(self, old_src, new_src)

    def test_nonexistentuser(self):
        """
        不存在的用户名无法登录
        :return:
        """
        self.testloginlog.info('TestCase-->>不存在的用户名无法登录')
        # 用户名输入内容
        self.testloginlog.info('Input not exist username')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.username).send_keys('Nonexistent')
        # 密码输入内容
        self.testloginlog.info('Input password')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.password).send_keys(
            self.login_page.login_password())
        # 验证码输入内容
        self.testloginlog.info('Input verification')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.verificationcode).send_keys(
            self.login_page.verification_code())
        # 点击登录
        self.testloginlog.info('Click login button')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.confirm).click()
        # 获取弹框的内容
        self.testloginlog.info('Get message frame content')
        msg = self.login_page.loginbrowser.find_element_by_xpath(self.login_page.msgframe).text
        unittest.TestCase.assertEqual(self, msg, '用户名或密码错误，请重新输入。')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.msgframebutton).click()
        # 清除输入框内容
        self.testloginlog.info('Clear input content')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.username).clear()
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.password).clear()
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.verificationcode).clear()

    def test_wrongpassword(self):
        """
        错误的密码无法登录
        :return:
        """
        self.testloginlog.info('TestCase-->>错误的密码无法登录')
        # 用户名输入内容
        self.testloginlog.info('Input username')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.username).send_keys(
            self.login_page.operation_login_username())
        # 密码输入内容
        self.testloginlog.info('Input wrong username')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.password).send_keys('Nonexistent')
        # 验证码输入内容
        self.testloginlog.info('Input verification')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.verificationcode).send_keys(
            self.login_page.verification_code())
        # 点击登录
        self.testloginlog.info('Click login button')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.confirm).click()
        # 获取弹框的内容
        self.testloginlog.info('Get message frame content')
        msg = self.login_page.loginbrowser.find_element_by_xpath(self.login_page.msgframe2).text
        unittest.TestCase.assertEqual(self, msg, '密码不正确')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.msgframebutton).click()
        # 清除输入框内容
        self.testloginlog.info('Clear input content')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.username).clear()
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.password).clear()
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.verificationcode).clear()

    def test_required(self):
        """
        必填项验证
        :return:
        """
        self.testloginlog.info('TestCase-->>必填项验证')
        # 用户名不输入
        # 密码输入内容
        self.testloginlog.info('Input password')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.password).send_keys(
            self.login_page.login_password())
        # 验证码输入内容
        self.testloginlog.info('Input verification')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.verificationcode).send_keys(
            self.login_page.verification_code())
        # 点击登录
        self.testloginlog.info('Click login button')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.confirm).click()
        # 获取弹框的内容
        self.testloginlog.info('Get message frame content')
        tips = self.login_page.loginbrowser.find_element_by_xpath(self.login_page.tips).text
        unittest.TestCase.assertEqual(self, tips, '该输入项为必输项')

        # 密码不输入
        # 用户名输入内容
        self.testloginlog.info('Input username')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.username).send_keys(
            self.login_page.operation_login_username())
        # 密码清空
        self.testloginlog.info('Clear password')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.password).clear()
        # 点击登录
        self.testloginlog.info('Click login button')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.confirm).click()
        # 获取弹框的内容
        self.testloginlog.info('Get message frame content')
        tips = self.login_page.loginbrowser.find_element_by_xpath(self.login_page.tips).text
        unittest.TestCase.assertEqual(self, tips, '该输入项为必输项')

        # 验证码不输入
        # 密码输入内容
        self.testloginlog.info('Input password')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.password).send_keys(
            self.login_page.login_password())
        # 验证码清空
        self.testloginlog.info('Input verification')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.verificationcode).clear()
        # 点击登录
        self.testloginlog.info('Click login button')
        self.login_page.loginbrowser.find_element_by_xpath(self.login_page.confirm).click()
        # 获取弹框的内容
        self.testloginlog.info('Get message frame content')
        tips = self.login_page.loginbrowser.find_element_by_xpath(self.login_page.tips).text
        unittest.TestCase.assertEqual(self, tips, '该输入项为必输项')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLoginPage('test_required'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
