# !/usr/local/python
# -*- coding: UTF-8 -*-
from data import initconnect


class LoginData(initconnect.ConnectSql):
    def __init__(self):
        initconnect.ConnectSql.__init__(self)
        self.logindatalog = self.logging.getLogger('LoginData')
        self.logindatalog.addHandler(self.logscr)

    def main(self):
        self.logindatalog.info('11111')


if __name__ == '__main__':
    a = LoginData()
    a.main()
