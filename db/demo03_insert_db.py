# 导包
import pymysql

# 创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "stu", autocommit=True)

# 创建游标对象
cursor = conn.cursor()

# 执行操作：新增一条学生数据
sql = "insert into student(id,name,sex,hometown,age) values('111','李白1','男','',18)"
cursor.execute(sql)

# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()
