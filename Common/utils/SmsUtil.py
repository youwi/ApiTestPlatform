# encoding:utf-8
from Common.utils.LoginGo import LoginGo
from Suites import Swagger, URL_FILE_UPLOAD, POST, jsonContain, GET
from Common.utils.HttpClient import HttpClient


class SmsUtil(object):
    headers = None

    @staticmethod
    def get_sms(mobile, option=None):
        # 获取短信验证码的接口,手机号必须
        # verifyCode?mobile = 18888888881 & smsOp = 4
        # // VC = 1; // 申请注册验证码
        # // MD = 2; // 修改绑定手机验证码
        # // MDPWD = 3; // 修改密码验证码
        # // LOGIN = 4; // 登录验证码
        # // VC_DRAW_APPLY = 11; // 申请提现验证码
        # google.protobuf.Int32Value
        # smsOp = 2;
        json = GET("www.xxxxxxx.com/api/c/verifyCode", {"mobile": mobile, "smsOp": option})
        return json['body']

