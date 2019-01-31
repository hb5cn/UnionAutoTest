# !/usr/local/python
# -*- coding: UTF-8 -*-
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from element.HomePage import HomePage
from element.LoginPage import LoginPage


class CloseBrowser(HomePage, LoginPage):
    def __init__(self):
        HomePage.__init__(self)
        LoginPage.__init__(self)

    def quitandclose(self, driver):
        js_script = 'return %s' % self.topbarstatus
        # 获取上方状态栏的展开状态
        topbar_status = driver.execute_script(js_script)
        if 'none' == str(topbar_status).lower():
            # 如果状态是none，则点击上方状态栏
            driver.find_element_by_xpath(self.topbar).click()
            while True:
                px = driver.execute_script('return $(\'#topDiv\').parent().css(\'top\')')
                if '0px' == px:
                    break
                else:
                    time.sleep(0.5)
            # 点击退出系统
            driver.find_element_by_xpath(self.exitsystem).click()
            # 判断是否退出正常
            WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH, self.username)))
            driver.quit()
        elif 'block' == str(topbar_status).lower():
            # 如果状态是block，则点击退出
            driver.find_element_by_xpath(self.exitsystem).click()
            # 判断是否退出正常
            WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH, self.username)))
            driver.quit()

    def quitboss(self, driver):
        js_script = 'return %s' % self.topbarstatus
        # 获取上方状态栏的展开状态
        topbar_status = driver.execute_script(js_script)
        if 'none' == str(topbar_status).lower():
            # 如果状态是none，则点击上方状态栏
            driver.find_element_by_xpath(self.topbar).click()
            while True:
                px = driver.execute_script('return $(\'#topDiv\').parent().css(\'top\')')
                if '0px' == px:
                    break
                else:
                    time.sleep(0.5)
            # 点击退出系统
            driver.find_element_by_xpath(self.exitsystem).click()
            # 判断是否退出正常
            WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH, self.username)))
        elif 'block' == str(topbar_status).lower():
            # 如果状态是block，则点击退出
            driver.find_element_by_xpath(self.exitsystem).click()
            # 判断是否退出正常
            WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH, self.username)))


if __name__ == '__main__':
    pass
