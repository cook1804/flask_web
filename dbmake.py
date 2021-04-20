import pymysql
# db 접속 하기위에 connect 메소드 사용. 
db = pymysql.connect(             
    host ='localhost',
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'busan' 
)

sql = '''
    CREATE TABLE `topic` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`title` varchar(100) NOT NULL,
	`body` text NOT NULL,
	`author` varchar(30) NOT NULL,
    `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
	) ENGINE=innoDB DEFAULT CHARSET=utf8;
'''
# sql_1 = "INSERT INTO `busan`.`topic` (`title`, `body`, `author`) VALUES ('부산', '와서 갈매기', '김태경');"

cursor = db.cursor()    # 쿼리문을 날릴 수 있는 준비라고 생각하면된다. 이거 먼저 써야 쿼리문 쓸 수 있다
# cursor.execute(sql)

# cursor.execute(sql_1)
# db.commit()
# db.close()

# cursor.execute('SELECT * FROM users;')  # excute 메소드 안에 쿼리문을 적어준다. 쿼리문을 실행시키는 메소드!
cursor.execute('SELECT * FROM topic;')
users = cursor.fetchall() # 조회한것을 리턴해오는 메소드(모든 데이터 한번에 가져올때 사용) fetchall, 조회하기 위해 fetchall 해줘야 함!
print(cursor.rowcount ,users)


#숙제 username :영어로 , mail : , name :한글로 ,passwd :12345
# sql_2 = "INSERT INTO `busan`.`users` (`name`, `email`, `username`, `password`) VALUES ('Yoo Ji Won', 'cook1804@naver.com', '유지원', '12345');"
# cursor = db.cursor()
# cursor.execute(sql_2)
# db.commit()   #db에 커밋한다.
# db.close()    # db에 쿼리문이 계속 날라갈 수 있으니, close 메소드 사용.

sql_1 = "INSERT INTO `busan`.`topic` (`title`, `body`, `author`) VALUES ('부산', '와서 갈매기', '김태경');"
# sql_3 = "INSERT INTO `busan`.`topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
# title = input('제목을 적으세요: ')
# body = input('내용을 적으세요: ')
# author = input("누구세요?: ")
# input_data = [title,body,author]

# cursor = db.cursor()
# cursor.execute(sql_3,input_data)
# db.commit()
# db.close()
