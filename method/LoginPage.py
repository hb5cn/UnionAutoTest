# !/usr/local/python
# -*- coding: UTF-8 -*-
from element.LoginPage import LoginPage as ElementLogin
from element.HomePage import HomePage as ElementHome
from method.OpenBrowser import OpenBrowser
from lib.data.LoginData import LoginData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


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

    def login(self):
        """
        正常登录系统。
        :return:
        """
        # 用户名输入内容
        self.loginbrowser.find_element_by_xpath(self.username).send_keys(self.operation_login_username())
        # 密码输入内容
        self.loginbrowser.find_element_by_xpath(self.password).send_keys(self.login_password())
        # 验证码输入内容
        self.loginbrowser.find_element_by_xpath(self.verificationcode).send_keys(self.verification_code())
        # 点击登录
        self.loginbrowser.find_element_by_xpath(self.confirm).click()
        self.loginlog.info('Begin Login Boss')
        # 等待刷新按钮出现
        WebDriverWait(self.loginbrowser, 20, 0.5).until(ec.presence_of_element_located((By.XPATH, self.refresh)))
        # 点击两次刷新按钮
        self.loginbrowser.find_element_by_xpath(self.refresh).click()
        self.loginbrowser.find_element_by_xpath(self.refresh).click()


# if __name__ == '__main__':
#     a = LoginPage()
#     a.login()
