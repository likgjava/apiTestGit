# 导包
import pymysql

# 创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "books", autocommit=True)

# 创建游标对象
cursor = conn.cursor()

# 执行操作：把图书名称为‘西游记’的阅读量加一
sql = "update t_book set `read`=`read`+1 where title='西游记'"
cursor.execute(sql)

# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()
