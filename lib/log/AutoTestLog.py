# !/usr/local/python
# -*- coding: UTF-8 -*-
import logging
import os
import sys
import time


class AutoTestLog(object):
    def __init__(self):
        self.logging = logging
        # 定义工程的初始路径
        os.chdir(os.path.dirname(sys.argv[0]))
        basepath = os.path.dirname(os.path.dirname(os.path.dirname(sys.argv[0])))

        # 定义日志文件输入的路径及文件名
        logfile = '%s/LOG/AutoTestLog%s.log' % (basepath, time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        self.logging.basicConfig(filename=logfile, level=self.logging.DEBUG,
                                 format='%(asctime)s %(name)s %(lineno)d %(levelname)s %(message)s',
                                 datefmt='%Y-%m-%d-%a %H:%M:%S', filemode='w')

        # 设置一个屏幕打印的句柄
        formatter = self.logging.Formatter('%(asctime)s %(name)s %(lineno)d %(levelname)s  %(message)s')
        setlevel = self.logging.DEBUG
        self.logscr = self.logging.StreamHandler()
        self.logscr.setLevel(setlevel)
        self.logscr.setFormatter(formatter)


if __name__ == '__main__':
    a = AutoTestLog()
    loggerBGCPL = logging.getLogger('main')
    loggerBGCPL.addHandler(a.logscr)
    loggerBGCPL.info('aaa')
