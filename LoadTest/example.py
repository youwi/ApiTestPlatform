import os
import sys

from locust import HttpLocust, TaskSet, task

sys.path.extend([os.getcwd()])
from Common.HttpClient import HttpClient

"""
这是一个示例
请在最上层目录运行脚本.(脚本中配置了当前路径)
运行:locust -f LoadTest/example.py
然后打开 http://127.0.0.1:8089 查看实时图表
![](./example.png)
![](./example.png)
注意: on_start方法
"""


class UserBehavior(TaskSet):

    # 包含的主要任务和方法
    @task(3)
    def to_py_test(self):
        TodoTest.test_get_todo_list()

    # 任务一开始执行的代码.
    def on_start(self):
        # 使用性能测试的http测试工具,它已经封装了工具
        HttpClient.client = self.client


"""
测试方案
UV:(web上填写)
Time:(永久)
Timeout:9s
"""


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
    host = "http://www.xxxxxxx.com"
