# 导包
import pymysql

# 创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "stu")

# 创建游标对象
cursor = conn.cursor()

try:
    # 新增一条学生数据
    sql = "insert into student(id,name,sex,hometown,age) values('010','李白','男','',18)"
    cursor.execute(sql)

    # 抛出一个异常
    raise Exception

    # 新增一条教师数据
    sql = "insert into teacher(id,name) values('4','孔子')"
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
