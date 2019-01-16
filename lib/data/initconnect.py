# !/usr/local/python
# -*- coding: UTF-8 -*-
from pymongo import MongoClient
from log.AutoTestLog import AutoTestLog


class ConnectSql(AutoTestLog):
    def __init__(self):
        AutoTestLog.__init__(self)
        self.connectlog = self.logging.getLogger('ConnectSql')
        self.connectlog.addHandler(self.logscr)

    def connectmongo(self, mongoip, mongoprot):
        self.connectlog.debug('MongodbIP is %s' % str(mongoip))
        self.connectlog.debug('Mongodbprot is %s' % str(mongoprot))
        conn = MongoClient(mongoip, mongoprot)
        return conn


if __name__ == '__main__':
    a = ConnectSql()
    b = a.connectmongo('10.10.17.222', 27017)
    print(b)
