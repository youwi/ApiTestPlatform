import pymysql

# 这个例子不能使用测试用例!
# 打开数据库连接
# 不数据库
db = pymysql.connect("172.16.52.81", "testing", "haolie123", "testing")
cursor = db.cursor()
cursor.execute("select * from account where mobile='19900020002'")
data = cursor.fetchone()
print(data)
db.close()

# 这个例子不能使用测试用例!
# 这个例子不能使用测试用例!
