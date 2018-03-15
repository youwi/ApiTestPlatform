import re

import requests

"""
中间封装层!注意!
当做性能测试时客户端会被替换成性能测试的客户端
示例查看 LoadTest/example.py
默认直接使用requests.

"""


class HttpClient:
    client = requests

    """
    post请求,,
    参数是json
    返回结果是json
    """
    CACHE_HEADERS = None

    @staticmethod
    def POST(url, json):
        # 自动查找路径和登陆情况,判断角色
        from Common.utils.LoginGo import LoginGo
        from Common.utils.SwaggerURL import SwaggerURL
        url = re.sub('http://(.*?)/', LoginGo.LOCK_URL_CACHE, url)
        url = SwaggerURL.bind(HttpClient.parse_url(url), "POST")
        resp = HttpClient.client.post(url, json=json, headers=LoginGo.CACHE_LAST)
        if resp.status_code == 200:
            return resp.json()
        else:
            raise Exception("http code:" + str(resp.status_code))

    @staticmethod
    def GET(url, params=None):
        # 自动查找路径和登陆情况,判断角色
        from Common.utils.LoginGo import LoginGo
        from Common.utils.SwaggerURL import SwaggerURL
        url = SwaggerURL.bind(HttpClient.parse_url(url), "GET")
        resp = HttpClient.client.get(url, params=params, headers=LoginGo.CACHE_LAST)
        if resp.status_code == 200:
            return resp.json()
        else:
            raise Exception("http code:" + str(resp.status_code) + " >>" + url)

    @staticmethod
    def parse_url(url):
        if url.startswith("www"):
            return "http://" + url
        if url.startswith("http://") or url.startswith("https://"):
            return url
        from Common.utils.LoginGo import LoginGo
        return LoginGo.URL_BASE_C + url
