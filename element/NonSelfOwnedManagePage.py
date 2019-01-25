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
        self.frame_business_bumber = '//input[@id="sys_num"]'
        self.frame_business_bumber = '//input[@id="sys_num"]'
