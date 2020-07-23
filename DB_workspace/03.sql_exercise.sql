/**********************************************************
*	SQL Query & Function Example1
**********************************************************/
/**
-- Employees Table Columns
-- EMPLOYEE_ID
-- FIRST_NAME
-- LAST_NAME
-- EMAIL
-- PHONE_NUMBER
-- HIRE_DATE
-- JOB_ID
-- SALARY
-- COMMISSION_PCT
-- MANAGER_ID
-- DEPARTMENT_ID
**/

--부서번호가 10번인 부서의 사람 중 사원번호, 이름, 월급을 출력하시오
SELECT employee_id 사원번호, first_name 이름, salary 월급
FROM employees 
WHERE department_id=10;


/**
--결과 
사원번호 이름                                           월급
-------- ---------------------------------------- ----------
     200 Jennifer                                       4400
*/

--사원번호가 200인 사람 중 이름, 입사일, 부서 번호를 출력하시오.
SELECT first_name 이름, hire_date 입사일, department_id 부서번호
FROM employees
WHERE employee_id=200;

/**
이름                                     입사일     부서번호
---------------------------------------- -------- ----------
Jennifer                                 03/09/17         10
*/


--이름이 Ellen인 사람의 모든 정보를 출력하시오.
SELECT * FROM employees
WHERE UPPER(first_name)='ELLEN';




--입사일이 08/04/21인 사원의 이름, 부서번호, 월급을 출력하시오.
SELECT first_name 이름, department_id 부서번호, salary 월급
FROM employees
WHERE hire_date='08/04/21';
/**
이름                                       부서번호       월급
---------------------------------------- ---------- ----------
Amit                                             80       6200
Sundita                                          80       6100
*/




--직무가 SA_MAN 아닌 사람의 모든 정보를 출력하시오.
SELECT *
FROM employees
WHERE job_id='SA_MAN';


--입사일이 08/04/21 이후에 입사한 사원의 정보를 출력하시오.
 SELECT *
 FROM employees
 WHERE hire_date>'08/04/21';


--부서번호와 20,30번을 제외한 모든 사람의 이름, 사원번호, 부서번호를 출력하시오.
SELECT first_name 이름, employee_id 사원번호, department_id 부서번호
FROM employees
WHERE department_id NOT IN(20,30);



--이름이 S로 시작하는 사원의 사원번호, 이름, 입사일, 부서번호를 출력하시오.
SELECT employee_id 사원번호, hire_date 입사일,department_id 부서번호
FROM employees
WHERE LOWER(first_name) LIKE 's%';


--이름이 s로 시작하고 마지막 글자가 t인 사람이 정보를 출력하시오.
SELECT *
FROM employees
WHERE LOWER(first_name) LIKE 's%t';




/**
employees 테이블에서 이름, 급여, 상여, 총액을 구하여 총액 많은 순서로 출력하라 단 상여금이 NULL인 사람은 제외

*/
 SELECT first_name 이름, salary 급여, salary*COMMISSION_PCT 상여, salary+NVL((salary*COMMISSION_PCT),0) 총액
 FROM employees
 WHERE COMMISSION_PCT IS NOT NULL
 ORDER BY 총액 DESC;



/**
10번 부서의 모든 사람들에게 급여의 13%를 보너스로 지불하기로 하였다. 이름, 급여, 보너스금액, 부서번호를 출력하시오.
**/
SELECT first_name 이름, salary 급여, salary*0.13 보너스금액, department_id 부서번호
FROM employees
WHERE department_id=10;


/**
30번 부서의 연봉을 계산하여 이름, 부서번호, 급여, 연봉을 출력하시오. 단 연말에 급여의 150%를 보너스로 지급한다.
   -- 연봉 = salary*12+(salary*1.5)
**/

SELECT first_name 이름,department_id 부서번호, salary 급여, salary*12+(salary*1.5) 연봉
FROM employees
WHERE department_id=30;


/**
부서번호가 20인 부서의 시간당 임금을 계산하여 출력하시오. 단 1달의 근무일수는 12일이고 1일 근무시간은 5시간이다.
출력양식은 이름, 급여, 시간당 임금(소수이하 1번째 자리에서 반올림)을 출력하시오.
   -- 시급 = sal/일수/시간  -> sal/ 12/5 
   -- round(m, n) m을 소수점 n자리에서 반올림 
**/
 SELECT ROUND(salary/12/5,1) 시급
 FROM employees
 WHERE department_id=20;



/**
급여가 1500부터 3000사이의 사람은 급여의 5%를 회비로 지불하기로 하였다. 이를 이름, 급여, 회비(-2자리에서 반올림)를 출력하시오.
	-- 회비  = sal * 0.05	
	-- -2자리에서 반올림 : 정수 2번째 자리에서 반올림.. 100단위로  
**/
SELECT first_name 이름,salary 급여, ROUND(salary*0.05,-2) 회비
FROM employees
WHERE salary BETWEEN 1500 AND 3000;




/**
입사일부터 지금까지의 날짜수를 출력하시오. 부서번호, 이름, 입사일, 현재일, 근무일수(소수점이하절삭), 근무년수,
 근무월수(30일 기준)를 출력하시오.
	-- 지금 날짜 : sysdate 
	-- 근무 일수 : 현재날짜 - 입사일 = sysdate - hire_date  -> 날짜 - 날짜 : 일수 나옴
	-- 근무 년수 : to_char(sysdate,'YYYY')-to_char(hiredate,'YYYY')
	-- 근무 월수 : 근무일수 / 1달(30일)
**/
SELECT department_id 부서번호, first_name 이름, hire_date 입사일, sysdate 현재일,
       ROUND(sysdate-hire_date, 0) 근무일수,
       TO_CHAR(sysdate,'YYYY')-TO_CHAR(hire_date,'YYYY') 근무년수,
       (ROUND((sysdate-hire_date)/30, 0)) 근무월수
FROM employees;  



/**
입사일로부터 오늘까지의 일수를 구하여 이름, 입사일, 근무일수를 출력하시오.
--ROUND(sysdate-hire_date,0) 근무일수
**/
SELECT first_name 이름, hire_date 입사일, ROUND(sysdate-hire_date,0) 근무일수
from employees;


/**
입사일을 2012년 7월 5일의 형태로 이름, 입사일을 출력하시오.
	-- 날짜 형식 앞에 fm 은 선행 '0'을 표현하지 않는다는 뜻.. 
	-- 'fmYYYY"년" MM"월" DD"일' 
**/
SELECT first_name 이름, TO_CHAR(hire_date,'fmYYYY"년" MM"월" DD"일"') 입사일
from employees;




/**
이름(first_name)의 글자수가 6자이상인 사람의 이름을 앞에서 3자만 구하여 소문자로 이름만을 출력하시오.
	-- substr(str, position, length) : str 문자를 positin 부터 length길이 만큼 표현
	-- lower(str)  소문자 변환
	-- length(str)  str의 길이
**/
SELECT LOWER(SUBSTR(first_name,1,3)) 소문자
FROM employees
WHERE length(first_name) >=6;


