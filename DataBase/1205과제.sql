-- 1번 SQL문으로  user 10명 생성
Insert into users (first_name, last_name, email, password, address, contact, gender, is_active, is_staff) values
	('sung', 'lee', 'q@oz.com', 'qwer', '서울', '010-1234-1234', 'male', True, False),
    ('bum', 'kim', 'w@oz.com', 'wqwe', '인천', '010-4312-4312', 'male', True, False),
    ('nug', 'ra', 'e@oz.com', 'eqrw', '경기', '010-3124-3124', 'female',False, True),
    ('hyun', 'kim', 'r@oz.com', 'asva', '부천', '010-6123-4122', 'male', True, False),
    ('ha', 'ha', 'a@oz.com', 'wzxc', '부산', '010-9873-4712', 'male', True, False),
    ('hong', 'ro', 's@oz.com', 'wqwe', '울산', '010-8731-4362', 'male', False, True),
    ('sunk', 'yu', 'd@oz.com', 'ngtq', '전남', '010-6562-7983', 'female', True, False),
    ('gun', 'gang', 'f@oz.com', 'ppiu', '제주', '010-1111-1111', 'male', True, False),
    ('no', 'nam', 'g@oz.com', 'ppap', '전주', '010-2222-2222', 'female', False, True),
    ('sugung', 'deok', 'h@oz.com', 'asap', '서울', '010-7777-7777', 'male', True, False);
-- 2번 SQL문으로 재고 변동 이력 10개 생성
insert into stocks (raw_material_id,pre_quantity,quantity,change_type,store_id)values
	(1,10,200,'in',10),
	(2,50,10,'returned',9),
	(3,5,5,'in',8),
	(4,50,35,'in',7),
	(5,10,100,'in',6),
	(6,40,50,'in',5),
	(7,25,20,'OUT',4),
	(8,20,35,'IN',3),
	(9,40,60,'IN',2),
	(10,100,70,'OUT',1);
-- 3번 SQL문으로 sales_items 테이블에 데이터 추가하기
insert into sales_items(sales_record_id,product_id,quantity) values (1,8,7);

-- 4번 SQL문으로 products 테이블에 본인만의 시그니처 메뉴 추가하기
insert into products (name, price, description) values
	('와사민트초코콘치즈붕어빵', 99.99, '와사비맛이나다가 치약맛이나다가 달달한초코맛이나는 콘치즈 붕어빵 ');
    
-- 5번 💡SQL문으로 user1과 user2를 각각 매장 id 5와 7에 소속되어있는 직원과 매니저로 변경하기
update employees set store_id = 5, type = 'staff' where id = 1;
	select * from employees where id = 1;
    
update employees set store_id = 7, type = 'manager' where id = 2;
	select * from employees where id = 2;
