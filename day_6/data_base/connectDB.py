#1.首先导入 pymysql 代码库
import pymysql

#2.连接数据库
def connDb():
    #要想连接数据库，需要知道数据库的连接地址、端口号、数据库的名称、用户名和密码
    conn=pymysql.Connect(host="127.0.0.1", user="root", password="root",database="pirate", port=3306, charset='utf8')
    #查询 hd_user 表中所有的数据，并且倒叙打印
    sql="select * from hd_user order by id desc"
    #要想在代码中执行这条sql语句，首先要获取数据库的游标
    curs=conn.cursor()
    #通过游标来执行sql语句
    # execute() 执行方法
    curs.execute(sql)
    #想获取数据库中最新的记录，那么就要把数据库所有记录倒叙排列
    #然后用 fetchone() 获取第一条记录，即数据库最新的记录.   fetch 抓取的意思
    result=curs.fetchone()
    #如果想获取所有的查询结果，则用 fetchall()
    result_all=curs.fetchall()
    return result

if __name__ == '__main__':
    print(connDb())
