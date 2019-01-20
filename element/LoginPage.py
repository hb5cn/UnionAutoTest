# !/usr/local/python
# -*- coding: UTF-8 -*-


class LoginPage(object):
    def __init__(self):
        self.username = '//input[@id="loginname"]'
        self.password = '//input[@id="password"]'
        self.verificationcodepicture = '//img[@id="captchaImg"]'
        self.verificationcode = '//input[@name="j_captcha"]'
        self.confirm = '//a[@onclick="login();"]'
        self.reset = '//a[@onclick="login_clear();"]'
        self.wechat = '//span[text()="微信登录"]'
        self.tips = '//div[contains(@class, "tooltip tooltip-right")]/div[1]'
