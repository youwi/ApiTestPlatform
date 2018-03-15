from Common.utils.HttpClient import HttpClient


class LoginGo(object):
    URL_XAUTH_CW = 'http://cw.lieluobo.testing/api/biz/account/xauth'
    URL_XAUTH_HR = 'http://www.lieluobo.testing/api/biz/account/xauth'
    URL_XAUTH_C = 'http://www.lieluobo.testing/api/biz/account/xauth'
    URL_XAUTH_CRM = 'http://crm.lieluobo.testing/api/biz/account/xauth'

    URL_BASE_CW = 'http://cw.lieluobo.testing/api/biz'
    URL_BASE_HR = 'http://hr.lieluobo.testing/api/biz'
    URL_BASE_C = 'http://www.lieluobo.testing/api/biz'
    URL_BASE_CRM = 'http://crm.lieluobo.testing/api/biz'

    URL_BASE_COMMON = 'http://www.lieluobo.testing/api/c'
    URL_BASE_COMMON_C = 'http://www.lieluobo.testing/api/c'
    URL_BASE_COMMON_CW = 'http://cw.lieluobo.testing/api/c'
    URL_BASE_COMMON_HR = 'http://hr.lieluobo.testing/api/c'
    URL_BASE_COMMON_CRM = 'http://crm.lieluobo.testing/api/c'

    URL_FILE_UPLOAD = 'http://file.testing.lieluobo.net'
    URL_QINIU = 'https://i.jihui.io'

    # 登陆状态缓存,(性能测试时不需要重复登陆)
    # 如果需要更换登陆只需要提前设置这些变量就OK
    CACHE_19900020002 = None
    CACHE_19900000002 = None
    CACHE_19900030001 = None
    CACHE_19912345678 = None
    CACHE_19900000011 = None
    CACHE_15900000001 = None
    CACHE_15200000019 = None
    CACHE_15021019698 = None
    CACHE_15200000007 = None
    CACHE_19900000004 = None
    CACHE_19900040002 = None
    CACHE_15200000009 = None
    CACHE_15200000005 = None
    CACHE_19900000022 = None
    CACHE_15200000002 = None

    # 用于强制锁替换
    LOCK_URL_CACHE = "http://\\1/"

    # 最后一个登陆信息
    # 多线程要注意
    CACHE_LAST = None

    @staticmethod
    def login(mobile, pwd, channel='c'):
        userName = {"mobile": mobile, "channel": channel, "password": pwd}
        headers = {'author': 'llbc', 'authorization': 'null', "channel": channel}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_C, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def login_c(mobile, pwd):
        userName = {"mobile": mobile, "channel": "c", "password": pwd}
        headers = {'author': 'llbc', 'authorization': 'null', "channel": "c"}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_C, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def login_cw(mobile, pwd):
        userName = {"mobile": mobile, "channel": "cw", "password": pwd}
        headers = {'author': 'haolie', 'authorization': 'null', "channel": "cw"}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_CW, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def login_crm(mobile, pwd, channel):
        userName = {"mobile": mobile, "channel": channel, "password": pwd}
        headers = {'author': 'haolie', 'authorization': 'null', "channel": channel}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_CRM, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def login_hr(mobile, pwd):
        userName = {"mobile": mobile, "channel": "hr", "password": pwd}
        headers = {'author': 'llbhr', 'authorization': 'null', "channel": "hr"}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_HR, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def hr19900020002():
        """
           登陆以后返回请求头
           HR 19900020002登陆HR端
           渠道hr
           注:有缓存,重复登陆,不发请求
           """

        if LoginGo.CACHE_19900020002 is not None:
            return LoginGo.CACHE_19900020002
        userName = {"mobile": "19900020002", "channel": "hr", "password": "123456"}
        headers = {'author': 'llbc', 'authorization': 'null'}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_HR, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_19900020002 = headers
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def c19900030001():

        """
        登陆以后返回请求头
        猎头 19900030001登陆C端
        渠道c
        """
        if LoginGo.CACHE_19900030001 is not None:
            LoginGo.CACHE_LAST = LoginGo.CACHE_19900030001
            return LoginGo.CACHE_19900030001
        userName = {"mobile": "19900030001", "channel": "c", "password": "123456"}
        headers = {'author': 'llbc', 'authorization': 'null', "channel": "c"}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_C, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_19900030001 = headers
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def c15021019698():
        if LoginGo.CACHE_15021019698 is not None:
            LoginGo.CACHE_LAST = LoginGo.CACHE_15021019698
            return LoginGo.CACHE_15021019698
        userName = {"mobile": "15021019698", "channel": "c", "password": "123456"}
        headers = {'author': 'llbc', 'authorization': 'null'}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_C, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_15021019698 = headers
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def c15900000001():
        if LoginGo.CACHE_15900000001 is not None:
            LoginGo.CACHE_LAST = LoginGo.CACHE_15900000001
            return LoginGo.CACHE_15900000001
        userName = {"mobile": "15900000001", "channel": "c", "password": "123456"}
        headers = {'author': 'llbc', 'authorization': 'null'}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_C, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_15900000001 = headers
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def crm_crmc_19900000002():
        """
         crmc 商务渠道,普通CRMc成员,登陆
         """

        if LoginGo.CACHE_19900000002 is not None:
            LoginGo.CACHE_LAST = LoginGo.CACHE_19900000002
            return LoginGo.CACHE_19900000002
        headers = LoginGo.login_crm("19900000002", "123456", "crmc")
        LoginGo.CACHE_19900000002 = headers
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def crm_crmhr_19900040002():
        """
        销售部 leader 19900040002
        """
        if LoginGo.CACHE_19900040002 is not None:
            LoginGo.CACHE_LAST = LoginGo.CACHE_19900040002
            return LoginGo.CACHE_19900040002
        headers = LoginGo.login_crm("19900040002", "123456", "crmhr")
        LoginGo.CACHE_19900040002 = headers
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def crm_crmhr_19900000004():
        """
        销售部 leader 19900000004
        """
        if LoginGo.CACHE_19900000004 is not None:
            LoginGo.CACHE_LAST = LoginGo.CACHE_19900000004
            return LoginGo.CACHE_19900000004
        headers = LoginGo.login_crm("19900000004", "123456", "crmhr")
        LoginGo.CACHE_19900000004 = headers
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def crm_crmc_19900000022():
        """
         crmc 商务渠道,普通CRMc成员,登陆
         """
        if LoginGo.CACHE_19900000022 is not None:
            LoginGo.CACHE_LAST = LoginGo.CACHE_19900000022
            return LoginGo.CACHE_19900000022
        headers = LoginGo.login_crm("19900000022", "123456", "crmc")
        LoginGo.CACHE_19900000022 = headers
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def crm_func_admin19912345678():
        """
         CRM 管理渠道,数据管理员,登陆
         """

        if LoginGo.CACHE_19912345678 is not None:
            LoginGo.CACHE_LAST = LoginGo.CACHE_19912345678
            return LoginGo.CACHE_19912345678
        userName = {"mobile": "19912345678", "channel": "func", "password": "123456"}
        headers = {'author': 'llbc', 'authorization': 'null', 'channel': 'func'}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_CRM, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_19912345678 = headers
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def c15200000019():
        """
         登陆以后返回请求头
         猎头 15200000019登陆C端
         渠道c
         """

        if LoginGo.CACHE_15200000019 is not None:
            LoginGo.CACHE_LAST = LoginGo.CACHE_15200000019
            return LoginGo.CACHE_15200000019
        userName = {"mobile": "15200000019", "channel": "c", "password": "123456"}
        headers = {'author': 'llbc', 'authorization': 'null'}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_C, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_15200000019 = headers
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def cw19900000011():
        if LoginGo.CACHE_19900000011 is not None:
            LoginGo.CACHE_LAST = LoginGo.CACHE_19900000011
            return LoginGo.CACHE_19900000011
        userName = {"mobile": "19900000011", "password": "123456", "channel": "cw"}
        headers = {'author': 'llbc', 'authorization': 'null', 'channel': 'cw'}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_CRM, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_19900000011 = headers
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def crm_crmhr_member15200000007():
        """
         CRM 销售渠道,普通CRMHR成员,登陆
         """

        if LoginGo.CACHE_15200000007 is not None:
            LoginGo.CACHE_LAST = LoginGo.CACHE_15200000007
            return LoginGo.CACHE_15200000007
        userName = {"mobile": "15200000007", "channel": "crmhr", "password": "123456"}
        headers = {'author': 'llbc', 'authorization': 'null', 'channel': 'crmhr'}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_CRM, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_15200000007 = headers
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def crm_crmc_member15200000009():
        """
         CRM 商务部渠道,普通CRMC成员,登陆
         """

        if LoginGo.CACHE_15200000009 is not None:
            LoginGo.CACHE_LAST = LoginGo.CACHE_15200000009
            return LoginGo.CACHE_15200000009
        userName = {"mobile": "15200000009", "channel": "crmc", "password": "123456"}
        headers = {'author': 'llbc', 'authorization': 'null', 'channel': 'crmc'}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_CRM, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_15200000009 = headers
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def crm_crm_member15200000005():
        """
         CRM 管理渠道,CRM管理成员,登陆
         """

        if LoginGo.CACHE_15200000005 is not None:
            LoginGo.CACHE_LAST = LoginGo.CACHE_15200000005
            return LoginGo.CACHE_15200000005
        userName = {"mobile": "15200000005", "channel": "func", "password": "123456"}
        headers = {'author': 'llbc', 'authorization': 'null', 'channel': 'func'}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_CRM, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_15200000005 = headers
        LoginGo.CACHE_LAST = headers
        return headers

    @staticmethod
    def cw_member15200000002():
        """
         CW CW成员,登陆
         """

        if LoginGo.CACHE_15200000002 is not None:
            LoginGo.CACHE_LAST = LoginGo.CACHE_15200000002
            return LoginGo.CACHE_15200000002
        userName = {"mobile": "15200000002", "channel": "cw", "password": "123456"}
        headers = {'author': 'llbc', 'authorization': 'null', 'channel': 'cw'}
        out = HttpClient.client.post(LoginGo.URL_XAUTH_CW, json=userName, headers=headers).json()
        headers['authorization'] = out['body']
        LoginGo.CACHE_15200000002 = headers
        LoginGo.CACHE_LAST = headers
        return headers
