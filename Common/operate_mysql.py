#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python连接到 MySQL 数据库及相关操作(基于Python3)"""
import pymysql.cursors
from Common.operate_ini import ReadConfig


class Database:

    def __init__(self):
        self.connection = pymysql.connect(
            host=ReadConfig().getValue(section='mysql', name='host'),
            port=int(ReadConfig().getValue(section='mysql', name='port')),
            user=ReadConfig().getValue(section='mysql', name='user'),
            password=ReadConfig().getValue(section='mysql', name='pwd'),
            db=ReadConfig().getValue(section='mysql', name='db'),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )

    def conn(self):
        return self.connection

#     def select_all(self):
#         try:
#             with self.connection.cursor() as cursor:
#                 sql = "SELECT * FROM tb_excel"
#                 cursor.execute(sql)
#                 result = cursor.fetchall()
#                 return result
#         finally:
#             self.connection.close()
#
#     def select_id(self, id):
#         try:
#             with self.connection.cursor() as cursor:
#                 sql = "SELECT * FROM tb_excel WHERE id = %s"
#                 cursor.execute(sql, id)
#                 result = cursor.fetchone()
#                 return result
#         finally:
#             self.connection.close()
#
#     def add(self, **kwargs):
#         try:
#             with self.connection.cursor() as cursor:
#                 sql = "INSERT INTO " \
#                       "tb_excel(apiName, isRun, apiLevel, url, method, headers, requestType, requestData, remark)" \
#                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
#                 values = (
#                     kwargs.get('apiName'), kwargs.get('isRun'), kwargs.get('apiLevel'),
#                     kwargs.get('url'), kwargs.get('method'), kwargs.get('headers'),
#                     kwargs.get('requestType'), kwargs.get('requestData'), kwargs.get('remark')
#                 )
#                 cursor.execute(sql, values)
#                 self.connection.commit()
#         except:
#             self.connection.rollback()
#         finally:
#             cursor.close()
#             self.connection.close()
#
#     def delete(self, id):
#         try:
#             with self.connection.cursor() as cursor:
#                 sql = "DELETE FROM tb_excel WHERE id = %s"
#                 cursor.execute(sql, id)
#                 self.connection.commit()
#         except:
#             self.connection.rollback()
#         finally:
#             cursor.close()
#             self.connection.close()
#
#     def updata(self, **kwargs):
#         try:
#             with self.connection.cursor() as cursor:
#                 sql = "UPDATE tb_excel SET apiName = %s, isRun = %s, apiLevel = %s, " \
#                       "url = %s, method = %s, headers = %s, requestType = %s, requestData = %s, remark = %s " \
#                       "WHERE id = %s"
#                 values = (
#                     kwargs.get('apiName'), kwargs.get('isRun'), kwargs.get('apiLevel'), kwargs.get('url'),
#                     kwargs.get('method'), kwargs.get('headers'), kwargs.get('requestType'), kwargs.get('requestData'),
#                     kwargs.get('remark'), kwargs.get('id')
#                 )
#                 cursor.execute(sql, values)
#                 self.connection.commit()
#         except:
#             self.connection.rollback()
#         finally:
#             cursor.close()
#             self.connection.close()
#
#
# if __name__ == '__main__':
#     # Database().select_all()
#     a = {"apiName": "1", "isRun": "1", "apiLevel": "1", "url": "1", "method": "1", "headers": "1", "requestType": "1", "requestData": "1", "remark": "1"}
#     Database().add(**a)
#     # Database().select_all()
#     # Database().delete("1")
#     # Database().select_id("1")
#     # a = {"apiName": "2", "isRun": "2", "apiLevel": "2", "url": "2", "method": "2", "headers": "2", "requestType": "2",
#     #      "requestData": "2", "remark": "2", "id": "7"}
#     # Database().updata(**a)
