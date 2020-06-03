from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import os
from werkzeug.utils import secure_filename
from Common.test import test

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'hello world'

@app.route('/name/')
@app.route('/name/<name>')
def Name(name=None):
    return render_template('Flask_Test.html', name=name)

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        upload_path = os.path.join(basepath, "../Resources/File", secure_filename(f.filename))
        f.save(upload_path)
        return redirect(url_for('message'))
    return render_template('Flask_Upload.html')

@app.route('/message', methods=['GET'])
def message():
    return render_template('Flask_Message.html', text=test().test_send_request())

if __name__ == '__main__':
    # debug 调试支持，修改代码自动重新载入
    app.run(debug=True)