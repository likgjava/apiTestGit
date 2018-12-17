# 导包
import pymysql

# 创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "books", autocommit=True)

# 创建游标对象
cursor = conn.cursor()

# 执行操作：新增一条图书数据
sql = "insert into t_book(id,title,pub_date) values(4,'西游记','1986-01-01')"
cursor.execute(sql)

# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()
