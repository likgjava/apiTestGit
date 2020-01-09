# 1.导包
import pymysql

conn, cursor = None, None
try:
    # 2.创建数据库连接
    conn = pymysql.connect("localhost", "root", "root", "books", autocommit=False)
    # conn.autocommit(False)

    # 3.获取游标对象
    cursor = conn.cursor()

    # 4.执行操作
    # 2).新增一条图书数据（id:4 title:西游记 pub_date:1986-01-01 ）
    # sql = "insert into t_book(id,title,pub_date) values(4, '西游记', '1986-01-01')"
    sql = "insert into t_book(title,pub_date) values('西游记', '1986-01-01')"
    cursor.execute(sql)

    # 3).故意抛出一个异常
    raise Exception("故意抛出一个异常")

    # 4).新增一条英雄人物数据（name:孙悟空 gender:1 book_id:4）
    sql = "insert into t_hero(name,gender,book_id) values('孙悟空', 1, %s)"
    cursor.execute(sql, cursor.lastrowid)

    # 提交事务
    conn.commit()
except Exception as e:
    print("error:", e)
    # 回滚事务
    conn.rollback()
finally:
    # 5.关闭游标
    if cursor:
        cursor.close()

    # 6.关闭数据库连接
    if conn:
        conn.close()
