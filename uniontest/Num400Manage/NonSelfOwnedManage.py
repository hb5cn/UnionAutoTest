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
from element.PricingManagementPage import PricingManagementPage


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
        cls.primag_page = PricingManagementPage()
        cls.NonSelf_page.login(cls.NonSelf_page.number_administrator_login_username())
        # 创建日志句柄
        cls.testloginlog = cls.NonSelf_page.logging.getLogger('NonSelfTestCase')
        cls.testloginlog.addHandler(cls.NonSelf_page.logscr)
        global driver
        driver = cls.NonSelf_page.loginbrowser

    @classmethod
    def tearDownClass(cls):
        cls.closeboss = CloseBrowser()
        cls().testloginlog.info('close browser now')
        cls().NonSelf_page.loginbrowser.switch_to.default_content()
        # 关闭浏览器
        cls.closeboss.quitandclose(cls().NonSelf_page.loginbrowser)
        cls().testloginlog.info('Logout now done')

    def test_normaladdednumber(self):
        self.testloginlog.info('TestCase-->>正常添加号码')
        self.nonself_method.addnum400(driver)
        add_number = self.nonself_method.collection2.find_one({"_id": 0}, {"num400": 1})['num400']
        numinfo_collection = self.nonself_method.db['biz_nonselfownedmanage']
        numinfo_collection.update_one({"_id": 0}, {'$set': {"businessnumber": str(add_number)}})

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
        driver.find_element_by_xpath(self.nonself_method.search_business_number).clear()
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

    def test_required(self):
        self.testloginlog.info('TestCase-->>创建号码必填项校验')
        biz_num = self.nonself_method.num400exists()
        self.nonself_method.getnuminfo(0)
        # 进入非自属号码管理页面
        self.testloginlog.info('into menu')
        self.entermenu(driver, '400号码管理', '非自属号码管理')
        WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH,
                                                                             self.nonself_method.nonselfiframe)))
        driver.switch_to_frame(driver.find_element_by_xpath(self.nonself_method.nonselfiframe))
        WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH, self.nonself_method.btn_addnum)))

        # 进入添加号码页面
        self.testloginlog.info('into add number')
        driver.find_element_by_xpath(self.nonself_method.btn_addnum).click()
        WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((
            By.XPATH, self.nonself_method.frame_business_number)))

        # 不输入业务号码
        # 点击提交
        self.testloginlog.info('submit number400')
        driver.find_element_by_xpath(self.nonself_method.frame_submit).click()
        WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, self.nonself_method.frame_msg1)))
        msg_text = driver.find_element_by_xpath(self.nonself_method.frame_msg1).get_attribute('textContent')
        unittest.TestCase().assertEqual(msg_text, '请输入400号码')
        driver.find_element_by_xpath(self.nonself_method.frame_employee_selection_frambutton).click()

        # 输入业务号码
        self.testloginlog.info('input number')
        driver.find_element_by_xpath(self.nonself_method.frame_business_number).send_keys(biz_num)

        # 不输入运营商
        # 点击提交
        self.testloginlog.info('submit number400')
        driver.find_element_by_xpath(self.nonself_method.frame_submit).click()
        WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((
            By.XPATH, self.nonself_method.frame_tips1)))
        msg_text = driver.find_element_by_xpath(self.nonself_method.frame_tips1).get_attribute('textContent')
        unittest.TestCase().assertEqual(msg_text, '该输入项为必输项')

        # 选择运营商
        self.testloginlog.info('select operator')
        self.comboboxsetvalue(driver, 'fl', self.nonself_method.operator)

        # 不输入状态
        # 点击提交
        self.testloginlog.info('submit number400')
        driver.find_element_by_xpath(self.nonself_method.frame_submit).click()
        WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((
            By.XPATH, self.nonself_method.frame_tips1)))
        msg_text = driver.find_element_by_xpath(self.nonself_method.frame_tips1).get_attribute('textContent')
        unittest.TestCase().assertEqual(msg_text, '该输入项为必输项')

        # 选择状态
        self.testloginlog.info('select accounts')
        self.comboboxsetvalue(driver, 'statu', self.nonself_method.state)

        # 号码类别不输入
        # 点击提交
        self.testloginlog.info('submit number400')
        driver.find_element_by_xpath(self.nonself_method.frame_submit).click()
        WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((
            By.XPATH, self.nonself_method.frame_tips1)))
        msg_text = driver.find_element_by_xpath(self.nonself_method.frame_tips1).get_attribute('textContent')
        unittest.TestCase().assertEqual(msg_text, '该输入项为必输项')

        # 选择号码类别
        self.testloginlog.info('select numbercategory')
        self.comboboxsetvalue(driver, 'sort', self.nonself_method.numbercategory)

        # 帐号不输入
        # 点击提交
        self.testloginlog.info('submit number400')
        driver.find_element_by_xpath(self.nonself_method.frame_submit).click()
        WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((
            By.XPATH, self.nonself_method.frame_tips1)))
        msg_text = driver.find_element_by_xpath(self.nonself_method.frame_tips1).get_attribute('textContent')
        unittest.TestCase().assertEqual(msg_text, '该输入项为必输项')

        # 选择帐号
        self.testloginlog.info('select accounts')
        self.comboboxsetvalue(driver, 'zh', self.nonself_method.accounts)

        # 截止日期不输入
        # 点击提交
        self.testloginlog.info('submit number400')
        driver.find_element_by_xpath(self.nonself_method.frame_submit).click()
        WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((
            By.XPATH, self.nonself_method.frame_tips1)))
        msg_text = driver.find_element_by_xpath(self.nonself_method.frame_tips1).get_attribute('textContent')
        unittest.TestCase().assertEqual(msg_text, '该输入项为必输项')

        # 选择截止日期
        self.testloginlog.info('select closingdate')
        self.setdata(driver, 'jzrq', self.nonself_method.closingdate)

        # 点击提交
        self.testloginlog.info('submit number400')
        driver.find_element_by_xpath(self.nonself_method.frame_submit).click()
        WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((
            By.XPATH, self.nonself_method.frame_addsuccessfram)))
        driver.find_element_by_xpath(self.nonself_method.frame_addsuccessfram_btn).click()

        numinfo_collection = self.nonself_method.db['biz_nonselfownedmanage']
        numinfo_collection.update_one({"_id": 1}, {'$set': {"businessnumber": str(biz_num)}})

    def test_validationofpricing(self):
        self.testloginlog.info('TestCase-->>创建完号码在号码定价管理页面有记录')
        search_number = self.nonself_method.collection2.find_one({"_id": 0}, {"num400": 1})['num400']
        # 进入定价管理页面
        self.testloginlog.info('into menu')
        self.entermenu(driver, '400号码管理', '号码定价管理')
        WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH,
                                                                             self.primag_page.primagframe)))
        driver.switch_to_frame(driver.find_element_by_xpath(self.primag_page.primagframe))
        WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((
            By.XPATH, self.primag_page.search_number)))

        # 查询已经创建完成的号码
        self.testloginlog.info('search number')
        WebDriverWait(driver, 20, 0.5).until_not(ec.presence_of_element_located((
            By.XPATH, self.primag_page.tab_wait_text)))
        driver.find_element_by_xpath(self.primag_page.search_number).send_keys(search_number)
        driver.find_element_by_xpath(self.primag_page.search_btn).click()
        WebDriverWait(driver, 20, 0.5).until_not(ec.presence_of_element_located((
            By.XPATH, self.primag_page.tab_wait_text)))

        # 判断是否在列表中有该号码
        self.testloginlog.info('judge number is in table')
        modify_result, row, col, xpath = self.istablecontent(driver, title='400号码', text=str(search_number))
        unittest.TestCase().assertEqual(str(modify_result), 'True')

    def test_rightoperationopenandopening(self):
        self.testloginlog.info('TestCase-->>已开户及开户流程中号码不可进行修改、释放、促销操作')
        # 获取当前登录用户
        nowloginuser = self.get_loginusername(driver)
        numinfo_collection = self.nonself_method.db['biz_nonselfownedmanage']
        numinfo_collection.update_one({"_id": 2}, {'$set': {"preoccupiedperson": str(nowloginuser)}})
        numinfo_collection.update_one({"_id": 2}, {'$set': {"reservations": str(nowloginuser)}})
        numinfo_collection.update_one({"_id": 3}, {'$set': {"preoccupiedperson": str(nowloginuser)}})
        numinfo_collection.update_one({"_id": 3}, {'$set': {"reservations": str(nowloginuser)}})

        # 创建已开户的号码
        self.testloginlog.info('Create Open account number')
        self.nonself_method.addnum400(driver, 2)

        # 查询已开户号码
        self.testloginlog.info('search Open account number')
        add_number = self.nonself_method.collection2.find_one({"_id": 0}, {"num400": 1})['num400']
        driver.find_element_by_xpath(self.nonself_method.search_business_number).clear()
        driver.find_element_by_xpath(self.nonself_method.search_business_number).send_keys(add_number)
        driver.find_element_by_xpath(self.nonself_method.search_search_btn).click()
        self.testloginlog.info('right click Open account number')
        self.rightclicktablecontent(driver, title='业务号码', text=str(add_number))
        rightbutton_js = 'return $(\'#saff_mmData\').css(\'display\')'
        status = driver.execute_script(rightbutton_js)
        unittest.TestCase().assertEqual(str(status).lower(), 'none')

        # 创建开户流程中的号码
        driver.switch_to.default_content()
        self.testloginlog.info('Create Account opening process number')
        self.nonself_method.addnum400(driver, 3)

        # 查询已开户号码
        self.testloginlog.info('search Account opening process number')
        add_number = self.nonself_method.collection2.find_one({"_id": 0}, {"num400": 1})['num400']
        driver.find_element_by_xpath(self.nonself_method.search_business_number).clear()
        driver.find_element_by_xpath(self.nonself_method.search_business_number).send_keys(add_number)
        driver.find_element_by_xpath(self.nonself_method.search_search_btn).click()
        self.testloginlog.info('right click Account opening process number')
        self.rightclicktablecontent(driver, title='业务号码', text=str(add_number))
        rightbutton_js = 'return $(\'#saff_mmData\').css(\'display\')'
        status = driver.execute_script(rightbutton_js)
        unittest.TestCase().assertEqual(str(status).lower(), 'none')

    def test_releasenumber(self):
        self.testloginlog.info('TestCase-->>对号码进行释放操作')
        # 进入非自属号码管理页面
        self.testloginlog.info('into menu')
        self.entermenu(driver, '400号码管理', '非自属号码管理')
        WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH,
                                                                             self.nonself_method.nonselfiframe)))
        driver.switch_to_frame(driver.find_element_by_xpath(self.nonself_method.nonselfiframe))
        WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH, self.nonself_method.btn_addnum)))

        # 查询已经创建的号码
        self.testloginlog.info('search number')
        numinfo_collection = self.nonself_method.db['biz_nonselfownedmanage']
        release_number = numinfo_collection.find_one({"_id": 1}, {'businessnumber': 1})['businessnumber']
        driver.find_element_by_xpath(self.nonself_method.search_business_number).clear()
        driver.find_element_by_xpath(self.nonself_method.search_business_number).send_keys(release_number)
        driver.find_element_by_xpath(self.nonself_method.search_search_btn).click()
        WebDriverWait(driver, 3, 0.5).until_not(ec.presence_of_element_located((By.XPATH,
                                                                                self.nonself_method.tab_wait_text)))

        # 对号码进行释放
        self.testloginlog.info('release number')
        self.rightclicktablecontent(driver, title='业务号码', text=str(release_number))
        driver.find_element_by_xpath(self.nonself_method.release_btn).click()
        WebDriverWait(driver, 3, 0.5).until(ec.presence_of_element_located((By.XPATH,
                                                                            self.nonself_method.msg_release)))
        driver.find_element_by_xpath(self.nonself_method.msg_release_btn).click()
        WebDriverWait(driver, 3, 0.5).until(ec.presence_of_element_located((By.XPATH,
                                                                            self.nonself_method.msg_release2)))
        driver.find_element_by_xpath(self.nonself_method.msg_release2_btn).click()

        # 查询是否已经释放
        self.testloginlog.info('seach release number sccess')
        driver.find_element_by_xpath(self.nonself_method.search_business_number).clear()
        driver.find_element_by_xpath(self.nonself_method.search_business_number).send_keys(release_number)
        driver.find_element_by_xpath(self.nonself_method.search_search_btn).click()
        WebDriverWait(driver, 3, 0.5).until_not(ec.presence_of_element_located((By.XPATH,
                                                                                self.nonself_method.tab_wait_text)))
        self.istablecontent(driver, title='状态', text='释放')

        # 对已释放的号码进行释放
        self.rightclicktablecontent(driver, title='业务号码', text=str(release_number))
        driver.find_element_by_xpath(self.nonself_method.release_btn).click()
        WebDriverWait(driver, 3, 0.5).until(ec.presence_of_element_located((By.XPATH,
                                                                            self.nonself_method.msg_release)))
        driver.find_element_by_xpath(self.nonself_method.msg_release_btn).click()
        WebDriverWait(driver, 3, 0.5).until(ec.presence_of_element_located((By.XPATH,
                                                                            self.nonself_method.msg_release3)))
        driver.find_element_by_xpath(self.nonself_method.msg_release3_btn).click()

    def test_promotionnumber(self):
        self.testloginlog.info('TestCase-->>对号码进行释放操作')
        # 进入非自属号码管理页面
        self.testloginlog.info('into menu')
        self.entermenu(driver, '400号码管理', '非自属号码管理')
        WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH,
                                                                             self.nonself_method.nonselfiframe)))
        driver.switch_to_frame(driver.find_element_by_xpath(self.nonself_method.nonselfiframe))
        WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH, self.nonself_method.btn_addnum)))

        # 查询已经创建的号码
        self.testloginlog.info('search number')
        numinfo_collection = self.nonself_method.db['biz_nonselfownedmanage']
        promotion_number = numinfo_collection.find_one({"_id": 1}, {'businessnumber': 1})['businessnumber']
        driver.find_element_by_xpath(self.nonself_method.search_business_number).clear()
        driver.find_element_by_xpath(self.nonself_method.search_business_number).send_keys(promotion_number)
        driver.find_element_by_xpath(self.nonself_method.search_search_btn).click()
        WebDriverWait(driver, 3, 0.5).until_not(ec.presence_of_element_located((By.XPATH,
                                                                                self.nonself_method.tab_wait_text)))

        # 对号码进行促销
        self.testloginlog.info('promotion number')
        self.rightclicktablecontent(driver, title='业务号码', text=str(promotion_number))
        driver.find_element_by_xpath(self.nonself_method.promotion_btn).click()
        WebDriverWait(driver, 3, 0.5).until(ec.presence_of_element_located((By.XPATH,
                                                                            self.nonself_method.msg_promotion)))
        driver.find_element_by_xpath(self.nonself_method.msg_promotion_btn).click()
        WebDriverWait(driver, 3, 0.5).until(ec.presence_of_element_located((By.XPATH,
                                                                            self.nonself_method.msg_promotion2)))
        driver.find_element_by_xpath(self.nonself_method.msg_promotion2_btn).click()

        # 查询是否已成功促销
        self.testloginlog.info('seach promotion number sccess')
        driver.find_element_by_xpath(self.nonself_method.search_business_number).clear()
        driver.find_element_by_xpath(self.nonself_method.search_business_number).send_keys(promotion_number)
        driver.find_element_by_xpath(self.nonself_method.search_search_btn).click()
        WebDriverWait(driver, 3, 0.5).until_not(ec.presence_of_element_located((By.XPATH,
                                                                                self.nonself_method.tab_wait_text)))
        self.istablecontent(driver, title='是否促销', text='是')

        # 对已经促销的号码进行促销
        self.testloginlog.info('promotion number')
        self.rightclicktablecontent(driver, title='业务号码', text=str(promotion_number))
        driver.find_element_by_xpath(self.nonself_method.promotion_btn).click()
        WebDriverWait(driver, 3, 0.5).until(ec.presence_of_element_located((By.XPATH,
                                                                            self.nonself_method.msg_promotion3)))
        driver.find_element_by_xpath(self.nonself_method.msg_promotion3_btn).click()
        WebDriverWait(driver, 3, 0.5).until(ec.presence_of_element_located((By.XPATH,
                                                                            self.nonself_method.msg_promotion2)))
        driver.find_element_by_xpath(self.nonself_method.msg_promotion2_btn).click()

        # 查询是否已成功促销
        self.testloginlog.info('seach promotion number sccess')
        driver.find_element_by_xpath(self.nonself_method.search_business_number).clear()
        driver.find_element_by_xpath(self.nonself_method.search_business_number).send_keys(promotion_number)
        driver.find_element_by_xpath(self.nonself_method.search_search_btn).click()
        WebDriverWait(driver, 3, 0.5).until_not(ec.presence_of_element_located((By.XPATH,
                                                                                self.nonself_method.tab_wait_text)))
        self.istablecontent(driver, title='是否促销', text='否')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(NonSelfOwnedManage('test_promotionnumber'))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
