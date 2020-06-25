# -*- coding: utf-8 -*-”
import json
import time
from Mysql.excel_sql import ExcelSql
from Mysql.excel_data_sql import ExcelDataSql
from Mysql.excel_header_sql import ExcelHeaderSql
from Common.operate_requests import RequestsData
from Mysql.excel_result_sql import ExcelResultSql

class SendRequests:

    def __init__(self):
        self.es = ExcelSql()
        self.eds = ExcelDataSql()
        self.ehs = ExcelHeaderSql()
        self.ers = ExcelResultSql()
        self.rd = RequestsData()

    def response(self, id):
        es_data = self.es.select_id(id)
        eds_data = self.eds.select_id(id)
        ehs_data = self.ehs.select_id(id)
        kwargs = {}

        res = self.rd.send_request(es_data["method"], es_data["url"], eds_data, ehs_data)
        kwargs["statusCode"] = res.status_code
        kwargs["message"] = json.loads(res.text)['message']
        kwargs["code"] = json.loads(res.text)['code']
        kwargs["time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        kwargs["eid"] = id

        self.ers.update(**kwargs)
        return {"message": "ok"}


if __name__ == "__main__":
    print(SendRequests().response("36"))