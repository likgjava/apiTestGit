# 导包
import pymysql

# 创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "stu")

# 创建游标对象
cursor = conn.cursor()

# 执行操作：把学生姓名为‘李白’的年龄改成20岁
sql = "update student set age=20 where name='李白'"
cursor.execute(sql)

# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()
