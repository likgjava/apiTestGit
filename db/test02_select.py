# 1.导包
import pymysql

# 2.创建数据库连接
# 连接到数据库（host:localhost username:root password:root database:books）
conn = pymysql.connect("localhost", "root", "root", "books")

# 3.获取游标对象
cursor = conn.cursor()

# 4.执行操作
# 2).查询图书表的数据（包括：图书id、图书名称、阅读量、评论量）
sql = "SELECT t.id,t.title,t.`read`,t.`comment` from t_book t"
cursor.execute(sql)

# 3).获取查询结果的总记录数
rowcount = cursor.rowcount
print("总记录数=", rowcount)

# 4).获取查询结果的第一条数据
# first = cursor.fetchone()
# print("first=", first)

# 5).获取全部的查询结果
data_list = cursor.fetchall()
print("data_list=", data_list)

for book in data_list:
    id, title, read, comment = book
    print("id={} title={} read={} comment={}".format(id, title, read, comment))

# 5.关闭游标
cursor.close()

# 6.关闭数据库连接
conn.close()
