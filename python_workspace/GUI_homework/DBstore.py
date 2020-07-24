import pymysql.cursors
from domain import AIEntity 
class AIStore:
    connection=None
    #Connection pool : 사용자 : method단위 connection 맺고 close 하고 매소드 마다 
    #DB 연결
    def __init__(self):
        #pool 스면 여기서 connection pool 객체 생성 

        AIStore.connection = db = pymysql.connect(
                    host='localhost',
                    port=3306, 
                    db='aidb', 
                    user='test', 
                    passwd='123123', 
                    charset='utf8',
                    cursorclass = pymysql.cursors.DictCursor
                )
    #DB 연결 종료 
    def close(self):
        AIStore.connection.close()

    def insert(self,ai_entity):
        #connection pool 객체 얻기 
        try:
            with AIStore.connection.cursor() as cursor:
                sql = """INSERT INTO `member` (`name`,`age`, `email`, `major`) 
                        VALUES (%s, %s,%s,%s)"""
                cursor.execute(sql, (ai_entity.name,ai_entity.age,ai_entity.email,ai_entity.major))
                AIStore.connection.commit()
        finally:
            pass
            # connection pool 에 객체 반납 하기 
            #     AIStore.close()

    def select_all(self):
        try:
            with AIStore.connection.cursor() as cursor:
                sql = """select * from `member`"""
                cursor.execute(sql)
                result = cursor.fetchall()
                
        finally:
            pass
        return result

    def update(self,ai_entity):
        try:
            with AIStore.connection.cursor() as cursor:
                sql = """update `member` set `name`=%s, `age`=%s, `major`=%s where `email`=%s"""
                cursor.execute(sql, (ai_entity.name,ai_entity.age,ai_entity.major,ai_entity.email))
                AIStore.connection.commit()
        finally:
            pass

    def delete(self,email):
        try:
            with AIStore.connection.cursor() as cursor:
                sql = """delete from `member` where `email`=%s"""
                cursor.execute(sql, (email))
                AIStore.connection.commit()
        finally:
            pass


    def select_by_email(self,email):
        try:
            with AIStore.connection.cursor() as cursor:
                sql = """select * from `member` where `email`=%s"""
                cursor.execute(sql,email)
                result = cursor.fetchone()
                
        finally:
            pass
        return result


# test = AIStore()
# test.insert(AIEntity("김주희",24,"qweqwe@email.com","전공은무엇"))
# #print(test.select_all())
# #test.update(AIEntity("김asdasd희",24,"전공은무엇","qweqwe@email.com"))
# #test.delete("qweqwe@email.com")
# print(test.select_by_email("qweqwe@email.com"))

#test.select_by_email
