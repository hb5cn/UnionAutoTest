# !/usr/local/python
# -*- coding: UTF-8 -*-


class HomePage(object):
    def __init__(self):
        self.refresh = '//input[@id="button5"]'
        self.topbarstatus = "$('#topDiv').css('display')"
        self.exitsystem = '//a[@onclick="logout();"]'
        self.topbar = '//a[@class="layout-button-down"]'
        self.topbar_up = '//a[@class="layout-button-up"]'

    @staticmethod
    def parentmenu(menuname):
        parentmenu = '//div[text()="%s"]' % menuname
        return parentmenu

    @staticmethod
    def submenu(parentname, subname):
        subname = '//div[text()="%s"]/parent::div/following-sibling::div//a[text()="%s"]' % (parentname, subname)
        return subname
