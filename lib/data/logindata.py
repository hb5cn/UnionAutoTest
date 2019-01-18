# !/usr/local/python
# -*- coding: UTF-8 -*-
from data import initconnect, readresource
import traceback


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
        self.conn_mongo = self.connectmongo(self.mongo_ip, self.mongo_prot)
        self.db = self.conn_mongo[self.mongo_database]
        self.collection = self.db[self.mongo_collection]

    def bossurl(self):
        # 查询要登录的boss的地址
        boss_url = ''
        try:
            boss_url = self.collection.find_one({'_id': self.mongo_id}, {"bossurl": 1, "_id": self.mongo_id})['bossurl']
            self.logindatalog.info('Boss url is : --->%s<---' % str(boss_url))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return boss_url

    def operation_login_username(self):
        # 查询要登录的运维的帐号
        operation_login_username = ''
        try:
            operation_login_username = self.collection.find_one(
                {'_id': self.mongo_id}, {"operation_login_username": 1,
                                         "_id": self.mongo_id})['operation_login_username']
            self.logindatalog.info('operation login username is : --->%s<---' % str(operation_login_username))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return operation_login_username

    def salesman_login_username(self):
        # 查询要登录的销售的帐号1
        salesman_login_username = ''
        try:
            salesman_login_username = self.collection.find_one(
                {'_id': self.mongo_id}, {"salesman_login_username": 1, "_id": self.mongo_id})['salesman_login_username']
            self.logindatalog.info('salesman login username is : --->%s<---' % str(salesman_login_username))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return salesman_login_username

    def salesman_login_username2(self):
        # 查询要登录的销售的帐号2
        salesman_login_username2 = ''
        try:
            salesman_login_username2 = self.collection.find_one(
                {'_id': self.mongo_id}, {"salesman_login_username2": 1,
                                         "_id": self.mongo_id})['salesman_login_username2']
            self.logindatalog.info('salesman login username2 is : --->%s<---' % str(salesman_login_username2))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return salesman_login_username2

    def salesman_login_username3(self):
        # 查询要登录的销售的帐号3
        salesman_login_username3 = ''
        try:
            salesman_login_username3 = self.collection.find_one(
                {'_id': self.mongo_id}, {"salesman_login_username3": 1,
                                         "_id": self.mongo_id})['salesman_login_username3']
            self.logindatalog.info('salesman login username3 is : --->%s<---' % str(salesman_login_username3))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return salesman_login_username3

    def number_administrator_login_username(self):
        # 查询要登录的号码管理员的帐号
        number_administrator_login_username = ''
        try:
            number_administrator_login_username = self.collection.find_one(
                {'_id': self.mongo_id}, {"number_administrator_login_username": 1,
                                         "_id": self.mongo_id})['number_administrator_login_username']
            self.logindatalog.info('number administrator login username is : --->%s<---' %
                                   str(number_administrator_login_username))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return number_administrator_login_username

    def presale_login_username(self):
        # 查询要登录的售前的帐号
        presale_login_username = ''
        try:
            presale_login_username = self.collection.find_one(
                {'_id': self.mongo_id}, {"presale_login_username": 1, "_id": self.mongo_id})['presale_login_username']
            self.logindatalog.info('presale login username is : --->%s<---' % str(presale_login_username))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return presale_login_username

    def return_visit_login_username(self):
        # 查询要登录的回访的帐号
        return_visit_login_username = ''
        try:
            return_visit_login_username = self.collection.find_one(
                {'_id': self.mongo_id}, {"return_visit_login_username": 1,
                                         "_id": self.mongo_id})['return_visit_login_username']
            self.logindatalog.info('return visit login username is : --->%s<---' % str(return_visit_login_username))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return return_visit_login_username

    def charging_login_username(self):
        # 查询要登录的计费的帐号
        charging_login_username = ''
        try:
            charging_login_username = self.collection.find_one(
                {'_id': self.mongo_id}, {"charging_login_username": 1, "_id": self.mongo_id})['charging_login_username']
            self.logindatalog.info('charging login username is : --->%s<---' % str(charging_login_username))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return charging_login_username

    def renewcontract_login_username(self):
        # 查询要登录的续约的帐号
        renewcontract_login_username = ''
        try:
            renewcontract_login_username = self.collection.find_one(
                {'_id': self.mongo_id}, {"renewcontract_login_username": 1,
                                         "_id": self.mongo_id})['renewcontract_login_username']
            self.logindatalog.info('renewcontract login username is : --->%s<---' % str(renewcontract_login_username))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return renewcontract_login_username

    def productaudit_login_username(self):
        # 查询要登录的产品审核的帐号
        productaudit_login_username = ''
        try:
            productaudit_login_username = self.collection.find_one(
                {'_id': self.mongo_id}, {"productaudit_login_username": 1,
                                         "_id": self.mongo_id})['productaudit_login_username']
            self.logindatalog.info('productaudit login username is : --->%s<---' % str(productaudit_login_username))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return productaudit_login_username

    def productopening_login_username(self):
        # 查询要登录的产品开户的帐号
        productopening_login_username = ''
        try:
            productopening_login_username = self.collection.find_one(
                {'_id': self.mongo_id}, {"productopening_login_username": 1,
                                         "_id": self.mongo_id})['productopening_login_username']
            self.logindatalog.info('productopening login username is : --->%s<---' % str(productopening_login_username))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return productopening_login_username

    def finance_login_username(self):
        # 查询要登录的财务开户的帐号
        finance_login_username = ''
        try:
            finance_login_username = self.collection.find_one(
                {'_id': self.mongo_id}, {"finance_login_username": 1, "_id": self.mongo_id})['finance_login_username']
            self.logindatalog.info('finance login username is : --->%s<---' % str(finance_login_username))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return finance_login_username

    def finance_login_username2(self):
        # 查询要登录的财务开户的帐号2
        finance_login_username2 = ''
        try:
            finance_login_username2 = self.collection.find_one(
                {'_id': self.mongo_id}, {"finance_login_username2": 1, "_id": self.mongo_id})['finance_login_username2']
            self.logindatalog.info('finance login username2 is : --->%s<---' % str(finance_login_username2))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return finance_login_username2

    def ftersale_login_username(self):
        # 查询要登录的售后的帐号
        ftersale_login_username = ''
        try:
            ftersale_login_username = self.collection.find_one(
                {'_id': self.mongo_id}, {"ftersale_login_username": 1, "_id": self.mongo_id})['ftersale_login_username']
            self.logindatalog.info('ftersale login username is : --->%s<---' % str(ftersale_login_username))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return ftersale_login_username

    def zfw400_login_username(self):
        # 查询要登录自服务的400帐号
        zfw400_login_username = ''
        try:
            zfw400_login_username = self.collection.find_one(
                {'_id': self.mongo_id}, {"zfw400_login_username": 1, "_id": self.mongo_id})['zfw400_login_username']
            self.logindatalog.info('zfw400 login username is : --->%s<---' % str(zfw400_login_username))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(zfw400_login_username)

    def zfw400_login_username2(self):
        # 查询要登录自服务的400帐号2
        zfw400_login_username2 = ''
        try:
            zfw400_login_username2 = self.collection.find_one(
                {'_id': self.mongo_id}, {"zfw400_login_username2": 1, "_id": self.mongo_id})['zfw400_login_username2']
            self.logindatalog.info('zfw400 login username2 is : --->%s<---' % str(zfw400_login_username2))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(zfw400_login_username2)

    def zfw400_login_username3(self):
        # 查询要登录自服务的400帐号3
        zfw400_login_username3 = ''
        try:
            zfw400_login_username3 = self.collection.find_one(
                {'_id': self.mongo_id}, {"zfw400_login_username3": 1, "_id": self.mongo_id})['zfw400_login_username3']
            self.logindatalog.info('zfw400 login username3 is : --->%s<---' % str(zfw400_login_username3))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(zfw400_login_username3)

    def zfwln_login_username(self):
        # 查询要登录自服务的LN帐号
        zfwln_login_username = ''
        try:
            zfwln_login_username = self.collection.find_one(
                {'_id': self.mongo_id}, {"zfwln_login_username": 1, "_id": self.mongo_id})['zfwln_login_username']
            self.logindatalog.info('zfwln login username is : --->%s<---' % str(zfwln_login_username))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(zfwln_login_username)

    def zfwln_login_password(self):
        # 查询要登录自服务的LN密码
        zfwln_login_password = ''
        try:
            zfwln_login_password = self.collection.find_one(
                {'_id': self.mongo_id}, {"zfwln_login_password": 1, "_id": self.mongo_id})['zfwln_login_password']
            self.logindatalog.info('zfwln login password is : --->%s<---' % str(zfwln_login_password))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(zfwln_login_password)

    def login_password(self):
        # 查询要登录boss的密码
        login_password = ''
        try:
            login_password = self.collection.find_one(
                {'_id': self.mongo_id}, {"login_password": 1, "_id": self.mongo_id})['login_password']
            self.logindatalog.info('login password is : --->%s<---' % str(login_password))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(login_password)

    def verification_code(self):
        # 查询要登录boss的验证码
        verification_code = ''
        try:
            verification_code = self.collection.find_one(
                {'_id': self.mongo_id}, {"verification_code": 1, "_id": self.mongo_id})['verification_code']
            self.logindatalog.info('verification code is : --->%s<---' % str(verification_code))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(verification_code)

    def database_ip(self):
        # 查询boss的数据库ip地址
        database_ip = ''
        try:
            database_ip = self.collection.find_one(
                {'_id': self.mongo_id}, {"database_ip": 1, "_id": self.mongo_id})['database_ip']
            self.logindatalog.info('database ip is : --->%s<---' % str(database_ip))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(database_ip)

    def database_username(self):
        # 查询boss的数据库连接用户名
        database_username = ''
        try:
            database_username = self.collection.find_one(
                {'_id': self.mongo_id}, {"database_username": 1, "_id": self.mongo_id})['database_username']
            self.logindatalog.info('database username is : --->%s<---' % str(database_username))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(database_username)

    def database_password(self):
        # 查询boss的数据库连接密码
        database_password = ''
        try:
            database_password = self.collection.find_one(
                {'_id': self.mongo_id}, {"database_password": 1, "_id": self.mongo_id})['database_password']
            self.logindatalog.info('database password is : --->%s<---' % str(database_password))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(database_password)

    def database_port(self):
        # 查询boss的数据库端口
        database_port = ''
        try:
            database_port = self.collection.find_one(
                {'_id': self.mongo_id}, {"database_port2": 1, "_id": self.mongo_id})['database_port']
            self.logindatalog.info('database port is : --->%s<---' % str(database_port))
        except KeyError:
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(database_port)


if __name__ == '__main__':
    a = LoginData()
    # print(a.bossurl())
    # print(a.operation_login_username())
    # print(a.salesman_login_username())
    # print(a.salesman_login_username2())
    # print(a.salesman_login_username3())
    # print(a.number_administrator_login_username())
    # print(a.presale_login_username())
    # print(a.return_visit_login_username())
    # print(a.charging_login_username())
    # print(a.renewcontract_login_username())
    # print(a.productaudit_login_username())
    # print(a.productopening_login_username())
    # print(a.finance_login_username())
    # print(a.finance_login_username2())
    # print(a.ftersale_login_username())
    # print(a.zfw400_login_username())
    # print(a.zfw400_login_username2())
    # print(a.zfw400_login_username3())
    # print(a.zfwln_login_username())
    # print(a.zfwln_login_password())
    # print(a.verification_code())
    # print(a.database_ip())
    # print(a.database_username())
    # print(a.database_password())
    print(a.database_port())
    print(a.database_password())
