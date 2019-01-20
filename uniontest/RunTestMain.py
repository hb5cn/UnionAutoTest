# !/usr/local/python
# -*- coding: UTF-8 -*-
import unittest
from uniontest.Public.LoginPage import TestLoginPage


class RunTestMain(unittest.TestCase):
    @staticmethod
    def suiteall():
        suite = unittest.TestSuite()
        suite.addTest(TestLoginPage('test_normallogin'))
        return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    a = RunTestMain().suiteall()
    result = runner.run(a)
