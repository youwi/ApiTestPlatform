# 创建一个新页面--
# https://docs.atlassian.com/ConfluenceServer/rest/6.7.2/#content-update
# https://developer.atlassian.com/server/confluence/confluence-rest-api-examples/
# curl -u admin:admin -X POST -H 'Content-Type: application/json' -d'{"type":"page","title":"new page",
# "ancestors":[{"id":456}], "space":{"key":"TST"},"body":{"storage":{"value":
# "<p>This is a new page</p>","representation":"storage"}}}'
# http://localhost:8080/confluence/rest/api/content/ | python -mjson.tool

import requests

data = {
    "type": "page",
    "title": "new page2222",
    "ancestors": [{"id": 5280144}],
    "space": {"key": "QA"},
    "body": {
        "storage": {
            "value": "fasfasf",
            "representation": "storage"
        }
    }
}

resp = requests.post("http://192.168.1.1/rest/api/content/", json=data, auth=('xxx', 'xxxx'))

print(resp)
