# -*- coding: utf-8 -*-
from flask import Blueprint, request, abort

from Common.operate_mysql import Database
import json
# 创建一个蓝图对象
excel_bp = Blueprint('excel', __name__, template_folder='../templates',)

@excel_bp.route('/data', methods=['GET', 'POST'])
def show_excel_all():
    if request.method == 'GET':
        result = Database().select_all()
        return json.dumps(result)
    elif request.method == 'POST':
        kwargs = {
            "apiName": request.form["apiName"],
            "isRun": request.form["isRun"],
            "apiLevel": request.form["apiLevel"],
            "url": request.form["url"],
            "method": request.form["method"],
            "headers": request.form["headers"],
            "requestType": request.form["requestType"],
            "requestData": request.form["requestData"],
            "remark": request.form["remark"],
        }
        Database().add(**kwargs)
        return json.dumps({"message": "ok"})


@excel_bp.route('/data/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def restful_excel(id):
    if request.method == 'GET':
        result = Database().select_id(id)
        return json.dumps(result)
    elif request.method == 'DELETE':
        Database().delete(id)
        return json.dumps({"message": "ok"})
    elif request.method == 'PUT':
        kwargs = {
            "apiName": request.form["apiName"],
            "isRun": request.form["isRun"],
            "apiLevel": request.form["apiLevel"],
            "url": request.form["url"],
            "method": request.form["method"],
            "headers": request.form["headers"],
            "requestType": request.form["requestType"],
            "requestData": request.form["requestData"],
            "remark": request.form["remark"],
            "id": id
        }
        Database().updata(**kwargs)
        return json.dumps({"message": "ok"})