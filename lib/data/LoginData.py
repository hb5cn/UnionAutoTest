# !/usr/local/python
# -*- coding: UTF-8 -*-
from data.InitConnect import ConnectSql
import traceback


class LoginData(ConnectSql):
    def __init__(self):
        ConnectSql.__init__(self)
        self.logindatalog = self.logging.getLogger('LoginData')
        self.logindatalog.addHandler(self.logscr)
        self.conn_mongo = self.connectmongo()
        self.db = self.conn_mongo['autotest']
        self.collection = self.db['sys_connectinfo']
        self.mongo_id = 0
        self.collection_set = self.collection.find({'_id': self.mongo_id})

    def bossurl(self):
        # 查询要登录的boss的地址
        boss_url = ''
        try:
            boss_url = self.collection_set[0]['bossurl']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return boss_url

    def operation_login_username(self):
        # 查询要登录的运维的帐号
        operation_login_username = ''
        try:
            operation_login_username = self.collection_set[0]['operation_login_username']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return operation_login_username

    def salesman_login_username(self):
        # 查询要登录的销售的帐号1
        salesman_login_username = ''
        try:
            salesman_login_username = self.collection_set[0]['salesman_login_username']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return salesman_login_username

    def salesman_login_username2(self):
        # 查询要登录的销售的帐号2
        salesman_login_username2 = ''
        try:
            salesman_login_username2 = self.collection_set[0]['salesman_login_username2']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return salesman_login_username2

    def salesman_login_username3(self):
        # 查询要登录的销售的帐号3
        salesman_login_username3 = ''
        try:
            salesman_login_username3 = self.collection_set[0]['salesman_login_username3']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return salesman_login_username3

    def number_administrator_login_username(self):
        # 查询要登录的号码管理员的帐号
        number_administrator_login_username = ''
        try:
            number_administrator_login_username = self.collection_set[0]['number_administrator_login_username']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return number_administrator_login_username

    def presale_login_username(self):
        # 查询要登录的售前的帐号
        presale_login_username = ''
        try:
            presale_login_username = self.collection_set[0]['presale_login_username']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return presale_login_username

    def return_visit_login_username(self):
        # 查询要登录的回访的帐号
        return_visit_login_username = ''
        try:
            return_visit_login_username = self.collection_set[0]['return_visit_login_username']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return return_visit_login_username

    def charging_login_username(self):
        # 查询要登录的计费的帐号
        charging_login_username = ''
        try:
            charging_login_username = self.collection_set[0]['charging_login_username']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return charging_login_username

    def renewcontract_login_username(self):
        # 查询要登录的续约的帐号
        renewcontract_login_username = ''
        try:
            renewcontract_login_username = self.collection_set[0]['renewcontract_login_username']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return renewcontract_login_username

    def productaudit_login_username(self):
        # 查询要登录的产品审核的帐号
        productaudit_login_username = ''
        try:
            productaudit_login_username = self.collection_set[0]['productaudit_login_username']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return productaudit_login_username

    def productopening_login_username(self):
        # 查询要登录的产品开户的帐号
        productopening_login_username = ''
        try:
            productopening_login_username = self.collection_set[0]['productopening_login_username']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return productopening_login_username

    def finance_login_username(self):
        # 查询要登录的财务开户的帐号
        finance_login_username = ''
        try:
            finance_login_username = self.collection_set[0]['finance_login_username']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return finance_login_username

    def finance_login_username2(self):
        # 查询要登录的财务开户的帐号2
        finance_login_username2 = ''
        try:
            finance_login_username2 = self.collection_set[0]['finance_login_username2']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return finance_login_username2

    def ftersale_login_username(self):
        # 查询要登录的售后的帐号
        ftersale_login_username = ''
        try:
            ftersale_login_username = self.collection_set[0]['ftersale_login_username']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return ftersale_login_username

    def zfw400_login_username(self):
        # 查询要登录自服务的400帐号
        zfw400_login_username = ''
        try:
            zfw400_login_username = self.collection_set[0]['zfw400_login_username']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(zfw400_login_username)

    def zfw400_login_username2(self):
        # 查询要登录自服务的400帐号2
        zfw400_login_username2 = ''
        try:
            zfw400_login_username2 = self.collection_set[0]['zfw400_login_username2']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(zfw400_login_username2)

    def zfw400_login_username3(self):
        # 查询要登录自服务的400帐号3
        zfw400_login_username3 = ''
        try:
            zfw400_login_username3 = self.collection_set[0]['zfw400_login_username3']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(zfw400_login_username3)

    def zfwln_login_username(self):
        # 查询要登录自服务的LN帐号
        zfwln_login_username = ''
        try:
            zfwln_login_username = self.collection_set[0]['zfwln_login_username']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(zfwln_login_username)

    def zfwln_login_password(self):
        # 查询要登录自服务的LN密码
        zfwln_login_password = ''
        try:
            zfwln_login_password = self.collection_set[0]['zfwln_login_password']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(zfwln_login_password)

    def login_password(self):
        # 查询要登录boss的密码
        login_password = ''
        try:
            login_password = self.collection_set[0]['login_password']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(login_password)

    def verification_code(self):
        # 查询要登录boss的验证码
        verification_code = ''
        try:
            verification_code = self.collection_set[0]['verification_code']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(verification_code)

    def database_ip(self):
        # 查询boss的数据库ip地址
        database_ip = ''
        try:
            database_ip = self.collection_set[0]['database_ip']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(database_ip)

    def database_username(self):
        # 查询boss的数据库连接用户名
        database_username = ''
        try:
            database_username = self.collection_set[0]['database_username']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(database_username)

    def database_password(self):
        # 查询boss的数据库连接密码
        database_password = ''
        try:
            database_password = self.collection_set[0]['database_password']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(database_password)

    def database_port(self):
        # 查询boss的数据库端口
        database_port = ''
        try:
            database_port = self.collection_set[0]['database_port']
        except (KeyError, TypeError):
            self.logindatalog.error(traceback.format_exc())
            self.conn_mongo.close()
        return str(database_port)


# if __name__ == '__main__':
#     a = LoginData()
#     print(a.bossurl())
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
    # print(a.database_port())
