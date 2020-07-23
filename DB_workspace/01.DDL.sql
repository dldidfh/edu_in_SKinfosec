/**
* Table 생성
*/
#기존 테이블로 테이블 생성하기
CREATE TABLE emp 
AS( SELECT employee_id, first_name, hire_date, salary, job_id, department_id
    FROM employees
);

#컬럼명과 데이터 확인
show columns from emp;
SELECT * FROM emp;

#제약사항 확인 - 제약사항은 복사 제외
SELECT * FROM Information_schema.table_constraints WHERE TABLE_NAME='emp';
 
#제약사항 추가
ALTER TABLE emp ADD CONSTRAINT emp_pk PRIMARY KEY (employee_id);


#테이블 생성
CREATE TABLE student(
  s_id		VARCHAR(10)  PRIMARY KEY,
  s_name	VARCHAR(20) NOT NULL,
  s_age		INT(3) UNSIGNED,
  major		VARCHAR(30) NOT NULL,
  gender	CHAR(1) CHECK(gender IN ('F','M')),
  entry_date	DATE NOT NULL
);


CREATE TABLE major_info(
  major_id	INT(5) PRIMARY KEY,
  major		VARCHAR(30) NOT NULL
);


show columns from student;         #desc hr.student  #desc student
show columns from major_info;

#제약사항 확인
SELECT * FROM Information_schema.table_constraints WHERE TABLE_NAME='student'

/**
* Table 수정
//COLUMN 추가
ALTER TABLE [테이블 명] ADD COLUMN [컬럼명 타입 제약조건];

//COLUMN 변경
ALTER TABLE [테이블 명] MODIFY COLUMN [컬럼명 타입 제약조건];

//COLUMN 이름까지 변경
ALTER TABLE [테이블명] CHANGE COLUMN [컬럼명 변경컬럼명 타입 제약조건]; 

//COLUMN 삭제
ALTER TABLE [테이블명] DROP COLUMN [컬럼명]

// 제약조건 삭제
ALTER TABLE [테이블 명] DROP CONSTRAINT [제약조건 이름];
ALTER TABLE [테이블 명] DROP FOREIGN KEY [제약조건 이름];

// 제약조건 추가
외래키 : ALTER TABLE [테이블 명] ADD CONSTRAINT [제약조건 이름] FOREIGN KEY(컬럼 명)
 REFERENCES [부모테이블 명](PK 컬럼 명) [ON DELETE CASCADE / ON UPDATE CASCADE];

기본키 : ALTER TABLE [테이블 명] ADD CONSTRAINT [제약조건 이름] PRIMARY KEY(컬럼 명);

// NOT NULL 제약 조건 추가
ALTER TABLE [테이블 명] MODIFY [컬럼 명] [데이터 타입] CONSTRAINT [제약조건 이름] NOT NULL;
**/

#Column이름 수정
ALTER TABLE student CHANGE COLUMN major major_id VARCHAR(30) NOT NULL;

#Column Type 수정
ALTER TABLE student MODIFY COLUMN major_id INT(5);

#제약사항 추가
ALTER TABLE student ADD CONSTRAINT student_fk_majorId
FOREIGN KEY(major_id) REFERENCES major_info(major_id) ON DELETE CASCADE;

#확인
SELECT * FROM Information_schema.table_constraints WHERE TABLE_NAME='student'

/**
*Table 삭제
*/
DROP TABLE student,major_info;







