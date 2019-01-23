# !/usr/local/python
# -*- coding: UTF-8 -*-
import unittest
from data import InitConnect, ReadResource
from uniontest.Public.LoginPage import TestLoginPage


class RunTestMain(unittest.TestCase, ReadResource.Readresource, InitConnect.ConnectSql):
    def __init__(self):
        InitConnect.ConnectSql.__init__(self)
        ReadResource.Readresource.__init__(self, 'testcase')
        self.mongo_ip = ReadResource.Readresource.mongoip(self)
        self.mongo_prot = ReadResource.Readresource.mongoport(self)
        self.mongo_database = ReadResource.Readresource.mongodatabase(self)
        self.mongo_collection = ReadResource.Readresource.mongocollection(self)
        self.mongo_id = int(ReadResource.Readresource.mongoid(self))
        self.conn_mongo = self.connectmongo(self.mongo_ip, self.mongo_prot)
        self.db = self.conn_mongo[self.mongo_database]
        self.collection = self.db[self.mongo_collection]

    def suiteall(self):
        caselist = []
        for i in self.collection.find({}, {"casename": 1, "method": 1, "casefile": 1, "module": 1}):
            caselist.append(eval(i['method']+'("'+i['casename']+'")'))
        suite = unittest.TestSuite()
        # 测试套添加内容
        suite.addTests(caselist)
        return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    a = RunTestMain().suiteall()
    result = runner.run(a)
