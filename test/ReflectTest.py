
"""
反射测试
"""
from unittest import TestCase


class TestReflect(TestCase):

    def test_on_methods(self):
        from Suites.数据分离示例.test_remind_list_example import TodoTestRemindList
        TodoTestRemindList.test_short()
