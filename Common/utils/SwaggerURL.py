import re

import requests


class SwaggerURL(object):
    URL_XAUTH_CW = 'http://cw.lieluobo.testing/api/biz/account/xauth'
    URL_XAUTH_HR = 'http://www.lieluobo.testing/api/biz/account/xauth'
    URL_XAUTH_C = 'http://www.lieluobo.testing/api/biz/account/xauth'
    URL_XAUTH_CRM = 'http://crm.lieluobo.testing/api/biz/account/xauth'

    URL_COUNT = {}
    LAST_URL = ""

    # 自动封装url对应到swagger文档.
    def __init__(self, s):
        return s

    # 自动封装url对应到swagger文档.
    @staticmethod
    def bind(ori_url, method="POST"):
        SwaggerURL.LAST_URL = ori_url
        method_url = "{}:{}".format(method.upper(), SwaggerURL.pure_back_url(ori_url))
        if not hasattr(SwaggerURL.URL_COUNT, method_url):
            SwaggerURL.URL_COUNT[method_url] = 1
        else:
            SwaggerURL.URL_COUNT[method_url] = SwaggerURL.URL_COUNT[method_url] + 1

        return ori_url

    @staticmethod
    def get_swagger_json():
        # TODO
        return True

    @staticmethod
    def pure_back_url(url):
        """
           把url进行还原操作,如
           http://abc.com?abc  ->http://abc.com
           http://abc.com/abc?abc  ->http://abc.com/abc
           http://abc.com/abc/123?abc  ->http://abc.com/abc/{id}
           http://abc.com/abc/123?abc  ->http://abc.com/abc/{id}
           http://hr.lieluobo.testing/20171117/event-->http://hr.lieluobo.testing/{id}/event
           """
        # TODO
        if url is None:
            return None

        new_url = url.split("?")[0]

        regex = re.compile(r"/\d+")
        match = regex.search(url)
        if match:
            new_url = new_url.replace(match.group(), "/{id}")
        return new_url

    @staticmethod
    def save_swagger_to_file():
        import json
        import os
        if len(SwaggerURL.URL_COUNT) <= 1:
            return
        o_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, "..", "Reports", "SwaggerMatch.json"))

        with open(o_path, "w") as fp:
            json.dump(SwaggerURL.URL_COUNT, fp)

        SwaggerURL.sync_to_yoda()

    @staticmethod
    def sync_to_yoda():
        # 同步数据信息到同步服务器
        # 按3个分类来做.
        p_cw = "http://172.16.52.181:8101/39"
        p_c = "http://172.16.52.181:8101/66"
        p_hr = "http://172.16.52.181:8101/67"
        from Suites import GET

        uc_cw = GET(p_cw)
        uc_c = GET(p_c)
        uc_hr = GET(p_hr)

        uc_cw_new = {}
        uc_c_new = {}
        uc_hr_new = {}

        key_c = "http://www.lieluobo.testing/api/biz"
        key_crm = "http://crm.lieluobo.testing/api/biz"
        key_cw = "http://crm.lieluobo.testing/api/biz"
        key_hr = "http://crm.lieluobo.testing/api/biz"
        key_http = "http://"

        for (key, value) in SwaggerURL.URL_COUNT.items():
            key = key.replace("POST:", "post:")
            key = key.replace("GET:", "get:")

            if key_c in key:
                uc_c_new[key.replace(key_c, "")] = 2
            if key_crm in key:
                uc_cw_new[key.replace(key_crm, "")] = 2
            if key_cw in key:
                uc_cw_new[key.replace(key_cw, "")] = 2
            if key_hr in key:
                uc_hr_new[key.replace(key_hr, "")] = 2
            if key_http not in key:
                uc_c_new[key] = 2

        from Suites import POST

        uc_cw_new.update(uc_cw)
        uc_c_new.update(uc_c)
        uc_hr_new.update(uc_hr)

        POST(p_cw, uc_cw_new)
        POST(p_c, uc_c_new)
        POST(p_hr, uc_hr_new)

        return
