# 导包
import pymysql

# 创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "stu")

# 创建游标对象
cursor = conn.cursor()

# 执行操作：查询全部的学生数据
cursor.execute("select * from student")

# 获取查询结果的总记录数
print("rowcount=", cursor.rowcount)

# 获取下一条数据
one = cursor.fetchone()
print("one=", one)

# 获取所有行
student_list = cursor.fetchall()
print("student_list=", student_list)
for student in student_list:
    print("student=", student)

# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()
