import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='spiderdb',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

# 插入数据
#sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', %.2f )"
sql1 = "INSERT INTO trade (name, account, saving) SELECT 'name' FROM trade WHERE NOT EXISTS(SELECT * FROM trade WHERE 'name'=''%s' AND 'account'='%s' AND 'saving'='%2f')"
data = ('雷军2', '13512345678', 10000)
cursor.execute(sql1 % data)
connect.commit()
print('成功插入', cursor.rowcount, '条数据')


# 关闭连接
cursor.close()
connect.close()