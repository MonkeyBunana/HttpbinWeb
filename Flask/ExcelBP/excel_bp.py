# -*- coding: utf-8 -*-
from flask import Blueprint, request
from Mysql.excel_sql import ExcelSql
from Requests.requests_sys_datas import SysDatas
from Mysql.excel_data_sql import ExcelDataSql
from  Mysql.excel_header_sql import ExcelHeaderSql
import json
# 创建一个蓝图对象
excel_bp = Blueprint('excel_bp', __name__, template_folder='../templates',)

@excel_bp.route('/datas', methods=['GET'])
def show_excel_all():
    result = ExcelSql().select_all()
    return json.dumps(result)


@excel_bp.route('/data', methods=['POST'])
@excel_bp.route('/data/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def restful_excel(id=0):
    """ tb_excelBean 表增删改差方法，采用 restful 规则设计
    :param id: PUT、DELETE表示被操作的ID，GET表示被查找的ID
    :return: GET方法返回查询到的数据，PUT、DELETE、PUT返回 {"message": "ok"}
    """
    kwargs = {
        "apiName": request.form["apiName"],
        "isRun": request.form["isRun"],
        "apiLevel": request.form["apiLevel"],
        "url": request.form["url"],
        "method": request.form["method"],
        "requestType": request.form["requestType"],
        "remark": request.form["remark"],

        "userToken": SysDatas().get_userToken(),
        "readerBarcode": request.form["readerBarcode"],
        "bookBarcode": request.form["bookBarcode"],
        "pageSize": request.form["pageSize"],
        "pageNumber": request.form["pageNumber"],
        "czid": request.form["czid"],
        "isSameCz": request.form["isSameCz"],

        "Accept": request.form["Accept"],
        "AcceptEncoding": request.form["AcceptEncoding"],
        "AcceptLanguage": request.form["AcceptLanguage"],
        "UserAgent": request.form["UserAgent"],
        "ContentType": request.form["ContentType"],
        "Connection": request.form["Connection"],
        "Host": request.form["Host"],
        "Origin": request.form["Origin"],
        "ContentLength": request.form["ContentLength"],
    }

    if request.method == 'GET':
        result = ExcelSql().select_id(id)
        return json.dumps(result)
    elif request.method == 'DELETE':
        ExcelSql().delete(id)
        return json.dumps({"message": "ok"})
    elif request.method == 'PUT':
        kwargs["id"] = id
        ExcelSql().update(**kwargs)
        return json.dumps({"message": "ok"})
    elif request.method == 'POST':
        eid = ExcelSql().add(**kwargs)
        kwargs["eid"] = eid
        ExcelDataSql().update(**kwargs)
        ExcelHeaderSql().update(**kwargs)
        return json.dumps({"message": "ok"})