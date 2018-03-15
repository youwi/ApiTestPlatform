import json
import os

import sys
from datetime import datetime, date, timedelta
from threading import Timer
import time

import shutil

import pymysql
from flask import Flask
from flask import render_template, make_response

app = Flask(__name__, static_folder='', static_url_path='')

app.root_path = os.path.dirname(os.path.abspath(__file__))

HOST = "0.0.0.0"
PORT = 9094
INFO = "Test Report on " + HOST + ":" + str(PORT)
UPDATE_SHELL = "----"
HTML_RUN_SHELL = 'pytest --html="Reports/report-`date +%Y-%m-%d`.html"'
XML_RUN_SHELL = 'pytest --junitxml="Reports/report-`date +%Y-%m-%d`.xml"'
RUN_SHELL = 'pytest --html="Reports/report-`date +%Y-%m-%d`.html" --junitxml="Reports/report-`date +%Y-%m-%d`.xml"'

MYSQL_HOST = "192.168.8.13"
MYSQL_DB_NAME = "xxxxxxx.com"
MYSQL_USER_NAME = "123123123"
MYSQL_USER_PWD = "xxxxxxx.com123"
SMS_SQL = "select * from tablexxx order by id desc limit 25"

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


# 经过测试自更新重启是有效的,python编译过程慢一个过程
# 要重启2次,注: linux/max下重启是替换进程本身,pid不变.
# 不支持idea调试和参数太多的情况.
# 支持nohub python server.py
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


@app.route("/")
def home():
    return render_template("index.html")


CACHE = {
    "time": datetime.now(),
    "reports": [],
    "suites": []
}


def get_report_file_pix():
    return "Reports/report-" + date.today().strftime("%Y-%m-%d")


def get_report_file_full():
    return "Reports/report-" + datetime.now().strftime("%Y%m%d%H%M%S")


def run_pytest_by_type(shell=XML_RUN_SHELL):
    import subprocess
    out = ""
    process = subprocess.Popen(shell, stdout=subprocess.PIPE, shell=True)
    for line in iter(process.stdout.readline, ''):
        if line == b'':
            break
        out += str(line)

    return out


def run_pytest_as_xml():
    """
    获取测试报告列表,生成xml格式的报告
    """
    out = run_pytest_by_type(XML_RUN_SHELL)
    shutil.copy(get_report_file_pix() + ".xml", get_report_file_full() + ".xml")
    return out


def run_pytest_as_html():
    """
    获取测试报告列表,生成html格式的报告    pytest --html="Reports/report-`date +%Y-%m-%d`.html"

    """
    out = run_pytest_by_type(HTML_RUN_SHELL)
    shutil.copy(get_report_file_pix() + ".html", get_report_file_full() + ".html")
    return out


def run_pytest_by_file(file):
    out = run_pytest_by_type("pytest " + file)
    return out


def run_pytest():
    """
    获取测试报告列表,生成多份报告.

    """
    out = run_pytest_by_type(RUN_SHELL)
    shutil.copy(get_report_file_pix() + ".html", get_report_file_full() + ".html")
    shutil.copy(get_report_file_pix() + ".xml", get_report_file_full() + ".xml")
    return out


def auto_pull_git():
    os.system(UPDATE_SHELL)
    return True


def walk_reports():
    if CACHE['reports']:
        return CACHE['reports']
    cpath = os.path.dirname(os.path.abspath(__file__)) + "/Reports"
    dir = os.scandir(cpath)
    file_list = []
    for root, dirs, files in dir:
        for filepath in files:
            new_path = root.replace(cpath, "")
            file_list.append("" + os.path.join(new_path, filepath))
    # file_list = os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/Reports")
    response = make_response(json.dumps(file_list))
    response.headers["Content-type"] = "application/json"
    return response


def walk_suites():
    if CACHE['reports']:
        return CACHE['reports']
    cpath = os.path.dirname(os.path.abspath(__file__)) + "/Suites"
    dir = os.scandir(cpath)
    file_list = []
    for root, dirs, files in dir:
        for filepath in files:
            new_path = root.replace(cpath, "")
            file_list.append("Suites/" + os.path.join(new_path, filepath))
    # file_list = os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/Reports")
    response = make_response(json.dumps(file_list))
    response.headers["Content-type"] = "application/json"
    return response


@app.route('/report/list')
def report_list(name=None):
    # 应该使用walk()方法
    # https://www.python.org/dev/peps/pep-0471/
    if CACHE['reports']:
        return CACHE['reports']
    cpath = os.path.dirname(os.path.abspath(__file__)) + "/Reports"
    dir = os.scandir(cpath)
    file_list = []
    for obj in dir:
        if not obj.is_dir():
            file_list.append(obj.name)
    response = make_response(json.dumps(file_list))
    response.headers["Content-type"] = "application/json"
    return response


@app.route('/suites/list')
def suite_list(name=None):
    """
    获取文件列表按路径直接取出来
    """
    time.sleep(0.1)
    cpath = os.path.dirname(os.path.abspath(__file__)) + "/Suites"
    dir = os.walk(cpath)

    file_list = []
    for root, dirs, files in dir:
        for filepath in files:
            new_path = root.replace(cpath, "")
            file_list.append("Suites/" + os.path.join(new_path, filepath))

    file_list_new = filter(filter_file_type, file_list)

    filter_list = [item for item in file_list_new]
    return make_response(json.dumps(filter_list))


@app.route('/server/stop')
def server_stop():
    restart_program()
    raise RuntimeError('Server will stop.')


@app.route('/server/update')
def server_update():
    auto_pull_git()
    restart_program()


@app.route('/server/trun')
def run_all_test_case():
    return make_response(run_pytest())


@app.route('/server/runfile')
def run_test_by_file():
    from flask import request
    args = request.args
    file = args['file']
    return make_response(run_pytest_by_file(file))


@app.route('/server/trunhtml')
def run_all_test_case_html():
    return make_response(run_pytest_as_html())


@app.route('/sms/list')
def get_sms_last_list():
    db = pymysql.connect(MYSQL_HOST, MYSQL_USER_NAME, MYSQL_USER_PWD, MYSQL_DB_NAME,charset="utf8")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(SMS_SQL)
    map_data = cursor.fetchall()
    db.close()
    return make_response(json.dumps(map_data, cls=CJsonEncoder))


@app.route('/server/treport')
def get_today_test_report():
    """
    获取当天的测试报告,如果没有就运行一次.
    获取的报告为xml格式的.
    :return:
    """
    file_name = "Reports/report-" + date.today().strftime("%Y-%m-%d") + ".xml"
    run_pytest()
    datas = open(file_name).read()
    return make_response(datas)


def filter_file_type(name):
    """
    过滤文件类型,有些类型的文件不需要显示.
    """

    if name.endswith(".py") and not name.endswith("__init__.py"):
        # or name.endswith(".png") or name.endswith(".md"):
        return True
    else:
        return False


# 开启服务 wsgi标准
# 指定端口 pywsgi.WSGIServer((HOST, PORT), app, log=None).serve_forever()
if __name__ == '__main__':
    print(INFO)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    # app.config['DEBUG'] = True
    app.run(port=PORT, threaded=True, host=HOST)

# flask 如果不使用多线程,会同步阻塞,(chrome快速请求时出现!)
