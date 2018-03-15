"""
用于重放HttpArchive文件
w3c标准:https://dvcs.w3.org/hg/webperf/raw-file/tip/specs/HAR/Overview.html
中文说明:http://weizhifeng.net/har-12-spec-chinese-edtion.html

测试需求:测试重放时不需要考虑登陆/Cookie返回信息都要过滤

"""
import json

import os


class HarReplay:

    @staticmethod
    def test():
        return True

    @staticmethod
    def replay_ignore_headers():
        """
           重放不包含请求头,通常用来忽略Cookie和登陆信息
       """
        # //TODO
        return True

    @staticmethod
    def replay_ignore_response():
        """
           不验证返回结果
           只验证错误码 httpCode!=200
           (200状态,code>0 或error>0 或 msg!=null 算错误)
       """
        # //TODO
        return True

    @staticmethod
    def read_har_file():
        """读取HRA文件"""
        # //TODO
        return True


class JsonReplay:
    """

    replay json as body
    把json数据按body传过去,注不考虑返回值,只适合组装.
    """

    @staticmethod
    def read_json_file(script_file_name, data_file_name):
        """
        注意是:由于是相对路径 脚本名称, __file__
        自动处理相对路径.
        返回json
        """
        f = open(os.path.dirname(os.path.abspath(script_file_name)) + "/" + data_file_name, encoding='utf-8')
        return json.load(f)
