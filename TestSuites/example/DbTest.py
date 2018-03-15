import pymysql

# 这个例子不能作为测试用例!
# 打开数据库连接
# 不数据库
db = pymysql.connect("xxxxxx", "1111", "111", "1111")
cursor = db.cursor()
cursor.execute("select * from account where mobile='xxxx'")
data = cursor.fetchone()
print(data)
db.close()

# 这个例子不能作为测试用例!
# 这个例子不能作为测试用例!
