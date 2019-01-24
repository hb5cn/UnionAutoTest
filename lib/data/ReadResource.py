# !/usr/local/python
# -*- coding: UTF-8 -*-
import configparser
import os
import sys


class Readresource(object):
    def __init__(self):
        # 读取ini配置文件
        self.conf = configparser.ConfigParser()
        self.configfile = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                       'config/resource.ini')
        self.conf.read(self.configfile)

    def mongoip(self):
        # 返回配置文件中MongoDB的ip地址
        return self.conf.get('mongodb', 'ip')

    def mongoport(self):
        # 返回配置文件中MongoDB的端口
        return self.conf.get('mongodb', 'prot')


if __name__ == '__main__':
    a = Readresource()
    print(a.mongoip())

