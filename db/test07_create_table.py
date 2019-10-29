# 1.导包
import pymysql

# 2.创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "books", autocommit=True)

# 3.获取游标对象
cursor = conn.cursor()

# 4.执行操作
# 1).连接到数据库（host:localhost username:root password:root database:books autocommit:True）
# 2).新增一条图书数据（id:4 title:西游记 pub_date:1986-01-01 ）
sql = """
        CREATE TABLE `t_hello` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(20) NOT NULL COMMENT '图书名称',
  `pub_date` date NOT NULL COMMENT '发布日期',
  `read` int(11) NOT NULL DEFAULT '0' COMMENT '阅读量',
  `comment` int(11) NOT NULL DEFAULT '0' COMMENT '评论量',
  `is_delete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '逻辑删除',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='图书表';
"""
cursor.execute(sql)

# 5.关闭游标
cursor.close()

# 6.关闭数据库连接
conn.close()
