from Common.operate_mysql import Database
from Mysql.excel_sql import ExcelSql

class ExcelResultSql:

    def __init__(self):
        self.conn = Database().conn()
        self.excel = ExcelSql()

    def update(self, **kwargs):
        try:
            with self.conn.cursor() as cursor:
                sql = "UPDATE tb_excel_result SET statusCode = %s, message = %s, code = %s, time = %s WHERE eid = %s"
                values = (
                    kwargs.get("statusCode"), kwargs.get("message"), kwargs.get("code"),
                    kwargs.get("time"), kwargs.get("eid")
                )
                cursor.execute(sql, values)
                self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()

    def update_type(self, fieldType, eid, value):
        try:
            with self.conn.cursor() as cursor:
                sql = "UPDATE tb_excel_result SET " + fieldType + " = %s WHERE eid =" + eid
                cursor.execute(sql, value)
                self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()

    def select(self, fieldType, eid):
        try:
            with self.conn as cursor:
                # value 为 数据库字段名，想查哪个字段的值就放哪个字段
                sql = "SELECT " + fieldType + " FROM tb_excel_result WHERE eid =" + eid
                cursor.execute(sql)
                result = cursor.fetchone()
                return result
        finally:
            self.conn.close()

if __name__ == '__main__':
    print()
