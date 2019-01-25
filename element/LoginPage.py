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
        self.msgframe = '//div[contains(@class, "messager-body")]/div[2]'
        self.msgframe2 = '//div[contains(@class, "messager-body")]/div[1]'
        self.msgframebutton = '//div[contains(@class, "messager-body")]/div[last()]/a'
        self.msgframe3 = '//div[text()="此用户正在登录使用中..是否强制注销？"]'
        self.msgframe3button = '//div[text()="此用户正在登录使用中..是否强制注销？"]/following-sibling::div//span[text()="确定"]'
        self.msgframe4 = '//div[text()="强制注销成功"]'
        self.msgframe4button = '//div[text()="强制注销成功"]/following-sibling::div//span[text()="确定"]'
        self.msgframe5 = '//div[text()="登录过于频繁，请稍后再登！"]'
        self.msgframe5button = '//div[text()="登录过于频繁，请稍后再登！"]/following-sibling::div//span[text()="确定"]'

