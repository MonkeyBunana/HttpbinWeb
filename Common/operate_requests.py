# -*- coding: utf-8 -*-”
import requests

class RequestsData:

    def get_request(self, url, data=None, headers=None):
        res = requests.get(url=url, data=data, headers=headers)
        return res

    def post_request(self, url, data, headers=None):
        res = requests.post(url=url, data=data, headers=headers)
        return res

    def del_request(self, url, data=None, headers=None):
        res = requests.delete(url, data=data)
        return res

    def put_request(self, url, data, headers=None):
        pass

    def send_request(self, method, url, data=None, headers=None):
        try:
            if headers:
                if method == "GET":
                    return self.get_request(url, data, headers=headers)
                if method == "POST":
                    return self.post_request(url, data=data, headers=headers)
                if method == "DELETE":
                    return self.del_request(url, data=data, headers=headers)
                if method == "PUT":
                    return self.put_request(url, data=data, headers=headers)
            else:
                pass
        except Exception as e:
            pass