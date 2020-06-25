# -*- coding: utf-8 -*-
from flask import Flask, render_template

from Flask.ExcelBP.excel_bp import excel_bp
from Flask.RequestsBP.requests_bp import request_bp

app = Flask(__name__)
app.secret_key = 'The quick brown fox jumps over the lazy dog'
# 注册蓝图
app.register_blueprint(excel_bp)
app.register_blueprint(request_bp)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5200, debug=True)