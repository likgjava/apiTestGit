import pymysql


class DBUtil:
    _conn = None

    @classmethod
    def get_conn(cls):
        if DBUtil._conn is None:
            cls._conn = pymysql.connect("localhost", "root", "root", "books")
        return cls._conn

    @classmethod
    def close_conn(cls):
        DBUtil.get_conn().close()

    @classmethod
    def get_cursor(cls):
        return DBUtil.get_conn().cursor()

    @classmethod
    def close_cursor(cls, cursor):
        if cursor:
            cursor.close()

