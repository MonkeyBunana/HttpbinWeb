# -*- coding: utf-8 -*-
from flask import Blueprint
from Requests.requests_mysql import SendRequests


# 创建一个蓝图对象
request_bp = Blueprint('request_bp', __name__, template_folder='../templates', )


@request_bp.route('/request/run/<int:id>', methods=['GET'])
def send_request(id):
    return SendRequests().response(str(id))



