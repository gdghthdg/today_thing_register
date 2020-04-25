#mysql安装的时候加密方式有问题,一定
# ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456';


import MySQLdb
import decimal
decimal.__version__


# 打开数据库连接
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", db="test_database",port=3306,charset='utf8' )

# db = mysql.connector.connect(host = 'localhost', user = 'root',password = 'somepasswd', database = 'randomdatabase')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT * FROM auth_group")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchall()

print(data)


# 关闭数据库连接
db.close()
input()

#alter user 'root'@'localhost' identified with mysql_native_password by '123456'