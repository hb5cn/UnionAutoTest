# !/usr/local/python
# -*- coding: UTF-8 -*-
import configparser
import os
import sys


class Readresource(object):
    def __init__(self):
        # 读取ini配置文件
        self.conf = configparser.ConfigParser()
        self.configfile = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(sys.argv[0]))),
                                       'config/resource.ini')
        self.conf.read(self.configfile)

    def mongoip(self):
        # 返回配置文件中MongoDB的ip地址
        return self.conf.get('mongodb', 'ip')

    def mongoport(self):
        # 返回配置文件中MongoDB的端口
        return self.conf.get('mongodb', 'prot')

    def mongodatabase(self):
        # 返回配置文件中MongoDB要连接的数据库
        return self.conf.get('mongodb', 'database')

    def mongocollection(self):
        # 返回配置文件中MongoDB要连接的文件集合
        return self.conf.get('mongodb', 'collection')

    def mongoid(self):
        # 返回配置文件中MongoDB要查询的id号
        return self.conf.get('mongodb', 'id')


if __name__ == '__main__':
    a = Readresource()
    print(a.mongoip())

