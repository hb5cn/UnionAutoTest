# !/usr/local/python
# -*- coding: UTF-8 -*-
from data import initconnect, readresource


class LoginData(initconnect.ConnectSql, readresource.Readresource):
    def __init__(self):
        initconnect.ConnectSql.__init__(self)
        readresource.Readresource.__init__(self)
        self.conn_mongo = None
        self.db = None
        self.collection = None
        self.logindatalog = self.logging.getLogger('LoginData')
        self.logindatalog.addHandler(self.logscr)
        self.mongo_ip = readresource.Readresource.mongoip(self)
        self.mongo_prot = readresource.Readresource.mongoport(self)
        self.mongo_database = readresource.Readresource.mongodatabase(self)
        self.mongo_collection = readresource.Readresource.mongocollection(self)
        self.mongo_id = int(readresource.Readresource.mongoid(self))

    def bossurl(self):
        self.conn_mongo = self.connectmongo(self.mongo_ip, self.mongo_prot)
        self.db = self.conn_mongo[self.mongo_database]
        self.collection = self.db[self.mongo_collection]
        # 查询要登录的boss的地址
        boss_url = self.collection.find_one({'_id': self.mongo_id}, {"bossurl": 1, "_id": self.mongo_id})['bossurl']
        self.logindatalog.info('Boss url is : --->%s<---' % str(boss_url))
        return boss_url


if __name__ == '__main__':
    a = LoginData()
    print(a.bossurl())
