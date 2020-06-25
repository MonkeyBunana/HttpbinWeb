# -*- coding: utf-8 -*-”
import json

from Common.operate_excel import ExcelData
from Requests.requests_sys_datas import SysDatas
from Common.operate_requests import RequestsData

class SendRequests:

    def __init__(self):
        self.result_res = []
        self.get_excel_datas = ExcelData().read_excel()
        self.get_userToken = SysDatas().get_userToken()
        self.rd = RequestsData()

    def response(self):
        """ 将数据读出并循环放入运行，返回处理好的 json 结果
            1、先将字段 Request Data 中的 userToken 赋值并保存回表中
            2、获取表中的所有数据，返回的一个 List，包含 dict
            3、将值分别对应填入模板中，运行结果处理后整合为一个 List，包含 dict
            4、转换为 json 值传出
        :return: json
        """
        # 给Excel中的userToken添加/更新值
        ExcelData().write_excel(self.get_userToken)
        # 遍历read_excel传过来的Excel list数据
        for i in self.get_excel_datas:
            # 如果Excel中用例是可执行的
            if i.get('IsRun') == 'Y':
                # 调用requests模板，根据参数返回get、post结果
                res = self.rd.send_request(
                    method=i.get('Method'),
                    url=i.get('Url'),
                    data=eval(i.get('Request Data')),
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


if __name__ == '__main__':
    print(SendRequests().response())