# !/usr/local/python
# -*- coding: UTF-8 -*-
from pymongo import MongoClient
from log.AutoTestLog import AutoTestLog


class ConnectSql(AutoTestLog):
    def __init__(self):
        AutoTestLog.__init__(self)
        # 初始化日志句柄
        self.connectlog = self.logging.getLogger('ConnectSql')
        self.connectlog.addHandler(self.logscr)

    def connectmongo(self, mongoip, mongoprot):
        self.connectlog.debug('MongodbIP is %s' % str(mongoip))
        self.connectlog.debug('Mongodbprot is %s' % str(mongoprot))
        # 返回MongoDB连接句柄
        conn = MongoClient(mongoip, int(mongoprot))
        return conn


if __name__ == '__main__':
    a = ConnectSql()
    b = a.connectmongo('10.10.17.222', 27017)
    my_set = b.autotest.connectinfo
    # for i in my_set.find({'_id': 0}):
    #     print(i)
    c = my_set.find_one({'_id': 0}, {"bossurl": 1, "_id": 0})
    print(c['bossurl'])
