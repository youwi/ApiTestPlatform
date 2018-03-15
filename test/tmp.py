import os


# print(os.curdir)
# print(os.getcwd())


#print(file_list)

# dir2 = os.path.walk(os.path.dirname(os.path.abspath(__file__)) + "../Suites")
from Common.utils import HttpClient

payload = {
    "id": 24,
    "eventCode": "AS6170",
    "eventName": "这是一个专题",
    "headImgUrl": "https://i.xxxxxxx.com/o_1c43i5ds51ikqvn81edtjb41f391a.png",
    "headImgHeight": 719,
    "footerImgUrl": "https://i.xxxxxxx.com/o_1c43i5vg81j8b1fag1abc1tgj1alh1f.png",
    "navigationUrl": "https://i.xxxxxxx.com/o_1c43i5a7crubb2363q1mu711pj15.png",
    "bgColorFrom": "#040541",
    "bgColorTo": "#0f010e",
    "categories": [
        {
            "id": 154,
            "specialEventId": 24,
            "categoryName": "产品类",
            "categoryOrder": 1,
            "showStyle": "0",
            "headImgUrl": "https://i.xxxxxxx.com/o_1c43i6es11rtrp3t1vb71nct1rkg1p.png",
            "borderColor": "#ec6f39",
            "projectNos": [
                "YX74160"
            ]
        },
        {
            "id": 155,
            "specialEventId": 24,
            "categoryName": "产婆",
            "categoryOrder": 2,
            "showStyle": "0",
            "headImgUrl": "https://i.xxxxxxx.com/o_1c43ia5n0eet1g41qnm19ot1vot3v.png",
            "borderColor": "#d05c0d",
            "projectNos": [
                "YX74160"
            ],
            "logoUrl": "https://i.xxxxxxx.com/o_1c43ia2es152o5srio516pm1p9f3q.png"
        },
        {
            "id": 156,
            "specialEventId": 24,
            "categoryName": "chan3",
            "categoryOrder": 3,
            "showStyle": "0",
            "headImgUrl": "https://i.xxxxxxx.com/o_1c43idl4tn6gdpqm7u1kqmlj5m.png",
            "borderColor": "#ff8630",
            "projectNos": [
                "YX74160"
            ],
            "logoUrl": "https://i.xxxxxxx.com/o_1c43idiat8nb1igd1ic51dnfa75h.png"
        },
        {
            "id": 157,
            "specialEventId": 24,
            "categoryName": "444",
            "categoryOrder": 4,
            "showStyle": "0",
            "headImgUrl": "https://i.xxxxxxx.com/o_1c43ieqke1oaqcuk13j816ei13fl7i.png",
            "borderColor": "#ff5625",
            "projectNos": [
                "YX74160"
            ]
        },
        {
            "id": 158,
            "specialEventId": 24,
            "categoryName": "5454",
            "categoryOrder": 5,
            "showStyle": "0",
            "headImgUrl": "https://i.xxxxxxx.com/o_1c43isfl81vntk1qvuu8g81uor73.jpeg",
            "borderColor": "#e6f11d",
            "projectNos": [
                "HM13302"
            ]
        }
    ]
}
headers = LOGIN_HEADERS
response = HttpClient.client.request("POST", url, json=payload, headers=headers)
