import pymysql
import pymysql.cursors

connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='abcdefg',
    db='airbnb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    # # 문제1 : 새로운 제품 추가
    # sql = "INSERT INTO Products(productName, price, stockQuantity) VALUES(%s, %s, %s)"
    # cursor.execute(sql, ('pythonBook', 10000, 10))
    # connection.commit()

    # # 문제2 : 목록 조회
    # cursor.execute("select * from products")
    # for book in cursor.fetchall():
    #     print(book)

    # # 문제3 : 제품 재고 업데이트
    # sql = "update products set stockQuantity = stockQuantity - %s where productID = %s"
    # cursor.execute(sql, (1, 1))
    # connection.commit()

    # 문제4 : 고객별 총 주문 금액
    # sql = "SELECT customerid, sum(totalAmount) as totalAmount from Orders GROUP BY customerid "
    # cursor.execute(sql)
    # data = cursor.fetchall()
    # print(data)

    #문제5 : 고객 이메일 업데이트
    # sql = "update Customers SET email=%s WHERE customerid=%s"
    # cursor.execute(sql, ('update@update.com',1))
    # connection.commit()

    # #문제6 : 주문 취소
    # sql = "delete from orders where orderId = %s"
    # cursor.execute(sql, (15))
    # connection.commit()

    # 문제 7 : 특정 제품 검색
    # sql = "select * from products where productName LIKE %s"
    # cursor.execute(sql, ('%book%'))
    # datas = cursor.fetchall()

    #문제 8 : 특정 고객의 주문 데이터 조회
    # sql = "select * from orders where customerID = %s"
    # cursor.execute(sql, (1))
    # datas = cursor.fetchall()
    
    # for data in datas:
    #     print(data)

    #문제 9 : 가장 많이 주문한 고객
    # sql = "select customerID, count(*) as ordercount from orders group by customerID order by ordercount desc limit 1"
    # cursor.execute(sql)
    # data = cursor.fetchone()
    # print(data)

cursor.close()