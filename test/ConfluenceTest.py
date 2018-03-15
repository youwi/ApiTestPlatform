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
            "value": "<p>汉字This is a new page</p><ul class='inline-task-list'><li data-inline-task-id=''>这是一条任务&nbsp;<a class='confluence-link' data-base-url='http://conf.jihui.in' data-linked-resource-id='5277116' data-linked-resource-type='userinfo' href='http://conf.jihui.in/display/~yuzc' data-linked-resource-default-alias='余珍成'>余珍成</a></li></ul>",
            "representation": "storage"
        }
    }
}

resp = requests.post("http://conf.jihui.in/rest/api/content/", json=data, auth=('yuzc', 'yuzc@1Ab'))

print(resp)
