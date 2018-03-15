"""
断言工具类
"""
import json


class Assertion:


    @staticmethod
    def jsonContain(ori, exp={}):
        """
           第一个参数为返回结果(大集)
           第二个参数为期待的包含的值(小集)
        """
        if ori is None: return False
        json.dumps(ori)

        if json.dumps(exp) in json.dumps(ori):
            return True
        if Assertion.trimSp(json.dumps(exp)) in json.dumps(ori):
            return True

        if isinstance(ori, str):
            return json.dumps(exp) in json.dumps(ori)

        if isinstance(ori, list):
            for i in range(0, len(ori)):
                curr = ori[i]
                if Assertion.trimSp(json.dumps(exp)) in json.dumps(curr) + "":
                    return True
                if Assertion.jsonContain(ori[i], exp):
                    return True

        if isinstance(ori, dict):
            if Assertion.inObject(ori, exp):
                return True
            for key in ori:
                if Assertion.jsonContain(ori[key], exp):
                    return True

            for key in exp:
                if Assertion.trimSp(json.dumps(exp)) in json.dumps(ori.get(key)) + "":
                    return True
                if Assertion.jsonContain(ori.get(key), exp):
                    return True

        return False


    @staticmethod
    def trimSp(obj):
        """
           *  消除2端无用符号,如 {a} 变成 a
           *  用于json对比
           *
        """
        arr = ['{', ']', '}', '[', "{[", "]}", "[{", "}]", "[[", "]]", "{{", "}}"]
        for i in range(0, len(arr)):
            ch = arr[i]
            if obj.startswith(ch):
                obj = obj.replace(ch, "")
            if obj.endswith(ch):
                obj = obj.replace(ch, "")

        return obj

    @staticmethod
    def inObject(objBig, objTarget):
        match = True
        for key in objTarget.keys():
            match = match and (
                    objTarget[key] == objBig.get(key, False)
                    or
                    json.dumps(objTarget.get(key, None)) == json.dumps(objBig.get(key, None))
            )

        return match


    @staticmethod
    def check(resp: object) -> object:
        # 猎萝卜错误码验证方法
        # code=1为返回正确
        if resp is None:
            assert False
        if hasattr(resp, "status_code"):
            code = resp.status_code

            if code == 200:
                json_str = resp.json()
                assert json_str['code'] == 1
            if code == 401:
                raise Exception("Login Error:" + bytes.decode(resp.content))
            if code == 404:
                raise Exception("404 Error:")
            if code == 500:
                raise Exception("500 Error:")
            if code == 502:
                raise Exception("502 Error:")
