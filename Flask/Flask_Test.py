from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'hello world'

@app.route('/name/')
@app.route('/name/<name>')
def Name(name=None):
    return render_template('Flask_Test.html', name=name)

if __name__ == '__main__':
    # debug 调试支持，修改代码自动重新载入
    app.run(debug=True)