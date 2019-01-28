# !/usr/local/python
# -*- coding: UTF-8 -*-
import MySQLdb
from data.InitConnect import ConnectSql


class BusinessData(ConnectSql):
    def __init__(self):
        ConnectSql.__init__(self)
        self.conn_mongo = self.connectmongo()
        self.db = self.conn_mongo['autotest']
        self.collection = self.db['sys_connectinfo']
        self.collection_set = self.collection.find({"_id": 0})
        self.collection2 = self.db['sys_businessdata']
        # 获取mysql数据库连接信息
        mysql_host = self.collection_set[0]['database_ip']
        mysql_user = self.collection_set[0]['database_username']
        mysql_passwd = self.collection_set[0]['database_password']
        mysql_port = self.collection_set[0]['database_port']
        # 连接mysql数据库
        conn = MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, port=int(mysql_port),
                               charset='utf8')
        self.cur = conn.cursor()

    def num400exists(self):
        try:
            number = self.collection2.find_one({"_id": 0}, {"num400": 1})['num400']
        except TypeError:
            number = 4000002193

        # 从数据库中查询400号码是否已被占用
        while True:
            sql = "SELECT * FROM xtboss.sys_numadmin WHERE number400 LIKE '%" + str(number) + "%';"
            self.cur.execute(sql)
            result = self.cur.fetchall()
            if () == result:
                self.collection2.update_one({"_id": 0}, {'$set': {"num400": str(number)}})
                break
            else:
                number = int(number) + 1
        return number


if __name__ == '__main__':
    a = BusinessData()
    print(a.num400exists())
