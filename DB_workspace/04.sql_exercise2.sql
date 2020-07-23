/**********************************************************
*	SQL Query & Function Example2
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

/**
--Departments Table Columns
--DEPARTMENT_ID
--DEPARTMENT_NAME
--MANAGER_ID
--LOCATION_ID
**/

/**
50번 부서 월급의 평균ㅡ 최고, 최저, 인원수를 구하여 출력하시오.
**/
SELECT avg(salary) 평균, MAX(salary)최고, MIN(salary)최저, COUNT(department_id) 인원수
FROM employees
GROUP BY department_id
HAVING department_id=50;


/**
각 부서별 급여의 평균, 최고, 최저, 인원수를 구하여 출력하시오..
**/
SELECT avg(salary) 평균, MAX(salary)최고, MIN(salary)최저, COUNT(department_id) 인원수
FROM employees
GROUP BY department_id;


/**
각 부서별 같은 업무를 하는 사람의 인원수를 구하여 부서번호, 업무명, 인원수를 출력하시오.
**/
SELECT department_id 부서번호, job_id 직무, COUNT(job_id) 인원수
FROM employees
GROUP BY department_id, job_id;



/**
같은 업무를 하는 사람의 수가 4명 이상인 업무와 인원수를 출력하시오.
**/
SELECT job_id 직무, COUNT(job_id) 인원수
FROM employees
GROUP BY job_id
HAVING COUNT(job_id) >= 4;


/**
각 부서별 평균월급, 전체월급, 최고월급, 최저월급,을 구하여 평균월급이 많은순으로 출력하시오.
**/
SELECT department_id 부서번호, AVG(salary) 평균월급, SUM(salary) 전체월급, MAX(salary) 최고월급, MIN(salary) 최저월급
FROM employees
GROUP BY department_id
ORDER BY 평균월급 DESC;


/**
 부서번호, 부서명, 이름, 급여를 출력하시오.
**/
SELECT e.department_id 부서번호, d.department_name 부서명, e.first_name 이름, e.salary 급여
FROM employees e, department d
WHERE e.department_id=d.department_id;


SELECT e.department_id 부서번호, d.department_name 부서명, e.first_name 이름, e.salary 급여
FROM employees e
JOIN department d ON (e.department_id=d.department_id);

/**
이름이 adam인 사원의 부서명을 출력하시오.
**/
SELECT   e.first_name, d.department_name 부서명
FROM employees e, departments d
WHERE e.department_id=d.department_id AND LOWER(e.first_name)='adam';


/**
employees테이블에 있는 employee_id와 manager_id를 이용하여 서로의 관계를 다음과 같이 출력하시오
'smith'의 매니저는 'ford'이다.
**/
SELECT e.first_name||'의 매니저는 '||e2.first_name||'이다.' 매니저정보출력
FROM employees e, employees e2
WHERE e.manager_id=e2.employee_id;


/**
adam의 직무와 같은 직무를 갖는 사람의 이름, 부서명, 급여, 직무를 출력하시오.
**/
SELECT e.first_name 이름, d.department_name 부서명, e.salary 급여, e.job_id 직무
FROM employees e, departments d
WHERE e.department_id=d.department_id 
      AND job_id=(SELECT job_id 
		  FROM employees 
		  WHERE UPPER(first_name)='ADAM');

/**
전체 사원의 평균 임금보다 많은 사원의 사원번호, 이름, 부서명, 입사일, 지역, 급여를 출력하시오.
**/
SELECT e.employee_id 사원번호, e.first_name 이름, d.department_name 부서명, 
       e.hire_date 입사일, l.city 지역, e.salary 급여
FROM employees e, departments d, locations l
WHERE e.department_id=d.department_id
      AND d.location_id=l.location_id
      AND e.salary > (SELECT AVG(salary)FROM employees);
		      

/**
50번 부서사람들 중에서 30번 부서의 사원과 같은 업무를 하는 사원의 사원번호, 이름, 부서명, 입사일을 출력하시오.
**/
SELECT e.employee_id 사원번호, e.first_name 이름, d.department_name 부서명, e.hire_date 입사일
FROM employees e, departments d
WHERE e.department_id=d.department_id 
      AND e.job_id IN (SELECT job_id FROM employees WHERE department_id=30) 
      AND e.department_id=50;


/**
급여가 30번 부서의 최고 급여보다 높은 사원의 사원번호, 이름, 급여를 출력하시오.
**/
SELECT employee_id 사원번호, first_name 이름, salary 급여
FROM employees
WHERE salary > (SELECT MAX(salary) FROM employees WHERE department_id=30);