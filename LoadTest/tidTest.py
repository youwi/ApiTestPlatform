import os
import sys
from threading import Timer

from locust import HttpLocust, TaskSet, task

sys.path.extend([os.getcwd()])

from Common.utils.DataMaker import DataMaker


class TidTest(TaskSet):
    list_out = []

    # 包含的主要任务和方法
    @task(3)
    def to_py_test(self):
        # 没有重复
        # TidTest.list_out.append(DataMaker.tid())
        # 有重复
        TidTest.list_out.append(DataMaker.tid_now())

    @staticmethod
    def printHello():
        # 检查重复
        new_list = list(set(TidTest.list_out))
        if len(TidTest.list_out) != len(new_list):
            print("!=")

    def on_start(self):
        Timer(3, TidTest.printHello).start()


class WebsiteUser(HttpLocust):
    task_set = TidTest
    min_wait = 5000
    max_wait = 9000
    host = "http://www.xxxxxxx.com"
