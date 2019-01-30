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
from method.NonSelfOwnedManage import NonSelfOwnedManage as NonselfMethod


class NonSelfOwnedManage(unittest.TestCase, Method_Nonself):
    def tearDown(self):
        png_floder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                       'ScreenShots', 'screennow')
        png_path = os.path.join(png_floder_path, '%s.png' % self._testMethodName)
        self.NonSelf_page.loginbrowser.get_screenshot_as_file(png_path)
        driver.switch_to.default_content()

    @classmethod
    def setUpClass(cls):
        # 实例化引用的类
        cls.NonSelf_page = LoginPage()
        cls.nonself_method = NonselfMethod()
        cls.NonSelf_page.login(cls.NonSelf_page.number_administrator_login_username())
        # 创建日志句柄
        cls.testloginlog = cls.NonSelf_page.logging.getLogger('NonSelfTestCase')
        cls.testloginlog.addHandler(cls.NonSelf_page.logscr)
        global driver
        driver = cls.NonSelf_page.loginbrowser

    @classmethod
    def tearDownClass(cls):
        cls().testloginlog.info('close browser now')
        cls().NonSelf_page.loginbrowser.switch_to.default_content()
        # 关闭浏览器
        CloseBrowser.quitandclose(cls().NonSelf_page.loginbrowser, cls().NonSelf_page.topbarstatus,
                                  cls().NonSelf_page.topbar, cls().NonSelf_page.exitsystem, cls().NonSelf_page.username)
        cls().testloginlog.info('Logout now done')

    def test_normaladdednumber(self):
        self.testloginlog.info('TestCase-->>正常添加号码')
        self.nonself_method.addnum400(driver)

    def test_normalmodificationnumber(self):
        self.testloginlog.info('TestCase-->>正常修改号码')
        # 进入非自属号码管理页面
        self.testloginlog.info('into menu')
        self.entermenu(driver, '400号码管理', '非自属号码管理')
        WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH,
                                                                             self.nonself_method.nonselfiframe)))
        driver.switch_to_frame(driver.find_element_by_xpath(self.nonself_method.nonselfiframe))
        WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH, self.nonself_method.btn_addnum)))

        # 查询已经创建的号码
        modify_number = self.nonself_method.collection2.find_one({"_id": 0}, {"num400": 1})['num400']
        driver.find_element_by_xpath(self.nonself_method.search_business_number).send_keys(modify_number)
        driver.find_element_by_xpath(self.nonself_method.search_search_btn).click()
        WebDriverWait(driver, 3, 0.5).until_not(ec.presence_of_element_located((By.XPATH,
                                                                                self.nonself_method.tab_wait_text)))

        # 进入修改号码页面
        self.rightclicktablecontent(driver, title='业务号码', text=str(modify_number))
        driver.find_element_by_xpath(self.nonself_method.btn_modify).click()

        # 开始修改内容
        self.nonself_method.getnuminfo(1)

        # 选择运营商
        self.testloginlog.info('select operator')
        self.comboboxsetvalue(driver, 'fl', self.nonself_method.operator)

        # 点击提交
        self.testloginlog.info('submit number400')
        driver.find_element_by_xpath(self.nonself_method.frame_submit).click()
        WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH,
                                                                             self.nonself_method.frame_addsuccessfram)))
        driver.find_element_by_xpath(self.nonself_method.frame_addsuccessfram_btn).click()

        # 检查是否修改成功
        driver.find_element_by_xpath(self.nonself_method.search_business_number).clear()
        driver.find_element_by_xpath(self.nonself_method.search_business_number).send_keys(modify_number)
        driver.find_element_by_xpath(self.nonself_method.search_search_btn).click()
        WebDriverWait(driver, 3, 0.5).until_not(ec.presence_of_element_located((By.XPATH,
                                                                                self.nonself_method.tab_wait_text)))
        self.testloginlog.info('Determine whether the number was created successfully')
        modify_result, row, col, xpath = self.istablecontent(driver, title='运营商',
                                                             text=str(self.nonself_method.operator))
        unittest.TestCase().assertEqual(str(modify_result), 'True')
        self.testloginlog.info('Modify number success')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(NonSelfOwnedManage('test_normalmodificationnumber'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
