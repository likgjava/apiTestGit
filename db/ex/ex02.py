# 2.请使用pymysql完成以下需求：
# * 插入一本书，书名为‘python从入门到放弃’，阅读量为50，评论量为0，发布日志为：2020-01-01
# * 测试工程师人员发现一个bug，这个本书的评论数与实际不符，要求你把评论量修改为修正后的值：250
# * 老板投资了python，觉得这本书名太不吉利，需要下架，请删除这本书。
# * 你删除后，心中不放心到底有没有删除，想确认是否真正删除了，你需要怎么做？

# 答案有多种，需要注意的是：应该要提交事务
# 导包
import pymysql

# 建立连接
conn = pymysql.connect("localhost", 'root', 'root', 'books', autocommit=True)

# 获取游标
cursor = conn.cursor()

# 执行需求一：插入一本书，书名为‘python从入门到放弃’，阅读量为50，评论量为0，发布日志为：2020-01-01
sql = "insert into t_book(title,`read`,`comment`,pub_date) values('python从入门到放弃',50,0,'2020-01-01');"
cursor.execute(sql)

# 执行需求二：把评论量修改为修正后的值：250
sql = "update t_book set `comment` = 250 where title='python从入门到放弃';"
cursor.execute(sql)

# 执行需求三：删除这本书
sql = "delete from t_book where title = 'python从入门到放弃';"
cursor.execute(sql)

# 执行需求四：确认是否真正删除了
sql = "select * from t_book;"
cursor.execute(sql)
print("全部的书有：", cursor.fetchall())

# 确认删除
# 使用MySQL客户端如navicat查询数据，确认数据库中数据是否被删除掉

# 关闭游标
cursor.close()

# 关闭连接
conn.close()
