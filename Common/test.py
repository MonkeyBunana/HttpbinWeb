# -*- coding: utf-8 -*-”
from Common.operate_requests import RequestsData
from Common.operate_excel import ExcelData
import json


class test:
    def __init__(self):
        self.result_res = []
        self.get_excel_datas = ExcelData().read_excel()
        self.req_data = {}

    def test_send_request(self):
        # 遍历read_excel传过来的Excel list数据
        for i in self.get_excel_datas:
            # 如果Excel中用例是可执行的
            if i.get('IsRun') == 'Y':
                # 如果Excel中的token为空
                if 'userToken' in eval(i.get('Request Data')) and eval(i.get('Request Data'))['userToken'] == '':
                    if i.get('Method') == 'POST':
                        # 获取Excel中的token值
                        self.req_data = eval(i.get('Request Data'))
                        # 给req_data字典中的userToken字段调用get_user_token()获取token
                        self.req_data['userToken'] = self.get_user_token()
                # 调用requests模板，根据参数返回get、post结果
                res = RequestsData().send_request(
                    method=i.get('Method'),
                    url=i.get('Url'),
                    data=self.req_data,
                    headers=eval(i.get('Headers')))
                # 将结果整合为一个字典
                res_str = {i.get('API Name'): {"status_code": res.status_code,
                                               "headers": dict(res.headers),
                                               "body": json.loads(res.text)}}
                # 将字典添加到列表中
                self.result_res.append(res_str)


        # 将列表转化为json数据，并返回
        # indent： json缩进多少空格
        # ensure_ascii： json值是否使用unicode编码
        return json.dumps(self.result_res, indent=2, ensure_ascii=False)

    def get_user_token(self):
        method = 'POST'
        url = 'http://192.168.1.47:8080/service/api/p/login/userLogin'
        data = {"loginName": "zhonglilong", "loginPwd": "Td123456"}
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

        res = RequestsData().send_request(method=method, url=url, data=data, headers=headers)
        return dict(json.loads(res.text))['data']['userToken']


if __name__ == "__main__":
    print(test().test_send_request())
    # test().test_send_request()
    # test().get_user_token()