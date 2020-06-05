# -*- coding: utf-8 -*-”
import json
from Common.operate_requests import RequestsData
from Common.operate_ini import ReadConfig

class SysDatas:

    def __init__(self):
        self.rd = RequestsData()
        self.rc = ReadConfig()

    def get_userToken(self):
        """ 通过post方法登录，获取并返回登录后随机值userToken
        :return: str
        """
        uname = self.rc.getValue(section='system_data', name='admin_uname')
        pwd = self.rc.getValue(section='system_data', name='admin_pwd')

        method = 'POST'
        url = 'http://192.168.1.47:8080/service/api/p/login/userLogin'
        data = {"loginName": uname, "loginPwd": pwd}
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/81.0.4044.138 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Connection": "keep-alive",
            "Host": "192.168.1.47:8080",
            "Origin": "http://192.168.1.47:8080",
            "Content-Length": "39",
            "Referer": "http://192.168.1.47:8080/elib/"
        }

        res = self.rd.send_request(method=method, url=url, data=data, headers=headers)
        return dict(json.loads(res.text))['data']['userToken']


if __name__ == '__main__':
    print(SysDatas().get_userToken())