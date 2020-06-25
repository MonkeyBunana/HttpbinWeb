# -*- coding: utf-8 -*-”
import requests

class RequestsData:

    @staticmethod
    def alter_data(**kwargs):
        data = {}
        for k, v in kwargs.items():
            if k != "id" and k != "eid" and v != 0 and v is not '':
                data[k] = v
        return data

    @staticmethod
    def alter_headers(**kwargs):
        headers = {}
        for k, v in kwargs.items():
            headers = {}
            if k != "id" and k != "eid":
                if k == "AcceptEncoding":
                    headers["Accept-Encoding"] = v
                elif k == "AcceptLanguage":
                    headers["Accept-Language"] = v
                elif k == "UserAgent":
                    headers["User-Agent"] = v
                elif k == "ContentType":
                    headers["Content-Type"] = v
                elif k == "ContentLength":
                    headers["Content-Length"] = v
                else:
                    headers[k] = v
        return headers

    @staticmethod
    def get_request(url, data=None, headers=None):
        res = requests.get(url=url, data=data, headers=headers)
        return res

    @staticmethod
    def post_request(url, data, headers=None):
        res = requests.post(url=url, data=data, headers=headers)
        return res

    @staticmethod
    def del_request(url, data=None, headers=None):
        res = requests.delete(url, data=data)
        return res

    @staticmethod
    def put_request(url, data, headers=None):
        res = requests.put(url, data, headers)

    def send_request(self, method, url, data=None, headers=None):
        """ 根据 request 的方法类型传入 url，data，headers 等值
        :param method: get / post / delete / put ...
        :param url: 网页地址
        :param data: 网页传参
        :param headers: 请求头
        :return: response
        """
        try:
            if headers:
                if method == "GET":
                    return self.get_request(url, self.alter_data(**data), self.alter_headers(**headers))
                if method == "POST":
                    return self.post_request(url, self.alter_data(**data), self.alter_headers(**headers))
                if method == "DELETE":
                    return self.del_request(url, self.alter_data(**data), self.alter_headers(**headers))
                if method == "PUT":
                    return self.put_request(url, self.alter_data(**data), self.alter_headers(**headers))
            else:
                pass
        except Exception as e:
            pass

