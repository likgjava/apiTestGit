# 1.导包
import pymysql

# 2.创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "books", autocommit=True)

# 3.获取游标对象
cursor = conn.cursor()

# 4.执行操作
# 把图书名称为‘西游记’的阅读量加一
sql = "UPDATE t_book SET `read`=`read`+1 WHERE title='西游记'"
# sql = "UPDATE t_book SET `read`=`read`+1"
cursor.execute(sql)

rowcount = cursor.rowcount
print("rowcount=", rowcount)

# 5.关闭游标
cursor.close()

# 6.关闭数据库连接
conn.close()
