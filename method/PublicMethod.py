# !/usr/local/python
# -*- coding: UTF-8 -*-
import time
from element.HomePage import HomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class PublicMethod(HomePage):
    def __init__(self):
        HomePage.__init__(self)

    def entermenu(self, driver, parentmenuname, subname):
        WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((
            By.XPATH, self.parentmenu(parentmenuname))))
        js_str = 'return $(\'div:contains("%s")[class="panel-title panel-with-icon"]\').parent().nextAll().' \
                 'find(\'div:contains("%s")\').parent().css(\'display\')' % (parentmenuname, subname)
        status = driver.execute_script(js_str)
        if 'none' == status:
            driver.find_element_by_xpath(self.parentmenu(parentmenuname)).click()
        driver.find_element_by_xpath(self.submenu(parentmenuname, subname)).click()

    @staticmethod
    def comboboxvalue(driver, option):
        while True:
            js_existence = 'return $(\'div[class*="combobox-item"]:contains("%s")\').length>0' % option
            print(js_existence)
            existence = driver.execute_script(js_existence)
            print(existence)
            if 'True' == str(existence):
                break
            else:
                time.sleep(0.5)
        js_str = 'return $(\'div[class*="combobox-item"]:contains("%s")\').attr(\'value\')' % option
        print(js_str)
        value = driver.execute_script(js_str)
        print(value)
        return value
