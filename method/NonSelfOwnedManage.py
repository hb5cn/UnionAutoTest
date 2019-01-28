# !/usr/local/python
# -*- coding: UTF-8 -*-
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
        self.nonselflog = self.logging.getLogger('NonSelfMethod')
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
        WebDriverWait(driver, 5, 0.5).until(ec.presence_of_element_located((By.XPATH, self.frame_business_number)))

        # 输入业务号码
        self.nonselflog.info('input number')
        driver.find_element_by_xpath(self.frame_business_number).send_keys(biz_num)

        # 选择运营商
        self.nonselflog.info('select operator')
        self.comboboxsetvalue(driver, 'fl', self.operator)

        # 选择二级代理商
        self.nonselflog.info('select twolevelclassification')
        self.comboboxsetvalue(driver, 'secondfl', self.twolevelclassification)

        # 选择帐号
        self.nonselflog.info('select accounts')
        self.comboboxsetvalue(driver, 'zh', self.accounts)

        # 选择状态
        self.nonselflog.info('select accounts')
        self.comboboxsetvalue(driver, 'statu', self.state)

        # 输入预定价
        self.nonselflog.info('Input predeterminedprice')
        if self.predeterminedprice:
            driver.find_element_by_xpath(self.frame_predete_value).send_keys(self.predeterminedprice)

        # 输入预定开始日期
        self.nonselflog.info('select scheduleddate')
        self.setdata(driver, 'ydrq', self.scheduleddate)

        # 输入预定结束日期
        self.nonselflog.info('select scheduledduedate')
        self.setdata(driver, 'ydrq2', self.scheduledduedate)

        # 选择预占人
        self.nonselflog.info('select preoccupiedperson')
        if self.preoccupiedperson:
            driver.find_element_by_xpath(self.frame_preoccupied_person).click()
            driver.find_element_by_xpath(self.frame_employee_selection).send_keys(self.preoccupiedperson)
            driver.find_element_by_xpath(self.frame_employee_selection_search).click()
            driver.find_element_by_xpath('//span[text()="%s"]' % self.preoccupiedperson).click()
            driver.find_element_by_xpath(self.frame_employee_selection_frambutton).click()
            driver.find_element_by_xpath(self.frame_employee_selection_close).click()

        # 选择开始日期
        self.nonselflog.info('select startdate')
        self.setdata(driver, 'ks', self.startdate)

        # 选择截止日期
        self.nonselflog.info('select closingdate')
        self.setdata(driver, 'jzrq', self.closingdate)

        # 输入套餐标价
        self.nonselflog.info('Input packageprice')
        driver.find_element_by_xpath(self.frame_ackage_value).send_keys(self.packageprice)

        # 选择预订人
        self.nonselflog.info('select reservations')
        if self.reservations:
            driver.find_element_by_xpath(self.frame_preoccupied_person).click()
            driver.find_element_by_xpath(self.frame_employee_selection).send_keys(self.preoccupiedperson)
            driver.find_element_by_xpath(self.frame_employee_selection_search).click()
            driver.find_element_by_xpath('//span[text()="%s"]' % self.reservations).click()
            driver.find_element_by_xpath(self.frame_employee_selection_frambutton).click()
            driver.find_element_by_xpath(self.frame_employee_selection_close).click()

        # 选择是否代理商专属
        self.nonselflog.info('select agentexclusive')
        self.comboboxsetvalue(driver, 'oewagnet', self.agentexclusive)

        # 选择号码类别
        self.nonselflog.info('select numbercategory')
        self.comboboxsetvalue(driver, 'sort', self.numbercategory)

        # 选择是否促销号码
        self.nonselflog.info('select ispromotionalnumber')
        self.comboboxsetvalue(driver, 'promotionNum', self.ispromotionalnumber)

        # 点击提交
        self.nonselflog.info('submit number400')
        driver.find_element_by_xpath(self.frame_submit).click()
        WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, self.frame_addsuccessfram)))
        driver.find_element_by_xpath(self.frame_addsuccessfram_btn).click()

        # 检查是否添加成功
        driver.find_element_by_xpath(self.search_business_number).send_keys(biz_num)
        driver.find_element_by_xpath(self.search_search_btn).click()


if __name__ == '__main__':
    a = NonSelfOwnedManage()
    a.getnuminfo('0')
