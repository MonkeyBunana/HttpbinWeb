import configparser

class ReadConfig:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read("../Resources/File/config.ini", encoding="utf-8-sig")  # 此处是utf-8-sig，而不是utf-8

    def getValue(self, section, name):
        return self.conf.get(section, name)


if __name__ == "__main__":
    browser = ReadConfig().getValue(section='browserType', name='browserName')
    print(len(browser))
