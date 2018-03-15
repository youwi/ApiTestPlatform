from unittest import TestCase

from Common.Assertion import Assertion
from Common.HttpClient import HttpClient


class Http500Test(TestCase):

    @staticmethod
    def test_daa():
        # 401
        try:
            resp = HttpClient.client.post("http://www.xxxxxxx.com/api/biz/todo", json={}, headers={})
            Assertion.check(resp)
            json = resp.json()
        except Exception:
            return True
        assert False
        # AssertionError("")

    @staticmethod
    def test_404():
        # 404
        try:
            resp = HttpClient.client.post("http://www.xxxxxxx.com/api/biz/todo2", json={}, headers={})
            Assertion.check(resp)
        except Exception:
            return True
        assert False
        # AssertionError("")
