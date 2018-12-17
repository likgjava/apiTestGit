# 导包
import pymysql

# 创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "books")

# 创建游标对象
cursor = conn.cursor()

# 执行操作：查询全部的图书数据
cursor.execute("select * from t_book")

# 获取查询结果的总记录数
print("rowcount=", cursor.rowcount)

# 获取下一条数据
one = cursor.fetchone()
print("one=", one)

# 获取所有行
book_list = cursor.fetchall()
print("book_list=", book_list)
for book in book_list:
    print("book=", book)

# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()
