# !/usr/local/python
# -*- coding: UTF-8 -*-
from pymongo import MongoClient
from log.AutoTestLog import AutoTestLog
from data.ReadResource import Readresource


class ConnectSql(AutoTestLog, Readresource):
    def __init__(self):
        AutoTestLog.__init__(self)
        Readresource.__init__(self)
        # 初始化日志句柄
        self.connectlog = self.logging.getLogger('ConnectSql')
        self.connectlog.addHandler(self.logscr)

    def connectmongo(self):
        # self.connectlog.info('MongodbIP is %s' % str(self.mongoip()))
        # self.connectlog.info('Mongodbprot is %s' % str(self.mongoport()))
        # 返回MongoDB连接句柄
        conn = MongoClient(self.mongoip(), int(self.mongoport()))
        return conn


if __name__ == '__main__':
    a = ConnectSql()
    b = a.connectmongo()
