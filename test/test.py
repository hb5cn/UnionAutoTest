# !/usr/local/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import unittest


class FirstTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def testone(self):
        self.browser.get('https://www.baidu.com')
        self.browser.maximize_window()
        browsertitle = self.browser.title
        self.assertEqual(browsertitle, '百度一下，你就知道')
        self.browser.quit()

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(FirstTest('testone'))
        return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(FirstTest.suite())
    print(result)
