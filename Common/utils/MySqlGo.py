import os
import pymysql


# 创建数据库连接,封装连接过程
# 有优化空间
# 禁用mysql做测试!
class MySqlGo(object):
    MYSQL_HOST = "192.168.8.13"
    MYSQL_DB_NAME = "xxxxxxx.com"
    MYSQL_USER_NAME = "testing"
    MYSQL_USER_PWD = "xxxxxxx.com123"

    db = pymysql.connect(MYSQL_HOST, MYSQL_USER_NAME, MYSQL_USER_PWD, MYSQL_DB_NAME)

    # 默认登陆到测试环境
    # 只返回一个结果
    # 非线程安全,如果是多线程,要另外处理
    # 测试用例如果插入数据库,不允许压力测试!
    @staticmethod
    def fetchone(sql):
        db = MySqlGo.db
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db.commit()
        map_data = cursor.fetchone()
        return map_data

    # 把数据库连接切换到另外一个环境
    # //TODO
    @staticmethod
    def switch_to_stg():
        MySqlGo.MYSQL_HOST = ""

    # 自动获取环境变量来设置数据库连接.
    # //TODO
    @staticmethod
    def auto_env():
        MySqlGo.MYSQL_DB_NAME = os.environ.get("PATHEXT")

    @staticmethod
    def close():
        MySqlGo.db.close()


    @staticmethod
    def insert(sql):
        MySqlGo.db.insert(sql)
