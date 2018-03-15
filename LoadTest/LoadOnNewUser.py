import os
import sys

from locust import HttpLocust, TaskSet, task

from Common.LoginGo import LoginGo

sys.path.extend([os.getcwd()])
from Common.HttpClient import HttpClient

"""
这是一个示例

假设以账号18912345678 运行性能测试(不考虑登陆的情况)
需要覆盖内置账号登陆信息来做性能测试.
"""


class LoadOnNewUserTest(TaskSet):

    @task(3)
    def to_py_test(self):
        return

    # 用新账号账号登陆
    @staticmethod
    def login18912345678():
        userName = {"mobile": "18912345678", "channel": "c", "password": "123456"}
        headers = {'author': '11', 'authorization': 'null'}
        from TestSuites import URL_XAUTH_C
        out = HttpClient.client.post(URL_XAUTH_C, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        return headers

    def on_start(self):
        # 使用性能测试的http测试工具,它已经封装了工具
        HttpClient.client = self.client
        # 一开始就覆盖内置账号的登陆信息!


class WebsiteUser(HttpLocust):
    task_set = LoadOnNewUserTest
    min_wait = 5000
    max_wait = 9000
    host = "http://www.xxxxxxx.com"
