from unittest import TestCase

# 这里不允许写脚本. 要求:所有测试代码放到函数中.
from Common.utils.HttpReplay import HarReplay
from Common.utils.LoginGo import LoginGo
from Suites import POST, jsonContain


class TodoTestRemindList(TestCase):

    @staticmethod
    def test_get_remind_list():
        """
           获取提醒列表的测试示例
           这里使用了 HarReplay 的方法
           直接重放json文件,
           注意:重放方法不处理登陆信息,所以登陆还是要自己来.
        """
        # TODO 未完成
        # 登陆
        LoginGo.hr19900020002()
        # 重放请求.
        HarReplay.test()

    def setUp(self):
        LoginGo.c19900030001()

    @staticmethod
    def test_short():
        LoginGo.c19900030001()
        data = {
            "startedAt": "2017-12-25T00:00:00+08:00",
            "endedAt": "2018-01-08T00:00:00+08:00",
            "uid": 149984216387509
        }
        json = POST("/todo/list", data)
        jsonContain(json, {"code": 0})
