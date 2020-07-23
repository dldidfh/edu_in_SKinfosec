CREATE TABLE IF NOT EXISTS major_info(
  major_id	VARCHAR(5) PRIMARY KEY,
  major		VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS student(
  s_id		 VARCHAR(10),
  s_name	 VARCHAR(20) NOT NULL,
  s_age		 INT(3) UNSIGNED,
  major_id	 VARCHAR(5),
  gender	 CHAR(1)  CHECK(gender IN ('F', 'M')), 
  entry_date DATE NOT NULL,
  
  CONSTRAINT student_key PRIMARY KEY (s_id),
  CONSTRAINT student_fk FOREIGN KEY (major_id) REFERENCES major_info(major_id)
);



/**
* INSERT 
**/

INSERT INTO major_info VALUES ( '12071', '소프트웨어');
INSERT INTO major_info(major_id, major) VALUES ('12072','컴퓨터공학');
INSERT INTO major_info VALUES ('12073', '응용컴퓨팅');
COMMIT;
 SELECT * FROM major_info;

# S_ID,S_NAME,S_AGE,MAJOR_ID
INSERT INTO student VALUES('SK001','유용민',28,'12071', 'M','2020/07/01');
INSERT INTO student VALUES('SK002','이재원',27,'12071','M','2020/07/01');
INSERT INTO student VALUES('SK003','이명우',26,'12071','M','2020/07/01');
INSERT INTO student VALUES('SK004','박시형',27,'12071','M','2020/07/01');
INSERT INTO student VALUES('SK005','박보람',25,'12071','F','2020/07/01');

#INSERT INTO student VALUES('SK006','홍길동',25,'12074','M','2020/07/01');
#error : parent key not found
#부모에 데이터 추가 후 자식에 데이터 추가

COMMIT;

#Multi INSERT
DROP TABLE emp;
CREATE TABLE emp AS SELECT * FROM employees WHERE 1=2;

INSERT INTO emp ( SELECT * FROM employees WHERE department_id=50);
SELECT * FROM emp;


/**
*UPDATE
**/
UPDATE student 
SET major_id='12073'
WHERE s_id='SK005';

COMMIT;

#부모 테이블의 데이터 수정시 자식 테이블의 데이터에 영향을 미침
UPDATE major_info
SET major='AI'
WHERE major_id=12071;

ROLLBACK;

#자식의 참조 키 수정시 부모테이블에 존재하는 값만 사용 가능
/*UPDATE student 
SET major_id='12076'
WHERE s_id='SK005';
#error : parents key not found
*/

UPDATE major_info
SET major_id='12074'
WHERE major_id='12072';

#자식 테이블에서 참고하고 있는 데이터 수정시 에러
/*
UPDATE major_info
SET major_id='12075'
WHERE major_id='12071';
#error : child record found 
*/
ROLLBACK;

/**
*DELETE
*/
DELETE student
WHERE s_id='SK006';

SELECT * FROM student;

# 전공이 응용컴퓨팅인 학생 모두 삭제
DELETE student
WHERE major_id=(SELECT major_id 
				 FROM major_info 
				 WHERE major='응용컴퓨팅');

SELECT * FROM student;
ROLLBACK;

# SAVEPOINT TEST
INSERT INTO student VALUES('SK006','홍길동',25,'12071','M','2020/07/01');
UPDATE student SET major_id='12072' WHERE s_id='SK006';

SAVEPOINT ss; #mark

DELETE FROM student WHERE  s_id='SK006';

ROLLBACK TO ss; #mark 된 곳까지 작업취소

COMMIT;#INSERT, UPDATE만 적용
