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
        # 等待子菜单出现
        WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((
            By.XPATH, self.parentmenu(parentmenuname))))
        # 查看父菜单的打开状态是否为开启
        js_str = 'return $(\'div:contains("%s")[class="panel-title panel-with-icon"]\').parent().nextAll().' \
                 'find(\'div:contains("%s")\').parent().css(\'display\')' % (parentmenuname, subname)
        status = driver.execute_script(js_str)
        # 如果不为开启，则点击父菜单开启该菜单
        if 'none' == status:
            driver.find_element_by_xpath(self.parentmenu(parentmenuname)).click()
        driver.find_element_by_xpath(self.submenu(parentmenuname, subname)).click()

    @staticmethod
    def comboboxvalue(driver, option):
        # 判断页面中要选择的选项是否加载完成
        while True:
            js_existence = 'return $(\'div[class*="combobox-item"]:contains("%s")\').length>0' % option
            existence = driver.execute_script(js_existence)
            if 'True' == str(existence):
                break
            else:
                time.sleep(0.5)
        # 返回要选择的选项的value值
        js_str = 'return $(\'div[class*="combobox-item"]:contains("%s")\').attr(\'value\')' % option
        value = driver.execute_script(js_str)
        return value

    def comboboxsetvalue(self, driver, combo_id, option):
        """
        combo_id必须是id
        """
        # 获取要选择的选项的value值
        value = self.comboboxvalue(driver, option)
        assert value is not None
        # 使用节点来在选择框内选择要选择的选项
        js = '$(\'#%s\').combobox(\'select\', \'%s\')' % (combo_id, value)
        driver.execute_script(js)

    @staticmethod
    def setdata(driver, datebox_id, date):
        date_js = '$(\'#%s\').datebox(\'setValue\', \'%s\')' % (datebox_id, date)
        driver.execute_script(date_js)

    @staticmethod
    def istablecontent(driver, tablepath='//div[@class="datagrid-view2"]', title='', text=''):
        """
        Determine whether there are relevant items in the table
        """
        # 获取该内容列的号码
        col_last_path = '%s/div/div/table/tbody/tr/td[last()]/div/span[1]' % tablepath
        col_last_str = driver.find_element_by_xpath(col_last_path).text
        col_num = 1
        while True:
            xpath = '%s/div/div/table/tbody/tr/td[%d]/div/span[1]' % (tablepath, col_num)
            now_str = driver.find_element_by_xpath(xpath).text
            if now_str == title:
                break
            if now_str == col_last_str:
                break

        row_last_path = ''
