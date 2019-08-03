import pymysql
# 1. 连接DB
def db_connect():
    db=pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        charset="utf8"
    )

    cursor=db.cursor()
    cursor.execute("SELECT VERSION()")
    data=cursor.fetchone()
    print("DB version is: %s" %data)
    db.close()

def main():
    db_connect()
if __name__=="__main__":
    main()

# 2. 创建数据库表
