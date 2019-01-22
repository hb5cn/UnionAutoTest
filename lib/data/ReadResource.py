# !/usr/local/python
# -*- coding: UTF-8 -*-
import configparser
import os
import sys


class Readresource(object):
    def __init__(self, section):
        # 读取ini配置文件
        self.conf = configparser.ConfigParser()
        self.configfile = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                       'config/resource.ini')
        self.conf.read(self.configfile)
        self.section = section

    def mongoip(self):
        # 返回配置文件中MongoDB的ip地址
        return self.conf.get(self.section, 'ip')

    def mongoport(self):
        # 返回配置文件中MongoDB的端口
        return self.conf.get(self.section, 'prot')

    def mongodatabase(self):
        # 返回配置文件中MongoDB要连接的数据库
        return self.conf.get(self.section, 'database')

    def mongocollection(self):
        # 返回配置文件中MongoDB要连接的文件集合
        return self.conf.get(self.section, 'collection')

    def mongoid(self):
        # 返回配置文件中MongoDB要查询的id号
        return self.conf.get(self.section, 'id')


if __name__ == '__main__':
    a = Readresource()
    print(a.mongoip())

