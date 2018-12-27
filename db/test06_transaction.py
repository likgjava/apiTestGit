# 导包
import pymysql

# 创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "books")

# 创建游标对象
cursor = conn.cursor()

try:
    # 新增一条图书数据
    sql = "insert into t_book(id,title,pub_date) values(4,'西游记','1986-01-01')"
    cursor.execute(sql)

    # 抛出一个异常
    raise Exception("故意抛出了一个异常")

    # 新增一条英雄人物数据
    sql = "insert into t_hero(name,gender,book_id) values('孙悟空',1,4)"
    cursor.execute(sql)

    # 提交事务
    conn.commit()
except Exception as e:
    print("error!", e)
    # 回滚事务
    conn.rollback()
finally:
    # 关闭游标对象
    cursor.close()

    # 关闭数据库连接
    conn.close()
