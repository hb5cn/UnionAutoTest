# !/usr/local/python
# -*- coding: UTF-8 -*-
import time
from element.NonSelfOwnedManagePage import NonSelfOwnedManagePage
from lib.data.BusinessData import BusinessData
from method.PublicMethod import PublicMethod
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class NonSelfOwnedManage(BusinessData, PublicMethod, NonSelfOwnedManagePage):
    def __init__(self):
        BusinessData.__init__(self)
        PublicMethod.__init__(self)
        NonSelfOwnedManagePage.__init__(self)
        self.businessnumber = ''
        self.operator = ''
        self.twolevelclassification = ''
        self.accounts = ''
        self.state = ''
        self.predeterminedprice = ''
        self.scheduleddate = ''
        self.scheduledduedate = ''
        self.preoccupiedperson = ''
        self.startdate = ''
        self.closingdate = ''
        self.packageprice = ''
        self.reservations = ''
        self.agentexclusive = ''
        self.numbercategory = ''
        self.ispromotionalnumber = ''
        self.nonselflog = self.logging.getLogger('NonSelf')
        self.nonselflog.addHandler(self.logscr)

    def getnuminfo(self, db_id):
        numinfo_collection = self.db['biz_nonselfownedmanage']
        collection_str = numinfo_collection.find({"_id": int(db_id)})
        self.businessnumber = collection_str[0]['businessnumber']
        self.operator = collection_str[0]['operator']
        self.twolevelclassification = collection_str[0]['twolevelclassification']
        self.accounts = collection_str[0]['accounts']
        self.state = collection_str[0]['state']
        self.predeterminedprice = collection_str[0]['predeterminedprice']
        self.scheduleddate = collection_str[0]['scheduleddate']
        self.scheduledduedate = collection_str[0]['scheduledduedate']
        self.preoccupiedperson = collection_str[0]['preoccupiedperson']
        self.startdate = collection_str[0]['startdate']
        self.closingdate = collection_str[0]['closingdate']
        self.packageprice = collection_str[0]['packageprice']
        self.reservations = collection_str[0]['reservations']
        self.agentexclusive = collection_str[0]['agentexclusive']
        self.numbercategory = collection_str[0]['numbercategory']
        self.ispromotionalnumber = collection_str[0]['ispromotionalnumber']

    def addnum400(self, driver):
        biz_num = self.num400exists()
        self.getnuminfo(0)
        # 进入非自属号码管理页面
        self.nonselflog.info('into menu')
        self.entermenu(driver, '400号码管理', '非自属号码管理')
        WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, self.nonselfiframe)))
        driver.switch_to_frame(driver.find_element_by_xpath(self.nonselfiframe))
        WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, self.btn_addnum)))
        # 进入添加号码页面
        self.nonselflog.info('into add number')
        driver.find_element_by_xpath(self.btn_addnum).click()
        WebDriverWait(driver, 5, 0.5).until(ec.presence_of_element_located((By.XPATH, self.frame_business_bumber)))
        # 输入业务号码
        self.nonselflog.info('input number')
        driver.find_element_by_xpath(self.frame_business_bumber).send_keys(biz_num)
        # time.sleep(10)
        operator_num = self.comboboxvalue(driver, self.operator)
        assert operator_num is not None
        operator_js = '$(\'#fl\').combobox(\'select\', \'%s\')' % operator_num
        # 选择运营商
        self.nonselflog.info('select operator')
        driver.execute_script(operator_js)
        twolevel_num = self.comboboxvalue(driver, self.twolevelclassification)
        assert twolevel_num is not None
        operator_js = '$(\'#secondfl\').combobox(\'select\', \'%s\')' % twolevel_num
        # 选择二级代理商
        self.nonselflog.info('select twolevelclassification')
        driver.execute_script(operator_js)


if __name__ == '__main__':
    a = NonSelfOwnedManage()
    a.getnuminfo('0')
