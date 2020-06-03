from Common.request_template import send_request
from Common.read_excel import read_excel
import json


class test:
    def __init__(self):
        self.result_res = []
        self.get_excel_datas = read_excel()

    def test_send_request(self):
        # 遍历read_excel传过来的Excel list数据
        for i in self.get_excel_datas:
            # 如果Excel中用例是可执行的
            if i.get('IsRun') == 'Y':
                # 调用requests模板，根据参数返回get、post结果
                res = send_request(
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


if __name__ == "__main__":
    print(test().test_send_request())
