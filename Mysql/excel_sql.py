from Common.operate_mysql import Database

class ExcelSql:

    def __init__(self):
        self.conn = Database().conn()

    def select_all(self):
        try:
            with self.conn as cursor:
                sql = "SELECT * FROM tb_excel"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        finally:
            self.conn.close()

    def select_id(self, id):
        try:
            with self.conn.cursor() as cursor:
                sql = "SELECT * FROM tb_excel WHERE id = %s"
                cursor.execute(sql, id)
                result = cursor.fetchone()
                return result
        finally:
            self.conn.close()

    def add(self, **kwargs):
        try:
            with self.conn.cursor() as cursor:
                sql = "INSERT INTO " \
                      "tb_excel(apiName, isRun, apiLevel, url, method, requestType, remark)" \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (
                    kwargs.get('apiName'), kwargs.get('isRun'), kwargs.get('apiLevel'), kwargs.get('url'),
                    kwargs.get('method'), kwargs.get('requestType'),  kwargs.get('remark')
                )
                cursor.execute(sql, values)
                # 获取 tb_excel 的 id，添加到 tb_excel_data 中
                eid = cursor.lastrowid
                cursor.execute("INSERT INTO tb_excel_data(eid) VALUES (%s)", eid)
                cursor.execute("INSERT INTO tb_excel_header(eid) VALUES (%s)", eid)
                cursor.execute("INSERT INTO tb_excel_result(eid) VALUES (%s)", eid)
                self.conn.commit()
                return eid
        except:
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()

    def delete(self, id):
        try:
            with self.conn.cursor() as cursor:
                sql = "DELETE FROM tb_excel WHERE id = %s"
                cursor.execute(sql, id)
                # 删除 tb_excel 中的数据时，顺手把 tb_excel_data 中的数据删除
                cursor.execute("DELETE FROM tb_excel_data WHERE eid = %s", id)
                cursor.execute("DELETE FROM tb_excel_header WHERE eid = %s", id)
                cursor.execute("DELETE FROM tb_excel_result WHERE eid = %s", id)
                self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()

    def update(self, **kwargs):
        try:
            with self.conn.cursor() as cursor:
                sql = "UPDATE tb_excel SET apiName = %s, isRun = %s, apiLevel = %s, " \
                      "url = %s, method = %s, requestType = %s, remark = %s " \
                      "WHERE id = %s"
                values = (
                    kwargs.get('apiName'), kwargs.get('isRun'), kwargs.get('apiLevel'), kwargs.get('url'),
                    kwargs.get('method'), kwargs.get('requestType'), kwargs.get('remark'), kwargs.get('id')
                )
                cursor.execute(sql, values)
                self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()


if __name__ == "__main__":
    # ExcelSql().updata_token("111", "1")
    a = {"apiName": "Elib_reader", "isRun": "Y", "apiLevel": "L2",
         "url": "http://192.168.1.47:8080/service/api/e/flow/doclx/reader",
         "method": "POST", "requestType": "FORM", "remark": "这是一个Elib的post测试，获取读者证信息"}
    ExcelSql().add(**a)
    # ExcelSql().delete("20")