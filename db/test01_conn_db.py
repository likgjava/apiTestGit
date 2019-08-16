# 1).连接到数据库（host:localhost username:root password:root database:books）
# 2).获取数据库服务器版本信息

# 1. 导包
import pymysql

# 2. 创建数据库连接
conn = pymysql.connect("localhost", "root", "root", "books", port=3306)

# 3. 获取游标对象
cursor = conn.cursor()

# 4. 执行操作：获取数据库的版本信息
cursor.execute("select version()")
result = cursor.fetchone()
print("result=", result)

# 5. 关闭游标
cursor.close()

# 6. 关闭数据库连接
conn.close()
