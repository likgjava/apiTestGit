# 1.导包
import pymysql

# 2.创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "books", autocommit=True)

# 3.获取游标对象
cursor = conn.cursor()

# 4.执行操作
# 删除名称为‘西游记’的图书
sql = "delete from t_book where title='西游记'"
cursor.execute(sql)

# 5.关闭游标
cursor.close()

# 6.关闭数据库连接
conn.close()
