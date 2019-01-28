# !/usr/local/python
# -*- coding: UTF-8 -*-


class NonSelfOwnedManagePage(object):
    def __init__(self):
        self.nonselfiframe = '//iframe[@src="/xtboss/union400/resource/page/numberManage/numManage.jsp"]'
        self.btn_addnum = '//a[@id="add"]'
        self.btn_turn_to_own_number = '//a[@id="reservSelf"]'
        self.btn_transfer_to_agent = '//span[text()="转给代理商"]'
        self.btn_transfer_from_agent = '//span[text()="从代理商转出"]'
        self.search_business_number = '//input[@name="sns.number400"]'
        self.search_Preoccupation = '//input[@name="sns.capturename"]'
        self.search_reservations = '//input[@name="sns.subscribename"]'
        self.search_package_price_start = '//input[@id="start"]'
        self.search_package_price_end = '//input[@id="end"]'
        self.search_operator = '//input[@name="sns.category"]/preceding-sibling::input'
        self.search_two_level_classification = '//input[@name="sns.category2"]/preceding-sibling::input'
        self.search_state = '//input[@name="sns.status"]/preceding-sibling::input'
        self.search_account_number = '//input[@name="sns.accountname"]/preceding-sibling::input'
        self.search_number_category = '//input[@id="resever6"]/following-sibling::span/input'
        self.search_search_btn = '//span[text()="查询"]'
        self.frame_business_number = '//input[@id="sys_num"]'
        self.frame_predete_value = '//input[@id="ydj"]'
        self.frame_preoccupied_person = '//input[@id="yzr"]'
        self.frame_employee_selection = '//input[@id="ss"]'
        self.frame_employee_selection_search = '//input[@onclick="seachStaff()"]'
        self.frame_employee_selection_frambutton = '//span[text()="确定"]'
        self.frame_employee_selection_close = '//div[text()="员工选择"]/following-sibling::div'
        self.frame_ackage_value = '//input[@id="tcbj"]'
        self.frame_submit = '//input[@id="sub1"]'
        self.frame_addsuccessfram = '//div[text()="保存成功"]'
        self.frame_addsuccessfram_btn = '//div[text()="保存成功"]/following-sibling::div//span[text()="确定"]'
