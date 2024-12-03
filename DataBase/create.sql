-- 생성 초급 
-- (1) customers 테이블에 새 고 객을 추가하세요.
insert into customers (name, age) values("나천보", 20);
-- (2) products 테이블에 새 제품을 추가하세요.
insert into products (productsID, productsName) values(001, "apple");
-- (3) employees 테이블에 새 직원을 추가하세요.
insert into employees (employeesID, name, age) values(007, "이박김", 27);
-- (4) office 테이블에 새 사무실을 추가하세요.
insert into office (officeName, city, number) values("겁쟁이쉼터", "seoul", 021231234);
-- (5) orders 테이블에 새 주문 추가하세요.
insert into orders (ordersName, orderEA) values ("apple", 3);
-- (6) orderdetails 테이블에 주문 상세 정보를 추가하세요.
insert into orderdetails ( ordersName, ordersDay) values ("apple", "12/03");
-- (7) payments 테이블에 지불 정보를 추가하세요.
insert into payments (orderpay, orederEA , total) values ("1000원", 3 , "3000원");
-- (8) productlines 테이블에 제품 라인을 추가하세요.
insert into productlines (productline, explanation) values ("fish", "물고기 팝니다");
-- (9) customers 테이블에 다른 지역의 고객을 추가하세요.
insert into customers (name, age, city) values ("천보나", 52, "KIMPO");
-- (10) products 테이블에 다른 카테고리의 제품을 추가하세요.
INSERT INTO products (productsID, productsName, productsPrice, productLine) VALUES (526, "고등어", 7000 , 'fish');


-- 읽기 초급
-- (1) customers 테이블에서 모든 고객 정보를 조회하세요.
select * from customers;
-- (2) products 테이블에서 모든 제품 목록을 조회하세요.
select productname from products;
-- (3) employees 테이블에서 모든 직원의 이름과 직급을 조회하세요.
select name, jobtitle from employees;
-- (4) offices 테이블에서 모든 사무실의 위치를 조회하세요.
select officeName, city, number from office;
-- (5) orders 테이블에서 최근 10개의 주문을 조회하세요.
SELECT * FROM orders ORDER BY orderEA DESC LIMIT 10;
-- (6) orderdetails 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
SELECT * FROM orders WHERE orderName = 1;
-- (7) payments 테이블에서 특정 고객의 모든 지불 정보를 조회하세요
SELECT * FROM payments WHERE total = 1
-- (8) productlines 테이블에서 각 제품 라인의 설명을 조회하세요
select productline, explanation from productlines;
-- (9) customers 테이블에서 특정 지역의 고객을 조회하세요.
select * from customers where city = "KIMPO";
-- (10) products 테이블에서 특정 가격 범위의 제품을 조회하세요.
select * from products where 5000 < productsPrice > 10000;




























