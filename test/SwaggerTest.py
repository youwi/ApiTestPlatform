from unittest import TestCase

from Common.utils.SwaggerURL import SwaggerURL


class SwaggerTest(TestCase):

    @staticmethod
    def test_daa():
        assert "http://hr.xxxxxxx.com/event/{id}" == SwaggerURL.pure_back_url("http://hr.xxxxxxx.com/event/20171117")
        assert "http://www.xxxxxxx.com/api/biz/remind/count" == SwaggerURL.pure_back_url("http://www.xxxxxxx.com/api/biz/remind/count?_=1517293023231")
        assert "http://hr.xxxxxxx.com/{id}/event" == SwaggerURL.pure_back_url("http://hr.xxxxxxx.com/20171117/event")

    @staticmethod
    def test_save_file():
        SwaggerURL.save_swagger_to_file();
