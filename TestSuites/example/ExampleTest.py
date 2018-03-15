from unittest import TestCase

from TestSuites import POST, jsonContain
from Common.LoginGo import LoginGo


class ExampleTest(TestCase):

    def setup_class(self):
        LoginGo.login_c("", "")
        return

    @staticmethod
    def test_short():
        """
        这是一个标准示例
        :return:
        """
        data = {
            "startedAt": "2017-12-25T00:00:00+08:00",
            "endedAt": "2018-01-08T00:00:00+08:00",
            "uid": 149984216387509
        }

        json = POST("/todo/list", data)
        assert jsonContain(json, {"code": 0})
