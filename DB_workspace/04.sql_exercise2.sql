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
50�� �μ� ������ ��դ� �ְ�, ����, �ο����� ���Ͽ� ����Ͻÿ�.
**/
SELECT avg(salary) ���, MAX(salary)�ְ�, MIN(salary)����, COUNT(department_id) �ο���
FROM employees
GROUP BY department_id
HAVING department_id=50;


/**
�� �μ��� �޿��� ���, �ְ�, ����, �ο����� ���Ͽ� ����Ͻÿ�..
**/
SELECT avg(salary) ���, MAX(salary)�ְ�, MIN(salary)����, COUNT(department_id) �ο���
FROM employees
GROUP BY department_id;


/**
�� �μ��� ���� ������ �ϴ� ����� �ο����� ���Ͽ� �μ���ȣ, ������, �ο����� ����Ͻÿ�.
**/
SELECT department_id �μ���ȣ, job_id ����, COUNT(job_id) �ο���
FROM employees
GROUP BY department_id, job_id;



/**
���� ������ �ϴ� ����� ���� 4�� �̻��� ������ �ο����� ����Ͻÿ�.
**/
SELECT job_id ����, COUNT(job_id) �ο���
FROM employees
GROUP BY job_id
HAVING COUNT(job_id) >= 4;


/**
�� �μ��� ��տ���, ��ü����, �ְ����, ��������,�� ���Ͽ� ��տ����� ���������� ����Ͻÿ�.
**/
SELECT department_id �μ���ȣ, AVG(salary) ��տ���, SUM(salary) ��ü����, MAX(salary) �ְ����, MIN(salary) ��������
FROM employees
GROUP BY department_id
ORDER BY ��տ��� DESC;


/**
 �μ���ȣ, �μ���, �̸�, �޿��� ����Ͻÿ�.
**/
SELECT e.department_id �μ���ȣ, d.department_name �μ���, e.first_name �̸�, e.salary �޿�
FROM employees e, department d
WHERE e.department_id=d.department_id;


SELECT e.department_id �μ���ȣ, d.department_name �μ���, e.first_name �̸�, e.salary �޿�
FROM employees e
JOIN department d ON (e.department_id=d.department_id);

/**
�̸��� adam�� ����� �μ����� ����Ͻÿ�.
**/
SELECT   e.first_name, d.department_name �μ���
FROM employees e, departments d
WHERE e.department_id=d.department_id AND LOWER(e.first_name)='adam';


/**
employees���̺� �ִ� employee_id�� manager_id�� �̿��Ͽ� ������ ���踦 ������ ���� ����Ͻÿ�
'smith'�� �Ŵ����� 'ford'�̴�.
**/
SELECT e.first_name||'�� �Ŵ����� '||e2.first_name||'�̴�.' �Ŵ����������
FROM employees e, employees e2
WHERE e.manager_id=e2.employee_id;


/**
adam�� ������ ���� ������ ���� ����� �̸�, �μ���, �޿�, ������ ����Ͻÿ�.
**/
SELECT e.first_name �̸�, d.department_name �μ���, e.salary �޿�, e.job_id ����
FROM employees e, departments d
WHERE e.department_id=d.department_id 
      AND job_id=(SELECT job_id 
		  FROM employees 
		  WHERE UPPER(first_name)='ADAM');

/**
��ü ����� ��� �ӱݺ��� ���� ����� �����ȣ, �̸�, �μ���, �Ի���, ����, �޿��� ����Ͻÿ�.
**/
SELECT e.employee_id �����ȣ, e.first_name �̸�, d.department_name �μ���, 
       e.hire_date �Ի���, l.city ����, e.salary �޿�
FROM employees e, departments d, locations l
WHERE e.department_id=d.department_id
      AND d.location_id=l.location_id
      AND e.salary > (SELECT AVG(salary)FROM employees);
		      

/**
50�� �μ������ �߿��� 30�� �μ��� ����� ���� ������ �ϴ� ����� �����ȣ, �̸�, �μ���, �Ի����� ����Ͻÿ�.
**/
SELECT e.employee_id �����ȣ, e.first_name �̸�, d.department_name �μ���, e.hire_date �Ի���
FROM employees e, departments d
WHERE e.department_id=d.department_id 
      AND e.job_id IN (SELECT job_id FROM employees WHERE department_id=30) 
      AND e.department_id=50;


/**
�޿��� 30�� �μ��� �ְ� �޿����� ���� ����� �����ȣ, �̸�, �޿��� ����Ͻÿ�.
**/
SELECT employee_id �����ȣ, first_name �̸�, salary �޿�
FROM employees
WHERE salary > (SELECT MAX(salary) FROM employees WHERE department_id=30);