# encoding: utf-8
import os

from Common.utils.SwaggerURL import SwaggerURL

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

DATA_PATH = os.path.join(ROOT_PATH, "TestData")

from Common.utils.Assertion import Assertion
from Common.utils.HttpClient import HttpClient
from Common.utils.LoginGo import LoginGo
from Common.utils.DataMaker import DataMaker


def get_data_abspath(data_path: object) -> object:
    """
    get data abspath by join DATA_PATH
    
    usage:
    
        get_data_abspath("test.txt")
        get_data_abspath("dir1/test.txt")
        get_data_abspath("dir1/dir2/test.txt")
    
    :param data_path: string
    :return: abspath
    """
    return os.path.join(DATA_PATH, data_path)


# 导出方法,现在把断言中的工具导出到这里,以方便使用.
jsonContain = Assertion.jsonContain

POST = HttpClient.POST
GET = HttpClient.GET

URL_XAUTH_CW = LoginGo.URL_XAUTH_CW
URL_XAUTH_HR = LoginGo.URL_XAUTH_HR
URL_XAUTH_C = LoginGo.URL_XAUTH_C
URL_XAUTH_CRM = LoginGo.URL_XAUTH_CRM

URL_BASE_CW = LoginGo.URL_BASE_CW
URL_BASE_HR = LoginGo.URL_BASE_HR
URL_BASE_C = LoginGo.URL_BASE_C
URL_BASE_CRM = LoginGo.URL_BASE_CRM

URL_BASE_COMMON = LoginGo.URL_BASE_COMMON
URL_BASE_COMMON_C = LoginGo.URL_BASE_COMMON_C
URL_BASE_COMMON_CW = LoginGo.URL_BASE_COMMON_CW
URL_BASE_COMMON_HR = LoginGo.URL_BASE_COMMON_HR
URL_BASE_COMMON_CRM = LoginGo.URL_BASE_COMMON_CRM

URL_FILE_UPLOAD = LoginGo.URL_FILE_UPLOAD

URL_QINIU = LoginGo.URL_QINIU

Swagger = SwaggerURL.bind

TPL_TIME = DataMaker.TPL_TIME