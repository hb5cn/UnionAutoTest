# !/usr/local/python
# -*- coding: UTF-8 -*-
import logging
import os
import time


class AutoTestLog(object):
    def __init__(self):
        self.logging = logging
        # 定义工程的初始路径
        basepath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        # 定义日志文件输入的路径及文件名
        logfile = '%s/LOG/AutoTestLog%s.log' % (basepath, time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        self.logging.basicConfig(filename=logfile, level=self.logging.INFO,
                                 format='%(asctime)s %(thread)d %(filename)s %(funcName)s %(lineno)d '
                                        '%(levelname)s %(message)s',
                                 datefmt='%Y-%m-%d-%a %H:%M:%S', filemode='w')
        # 设置一个屏幕打印的句柄
        formatter = self.logging.Formatter('%(asctime)s %(thread)d %(filename)s %(funcName)s %(lineno)d '
                                           '%(levelname)s  %(message)s')
        setlevel = self.logging.INFO
        self.logscr = self.logging.StreamHandler()
        self.logscr.setLevel(setlevel)
        self.logscr.setFormatter(formatter)
        self.mainlog = self.logging.getLogger('LOG')
        if 0 == len(self.mainlog.handlers):
            self.mainlog.addHandler(self.logscr)


if __name__ == '__main__':
    pass
    # a = AutoTestLog()
    # a.main()
