# !/usr/local/python
# -*- coding: UTF-8 -*-
import unittest
from lib.data.LoginData import LoginData
from uniontest.Public.LoginPage import TestLoginPage


class RunTestMain(unittest.TestCase, LoginData):
    def __init__(self):
        LoginData.__init__(self, 'testcase')

    def suiteall(self):
        caselist = []
        for i in self.collection.find({}, {"casename": 1, "method": 1, "casefile": 1, "module": 1}):
            caselist.append(eval(i['method']+'("'+i['casename']+'")'))
        suite = unittest.TestSuite()
        # 测试套添加内容
        suite.addTests(caselist)
        return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    a = RunTestMain().suiteall()
    result = runner.run(a)
