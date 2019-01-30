# !/usr/local/python
# -*- coding: UTF-8 -*-
import time
from element.LoginPage import LoginPage as ElementLogin
from element.HomePage import HomePage as ElementHome
from method.OpenBrowser import OpenBrowser
from lib.data.LoginData import LoginData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage(OpenBrowser, ElementLogin, ElementHome, LoginData):
    def __init__(self):
        OpenBrowser.__init__(self)
        LoginData.__init__(self)
        ElementLogin.__init__(self)
        ElementHome.__init__(self)
        self.loginbrowser = self.browser
        # 登录网站并且最大化
        self.loginbrowser.get(LoginData.bossurl(self))
        self.loginbrowser.maximize_window()
        # 获取日志句柄
        self.loginlog = self.logging.getLogger('LoginBoss')
        self.loginlog.addHandler(self.logscr)

    def login(self, username):
        """
        正常登录系统。
        :return:
        """
        # 用户名输入内容
        self.loginlog.info('Login username is :    %s' % username)
        self.loginbrowser.find_element_by_xpath(self.username).send_keys(username)
        # 密码输入内容
        self.loginlog.info('Login password is :    %s' % self.login_password())
        self.loginbrowser.find_element_by_xpath(self.password).send_keys(self.login_password())
        # 验证码输入内容
        self.loginlog.info('Login verificationcode is :    %s' % self.verification_code())
        self.loginbrowser.find_element_by_xpath(self.verificationcode).send_keys(self.verification_code())
        # 点击登录
        self.loginlog.info('cilck login button')
        self.loginbrowser.find_element_by_xpath(self.confirm).click()
        try:
            self.loginbrowser.find_element_by_xpath(self.msgframe3)
            self.loginbrowser.find_element_by_xpath(self.msgframe3button).click()
            self.loginbrowser.find_element_by_xpath(self.msgframe4)
            self.loginbrowser.find_element_by_xpath(self.msgframe4button).click()
            self.loginlog.info('Duplicate logon')
            time.sleep(2)
            self.loginbrowser.find_element_by_xpath(self.confirm).click()
        except NoSuchElementException:
            pass

        try:
            self.loginbrowser.find_element_by_xpath(self.msgframe5)
            self.loginbrowser.find_element_by_xpath(self.msgframe5button).click()
            self.loginlog.info('Frequent login')
            time.sleep(2)
            self.loginbrowser.find_element_by_xpath(self.confirm).click()
        except NoSuchElementException:
            pass

        self.loginlog.info('Begin Login Boss')
        # 等待刷新按钮出现
        WebDriverWait(self.loginbrowser, 60, 0.5).until(ec.presence_of_element_located((By.XPATH, self.refresh)))
        # 点击两次刷新按钮
        self.loginbrowser.find_element_by_xpath(self.refresh).click()
        self.loginbrowser.find_element_by_xpath(self.refresh).click()
        # 点击上方状态栏，让其收起来
        WebDriverWait(self.loginbrowser, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, self.topbar_up)))
        self.loginbrowser.find_element_by_xpath(self.topbar_up).click()
        while True:
            px = self.loginbrowser.execute_script('return $(\'#topDiv\').parent().css(\'top\')')
            if '-100px' == px:
                break
            else:
                time.sleep(0.5)


# if __name__ == '__main__':
#     a = LoginPage()
#     a.login()
