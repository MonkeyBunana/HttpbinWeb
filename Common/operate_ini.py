# -*- coding: utf-8 -*-”
import configparser

class ReadConfig:

    def __init__(self):
        self.conf = configparser.ConfigParser()


    def getValue(self, section, name):
        """ 读取 Resources/File 文件夹中的 config.ini，返回 config.ini 获取字段的值
        :param section: config.ini 中的标题名
        :param name: config.ini 中的字段名
        :return: str
        """
        # 此处是utf-8-sig，而不是utf-8
        self.conf.read("../Resources/File/config.ini", encoding="utf-8-sig")
        return self.conf.get(section, name)


if __name__ == "__main__":
    browser = ReadConfig().getValue(section='located_path', name='log_path')
    print(browser)
