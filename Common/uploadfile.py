# encoding:utf-8
from TestSuites import Swagger, URL_FILE_UPLOAD
from Common.HttpClient import HttpClient


class UploadFile(object):
    headers = None

    def init(self, headers=None):
        self.headers = headers

    def get_token(self, base_url):
        if not self.headers:
            raise ValueError("none of headers")
        token_url = base_url + Swagger("/token/upload")
        resp = HttpClient.client.get(token_url, headers=self.headers)
        resp = resp.json()
        token = resp["body"]["value"]
        return token

    def upload_to_internal(self, base_url, data_path):
        """
        上传至运维的服务器
        """
        url = URL_FILE_UPLOAD + Swagger("")
        file = open(data_path, "rb")
        resp = HttpClient.client.post(url, params={"token": self.get_token(base_url)},
                                      files={'file': ("1.docx", file.read(), "application/vnd.ms-word")})
        resp = resp.json()
        key = resp["key"]
        file.close()
        return key
