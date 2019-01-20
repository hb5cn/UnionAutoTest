# !/usr/local/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class CloseBrowser(object):
    def __init__(self):
        pass

    @staticmethod
    def quitboss(driver, topbarstatus_path, exitsystem_path, verificationelement, topbar):
        js_script = 'return %s' % topbarstatus_path
        # 获取上方状态栏的展开状态
        topbar_status = driver.execute_script(js_script)
        if 'none' == topbar_status:
            # 如果状态是none，则点击上方状态栏
            driver.find_element_by_xpath(topbar).click()
            # 点击退出系统
            driver.find_element_by_xpath(exitsystem_path).click()
            # 判断是否退出正常
            WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH, verificationelement)))
            driver.quit()
        elif 'block' == topbar_status:
            # 如果状态是block，则点击上方状态栏
            driver.find_element_by_xpath(exitsystem_path).click()
            # 点击退出系统
            WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH, verificationelement)))
            # 判断是否退出正常
            driver.quit()


if __name__ == '__main__':
    pass
