# !/usr/local/python
# -*- coding: UTF-8 -*-
import os
import time
import shutil
import unittest
from pymongo import errors
from lib.report import HTMLTestRunner
from data.InitConnect import ConnectSql
from uniontest.Public.LoginPage import TestLoginPage


class RunTestMain(unittest.TestCase, ConnectSql):
    def __init__(self):
        ConnectSql.__init__(self)
        # 初始化mongodb的连接
        self.conn_mongo = self.connectmongo()
        self.db = self.conn_mongo['autotest']
        self.runmanlog = self.logging.getLogger('RunMain')
        # 初始化时间戳
        self.nowtime = time.strftime("%Y%m%d%H%M%S")

    def suiteall(self):
        caselist = []
        self.collection = self.db['testcase']
        # 从testcase集合中
        for i in self.collection.find({}, {"casename": 1, "method": 1, "casefile": 1, "module": 1}):
            caselist.append(eval(i['method']+'("'+i['casename']+'")'))
        suite = unittest.TestSuite()
        # 测试套添加内容
        suite.addTests(caselist)
        return suite

    def main(self):
        report_repash = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'report', '%s.html'
                                     % self.nowtime)
        fp = open(report_repash, "wb")  # 保存报告文件
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', screentime=self.nowtime)
        runner.run(self.suiteall())  # 执行用例
        fp.close()

    def backupscreen(self, time_id=0):
        self.collection = self.db['timestamp']
        try:
            self.collection.insert_one({"_id": time_id, "time": self.nowtime})
        except errors.DuplicateKeyError:
            self.collection.update_one({"_id": time_id}, {'$set': {"time": self.nowtime}})
        png_floder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                       'ScreenShots', 'backup_%s' % self.nowtime)
        if not os.path.exists(png_floder_path):
            os.mkdir(png_floder_path)

        source_png_path = os.path.join(os.path.dirname(png_floder_path), 'screennow')
        if os.path.exists(png_floder_path):
            shutil.rmtree(png_floder_path)
        shutil.move(source_png_path, png_floder_path)
        os.mkdir(source_png_path)


if __name__ == '__main__':
    a = RunTestMain()
    a.main()
    a.backupscreen()
