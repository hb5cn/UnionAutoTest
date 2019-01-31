# !/usr/local/python
# -*- coding: UTF-8 -*-


class PricingManagementPage(object):
    def __init__(self):
        self.primagframe = '//iframe[@src="/xtboss/union400/resource/page/numberManage/numStaffManage.jsp"]'
        self.search_number = '//input[@name="sns.number400"]'
        self.search_btn = '//span[text()="查询"]'
        self.tab_wait_text = '//div[text()="数据装载中......"]'
