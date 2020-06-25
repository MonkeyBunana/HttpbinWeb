from Common.operate_mysql import Database
from Requests.requests_sys_datas import SysDatas

class ExcelDataSql:

    def __init__(self):
        self.conn = Database().conn()

    def update(self, **kwargs):
        try:
            with self.conn.cursor() as cursor:
                sql = "UPDATE tb_excel_data SET userToken = %s, readerBarcode = %s, bookBarcode = %s, " \
                      "pageSize = %s, pageNumber = %s, czid = %s, isSameCz = %s " \
                      "WHERE eid = %s"
                values = (
                    kwargs.get('userToken'), kwargs.get('readerBarcode'), kwargs.get('bookBarcode'),
                    kwargs.get('pageSize'), kwargs.get('pageNumber'), kwargs.get('czid'), kwargs.get('isSameCz'),
                    kwargs.get('eid')
                )
                cursor.execute(sql, values)
                self.conn.commit()
        # except:
        #     self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()

    def update_type(self, fieldType, eid, value):
        try:
            with self.conn.cursor() as cursor:
                sql = "UPDATE tb_excel_data SET " + fieldType + " = %s WHERE eid =" + eid
                cursor.execute(sql, value)
                self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()

    def select_type(self, fieldType, eid):
        try:
            with self.conn as cursor:
                # value 为 数据库字段名，想查哪个字段的值就放哪个字段
                sql = "SELECT " + fieldType + " FROM tb_excel_data WHERE eid =" + eid
                cursor.execute(sql)
                result = cursor.fetchone()
                return result
        finally:
            self.conn.close()

    def select_id(self, eid):
        try:
            with self.conn as cursor:
                # value 为 数据库字段名，想查哪个字段的值就放哪个字段
                sql = "SELECT * FROM tb_excel_data WHERE eid =" + eid
                cursor.execute(sql)
                result = cursor.fetchone()
                return result
        finally:
            self.conn.close()

if __name__ == "__main__":
    print(ExcelDataSql().update_type('userToken', "23", SysDatas().get_userToken()))