out = "http://crm.xxxxxxx.com/api/biz/account/tag/list".replace('http://(.*)?/', "\\2")

print(out)

import re

src = 'aabcdddd'
print(re.sub('(b).*(dd)', '\\2+\\2', src))

print(re.sub('(b).*(dd)', '', src))

print(re.sub('http://(.*?)/', "http://baidu.com/", "http://crm.xxxxxxx.com/api/biz/account/tag/list"))


print(re.sub('http://(.*?)/', "http://:\\1/", "http://crm.xxxxxxx.com/api/biz/account/tag/list"))
