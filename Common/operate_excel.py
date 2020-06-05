# -*- coding: utf-8 -*-”
import xlrd
from Common.operate_ini import ReadConfig
from xlutils.copy import copy

class ExcelData:

    def __init__(self):
        # 获取Excel表路径
        self.excel_path = ReadConfig().getValue(section='located_path', name='excel_path')
        # 获取Excel用例表
        self.excel_sheet = ReadConfig().getValue(section='custom_variable', name='excel_sheet_name')
        # 打开Excel
        self.data = xlrd.open_workbook(self.excel_path)
        # 打开指定用例表
        self.table = self.data.sheet_by_name(self.excel_sheet)
        # 获取有效行数
        self.rowNum = self.table.nrows
        # 获取有效列数
        self.colNum = self.table.ncols
        # 获取第一行所有内容,如果括号中1就是第二行，这点跟列表索引类似
        self.keys = self.table.row_values(0)

    def read_excel(self):
        """
            xlrd的数据类型有：0 empty, 1 string, 2 number, 3 date, 4 boolean, 5 error
            数字一律按浮点型输出，日期输出成一串小数，布尔型输出0或1，所以我们必须在程序中做判断处理转换成我们想要的数据类型
        """
        # 定义一个空列表
        datas = []
        for i in range(1, self.rowNum):
            # 定义一个空字典
            sheet_data = {}
            for j in range(self.colNum):
                # 获取单元格数据类型
                c_type = self.table.cell(i, j).ctype
                # 获取单元格数据
                c_cell = self.table.cell_value(i, j)
                if c_type == 2 and c_cell % 1 == 0:    # 如果是整形
                    c_cell = int(c_cell)
                sheet_data[self.keys[j]] = c_cell
            datas.append(sheet_data)
        return datas


    def write_excel_token(self, token):
        """ 将token值写入Excel列表中
        :param token: 传入获取到的token值
        :return: 暂无返回
        """
        copy_excel = copy(self.data)
        # 通过get_sheet()获取的sheet有write()方法
        for i in self.post_token_items():
            for k, v in i.items():
                v['userToken'] = token
                copy_excel.get_sheet(0).write(int(k), 8, str(v))
        copy_excel.save(self.excel_path)


    def post_token_items(self):
        # 获取request Data中含有userToken的No列表
        token_list = []
        token_data = {}
        # 读取Excel数据
        excel_data = ExcelData().read_excel()
        for i in excel_data:
            if 'userToken' in i.get('Request Data'):
                token_data[i.get('No')] = eval(i.get('Request Data'))
                token_list.append(token_data)
        return token_list


if __name__ == "__main__":
    # print(ExcelData().read_excel())
    print(ExcelData().post_token_items())
    # ExcelData().write_excel_token(2)