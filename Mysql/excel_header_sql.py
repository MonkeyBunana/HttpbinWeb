from Common.operate_mysql import Database

class ExcelHeaderSql:

    def __init__(self):
        self.conn = Database().conn()

    def update(self, **kwargs):
        try:
            with self.conn.cursor() as cursor:
                sql = "UPDATE tb_excel_header SET Accept = %s, AcceptEncoding = %s, AcceptLanguage = %s, " \
                      "UserAgent = %s, ContentType = %s, Connection = %s, Host = %s , Origin = %s, ContentLength = %s" \
                      "WHERE eid = %s"
                values = (
                    kwargs.get('Accept'), kwargs.get('AcceptEncoding'), kwargs.get('AcceptLanguage'),
                    kwargs.get('UserAgent'), kwargs.get('ContentType'), kwargs.get('Connection'), kwargs.get('Host'),
                    kwargs.get('Origin'), kwargs.get('ContentLength'), kwargs.get('eid')
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
                sql = "UPDATE tb_excel_header SET " + fieldType + " = %s WHERE eid =" + eid
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
                sql = "SELECT " + fieldType + " FROM tb_excel_header WHERE eid =" + eid
                cursor.execute(sql)
                result = cursor.fetchone()
                return result
        finally:
            self.conn.close()

    def select_id(self, eid):
        try:
            with self.conn as cursor:
                # value 为 数据库字段名，想查哪个字段的值就放哪个字段
                sql = "SELECT * FROM tb_excel_header WHERE eid =" + eid
                cursor.execute(sql)
                result = cursor.fetchone()
                return result
        finally:
            self.conn.close()

if __name__ == "__main__":
    # ExcelHeaderSql().update('ContentLength', '21', '63')
    print(ExcelHeaderSql().select('UserAgent', '21'))