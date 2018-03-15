from Common.HttpClient import HttpClient


class LoginGo(object):
    URL_XAUTH_CW = 'http://cw.xxxxxxx.com/api/biz/account/xauth'
    URL_XAUTH_HR = 'http://www.xxxxxxx.com/api/biz/account/xauth'
    URL_XAUTH_C = 'http://www.xxxxxxx.com/api/biz/account/xauth'
    URL_XAUTH_CRM = 'http://crm.xxxxxxx.com/api/biz/account/xauth'

    URL_BASE_CW = 'http://cw.xxxxxxx.com/api/biz'
    URL_BASE_HR = 'http://hr.xxxxxxx.com/api/biz'
    URL_BASE_C = 'http://www.xxxxxxx.com/api/biz'
    URL_BASE_CRM = 'http://crm.xxxxxxx.com/api/biz'

    URL_BASE_COMMON = 'http://www.xxxxxxx.com/api/c'
    URL_BASE_COMMON_C = 'http://www.xxxxxxx.com/api/c'
    URL_BASE_COMMON_CW = 'http://cw.xxxxxxx.com/api/c'
    URL_BASE_COMMON_HR = 'http://hr.xxxxxxx.com/api/c'
    URL_BASE_COMMON_CRM = 'http://crm.xxxxxxx.com/api/c'

    URL_FILE_UPLOAD = 'http://file.xxxxxxx.com'
    URL_QINIU = 'http://qiniu.xxxxxxx.com'

    # 登陆状态缓存,(性能测试时不需要重复登陆)
    # 如果需要更换登陆只需要提前设置这些变量就OK

    # 用于强制锁替换
    LOCK_URL_CACHE = "http://\\1/"

    # 最后一个登陆信息
    # 多线程要注意
    CACHE_LAST = None

    @staticmethod
    def login(mobile, pwd, channel='c'):
        userName = {"mobile": mobile, "channel": channel, "password": pwd}
        headers = {'author': 'xxx', 'authorization': 'null', "channel": channel}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_C, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def login_c(mobile, pwd):
        userName = {"mobile": mobile, "channel": "c", "password": pwd}
        headers = {'author': 'xxxx', 'authorization': 'null', "channel": "c"}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_C, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def login_cw(mobile, pwd):
        userName = {"mobile": mobile, "channel": "cw", "password": pwd}
        headers = {'author': 'xxx', 'authorization': 'null', "channel": "cw"}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_CW, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def login_crm(mobile, pwd, channel):
        userName = {"mobile": mobile, "channel": channel, "password": pwd}
        headers = {'author': 'xxxx', 'authorization': 'null', "channel": channel}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_CRM, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def login_hr(mobile, pwd):
        userName = {"mobile": mobile, "channel": "hr", "password": pwd}
        headers = {'author': 'xxx', 'authorization': 'null', "channel": "hr"}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_HR, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_LAST = headers
        return headers
