import pymysql.cursors
from domain import ProEntity 
class ProStore:
    connection=None
    def __init__(self):

        ProStore.connection = pymysql.connect(
                    host='localhost',
                    port=3306, 
                    db='aidb', 
                    user='test', 
                    passwd='123123', 
                    charset='utf8',
                    cursorclass = pymysql.cursors.DictCursor
                )

    def close(self):
        ProStore.connection.close()

    def insert(self,proBean):

        try:
            with ProStore.connection.cursor() as cursor:
                sql = """INSERT INTO `product` (`proName`,`proPrice`, `proWeight`, `proSize`) 
                        VALUES (%s,%s,%s,%s)"""
                cursor.execute(sql, (proBean.proName,proBean.proPrice,proBean.proWeight,proBean.proSize))
                ProStore.connection.commit()
        finally:
            pass

    def select_all(self):
        try:
            with ProStore.connection.cursor() as cursor:
                sql = """select * from `product`"""
                cursor.execute(sql)
                result = cursor.fetchall()
                
        finally:
            pass
        return result

    def update(self,proBean):
        try:
            with ProStore.connection.cursor() as cursor:
                sql = """update `product` set `proName`=%s, `proPrice`=%s, `proSize`=%s where `proWeight`=%s"""
                cursor.execute(sql, (proBean.proName,proBean.proPrice,proBean.proSize,proBean.proWeight))
                ProStore.connection.commit()
        finally:
            pass

    def delete(self,proName):
        try:
            with ProStore.connection.cursor() as cursor:
                sql = """delete from `product` where `proName`=%s"""
                cursor.execute(sql, (proName))
                ProStore.connection.commit()
        finally:
            pass


    def select_by_proName(self,proName):
        try:
            with ProStore.connection.cursor() as cursor:
                sql = """select * from `product` where `proName`=%s"""
                cursor.execute(sql,proName)
                result = cursor.fetchone()
                
        finally:
            pass
        return result
     

# test = ProStore()
# test.insert(ProEntity("김주희",24,"qweqwe@proWeight.com","전공은무엇"))
# #print(test.select_all())
# #test.update(ProEntity("김asdasd희",24,"전공은무엇","qweqwe@proWeight.com"))
# #test.delete("qweqwe@proWeight.com")
# print(test.select_by_proWeight("qweqwe@proWeight.com"))

#test.select_by_proWeight
