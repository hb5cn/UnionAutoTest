# !/usr/local/python
# -*- coding: UTF-8 -*-


class HomePage(object):
    def __init__(self):
        self.refresh = '//input[@id="button5"]'
        self.topbarstatus = "$('#topDiv').css('display')"
        self.exitsystem = '//a[@onclick="logout();"]'
        self.topbar = '//a[@class="layout-button-down"]'
