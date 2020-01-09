# 1.导包
import pymysql

# 2.创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "books", autocommit=True)

# 3.获取游标对象
cursor = conn.cursor()

# 4.执行操作
# 1).连接到数据库（host:localhost username:root password:root database:books autocommit:True）
# 2).新增一条图书数据（id:4 title:西游记 pub_date:1986-01-01 ）
sql = "insert into t_book(title,pub_date) values('西游记', '1986-01-01')"
cursor.execute(sql)

print("id===", cursor.lastrowid)

# 5.关闭游标
cursor.close()

# 6.关闭数据库连接
conn.close()
