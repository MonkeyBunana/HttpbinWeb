from Common.operate_mysql import Database

class RequestSql:

    def __init__(self):
        self.conn = Database().conn()

