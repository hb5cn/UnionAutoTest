# !/usr/local/python
# -*- coding: UTF-8 -*-
import os
import unittest
from method.LoginPage import LoginPage
from method.CloseBrowser import CloseBrowser
from method.NonSelfOwnedManage import NonSelfOwnedManage as Method_Nonself
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NonSelfOwnedManage(unittest.TestCase, Method_Nonself):
    def tearDown(self):
        png_floder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                       'ScreenShots', 'screennow')
        png_path = os.path.join(png_floder_path, '%s.png' % self._testMethodName)
        self.NonSelf_page.loginbrowser.get_screenshot_as_file(png_path)

    @classmethod
    def setUpClass(cls):
        # 实例化引用的类
        cls.NonSelf_page = LoginPage()
        cls.NonSelf_page.login(cls.NonSelf_page.number_administrator_login_username())
        # 创建日志句柄
        cls.testloginlog = cls.NonSelf_page.logging.getLogger('LoginBoss')
        cls.testloginlog.addHandler(cls.NonSelf_page.logscr)
        global driver
        driver = cls.NonSelf_page.loginbrowser

    @classmethod
    def tearDownClass(cls):
        cls().testloginlog.info('close browser now')
        # 关闭浏览器
        CloseBrowser.quitandclose(cls().NonSelf_page.loginbrowser, cls().NonSelf_page.topbarstatus,
                                  cls().NonSelf_page.topbar, cls().NonSelf_page.exitsystem, cls().NonSelf_page.username)
        cls().testloginlog.info('Logout now done')
        # cls().NonSelf_page.loginbrowser.quit()

    def normaladdednumber(self):
        Method_Nonself().addnum400(self.NonSelf_page.loginbrowser)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(NonSelfOwnedManage('normaladdednumber'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
