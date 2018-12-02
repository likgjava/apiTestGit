# 导包
import pymysql

# 创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "stu")

# 创建游标对象
cursor = conn.cursor()

# 执行操作：删除姓名为‘李白’的学生
sql = "delete from student where name='李白'"
cursor.execute(sql)

# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()
