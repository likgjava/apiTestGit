# 4.使用pymysql操作MySQL数据库，具体操作如下：
# 1).在“books”数据库中，新增评论表t_comment，包含字段：主键、图书id、评论人名称、评论内容、评论时间。
# 2).在评论表中新增一条数据，并更新图书表t_book中的评论量comment字段。

"""
CREATE TABLE `t_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL COMMENT '图书id',
  `name` varchar(20) NOT NULL COMMENT '评论人名称',
  `content` varchar(100) DEFAULT NULL COMMENT '评论内容',
  `create_time` datetime DEFAULT NULL COMMENT '评论时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='评论表';
"""

import pymysql

conn, cursor = None, None
try:
    # 创建数据库连接
    conn = pymysql.connect("localhost", "root", "root", "books", autocommit=False)

    # 获取游标对象
    cursor = conn.cursor()

    # 执行操作
    # 新增评论
    sql = "insert into t_comment(book_id,name,content,create_time) values(1,'李白', '这本书不错', '2020-01-01 20:01:01')"
    cursor.execute(sql)

    # 更新图书表t_book中的评论量comment字段
    sql = "update t_book set comment=comment+1 where id=1"
    cursor.execute(sql)

    # 提交事务
    conn.commit()
except Exception as e:
    print("error:", e)
    # 回滚事务
    conn.rollback()
finally:
    # 关闭游标
    if cursor:
        cursor.close()

    # 关闭数据库连接
    if conn:
        conn.close()
