# !/usr/local/python
# -*- coding: UTF-8 -*-
from selenium import webdriver


class OpenBrowser(object):
    def __init__(self):
        self.browser = webdriver.Chrome()
        # 隐式等待5秒
        self.browser.implicitly_wait(5)


# if __name__ == '__main__':
#     a = OpenBrowser()
#     a.browser.get("http://101.200.123.227:8081/xtboss")
