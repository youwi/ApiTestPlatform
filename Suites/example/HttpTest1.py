import requests


"""
  这个例子不能做为测试用例!
  这里只是展示如何进行写代码.
"""

loginUrl = 'http://www.lieluobo.testing/api/biz/account/xauth'
positionUrl = 'http://hr.lieluobo.testing/api/biz/hr/positions'
userName = {"mobile": "19900020002", "channel": "hr", "password": "123456"}
headers = {'author': 'llbc', 'authorization': 'null'}
params = {'page': 1, 'size': 10, 'keyword': '', 'status': 0}
out = requests.post(loginUrl, json=userName, headers=headers).json()
headers['authorization'] = out['body']
# print(out['body'])
hrp = requests.get('http://hr.lieluobo.testing/api/biz/hr/positions', params, headers=headers).json()
lasted = hrp['body'][0]['positionName']
print(lasted)

# 这个例子不能做为测试用例!



