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

--�μ���ȣ�� 10���� �μ��� ��� �� �����ȣ, �̸�, ������ ����Ͻÿ�
SELECT employee_id �����ȣ, first_name �̸�, salary ����
FROM employees 
WHERE department_id=10;


/**
--��� 
�����ȣ �̸�                                           ����
-------- ---------------------------------------- ----------
     200 Jennifer                                       4400
*/

--�����ȣ�� 200�� ��� �� �̸�, �Ի���, �μ� ��ȣ�� ����Ͻÿ�.
SELECT first_name �̸�, hire_date �Ի���, department_id �μ���ȣ
FROM employees
WHERE employee_id=200;

/**
�̸�                                     �Ի���     �μ���ȣ
---------------------------------------- -------- ----------
Jennifer                                 03/09/17         10
*/


--�̸��� Ellen�� ����� ��� ������ ����Ͻÿ�.
SELECT * FROM employees
WHERE UPPER(first_name)='ELLEN';




--�Ի����� 08/04/21�� ����� �̸�, �μ���ȣ, ������ ����Ͻÿ�.
SELECT first_name �̸�, department_id �μ���ȣ, salary ����
FROM employees
WHERE hire_date='08/04/21';
/**
�̸�                                       �μ���ȣ       ����
---------------------------------------- ---------- ----------
Amit                                             80       6200
Sundita                                          80       6100
*/




--������ SA_MAN �ƴ� ����� ��� ������ ����Ͻÿ�.
SELECT *
FROM employees
WHERE job_id='SA_MAN';


--�Ի����� 08/04/21 ���Ŀ� �Ի��� ����� ������ ����Ͻÿ�.
 SELECT *
 FROM employees
 WHERE hire_date>'08/04/21';


--�μ���ȣ�� 20,30���� ������ ��� ����� �̸�, �����ȣ, �μ���ȣ�� ����Ͻÿ�.
SELECT first_name �̸�, employee_id �����ȣ, department_id �μ���ȣ
FROM employees
WHERE department_id NOT IN(20,30);



--�̸��� S�� �����ϴ� ����� �����ȣ, �̸�, �Ի���, �μ���ȣ�� ����Ͻÿ�.
SELECT employee_id �����ȣ, hire_date �Ի���,department_id �μ���ȣ
FROM employees
WHERE LOWER(first_name) LIKE 's%';


--�̸��� s�� �����ϰ� ������ ���ڰ� t�� ����� ������ ����Ͻÿ�.
SELECT *
FROM employees
WHERE LOWER(first_name) LIKE 's%t';




/**
employees ���̺��� �̸�, �޿�, ��, �Ѿ��� ���Ͽ� �Ѿ� ���� ������ ����϶� �� �󿩱��� NULL�� ����� ����

*/
 SELECT first_name �̸�, salary �޿�, salary*COMMISSION_PCT ��, salary+NVL((salary*COMMISSION_PCT),0) �Ѿ�
 FROM employees
 WHERE COMMISSION_PCT IS NOT NULL
 ORDER BY �Ѿ� DESC;



/**
10�� �μ��� ��� ����鿡�� �޿��� 13%�� ���ʽ��� �����ϱ�� �Ͽ���. �̸�, �޿�, ���ʽ��ݾ�, �μ���ȣ�� ����Ͻÿ�.
**/
SELECT first_name �̸�, salary �޿�, salary*0.13 ���ʽ��ݾ�, department_id �μ���ȣ
FROM employees
WHERE department_id=10;


/**
30�� �μ��� ������ ����Ͽ� �̸�, �μ���ȣ, �޿�, ������ ����Ͻÿ�. �� ������ �޿��� 150%�� ���ʽ��� �����Ѵ�.
   -- ���� = salary*12+(salary*1.5)
**/

SELECT first_name �̸�,department_id �μ���ȣ, salary �޿�, salary*12+(salary*1.5) ����
FROM employees
WHERE department_id=30;


/**
�μ���ȣ�� 20�� �μ��� �ð��� �ӱ��� ����Ͽ� ����Ͻÿ�. �� 1���� �ٹ��ϼ��� 12���̰� 1�� �ٹ��ð��� 5�ð��̴�.
��¾���� �̸�, �޿�, �ð��� �ӱ�(�Ҽ����� 1��° �ڸ����� �ݿø�)�� ����Ͻÿ�.
   -- �ñ� = sal/�ϼ�/�ð�  -> sal/ 12/5 
   -- round(m, n) m�� �Ҽ��� n�ڸ����� �ݿø� 
**/
 SELECT ROUND(salary/12/5,1) �ñ�
 FROM employees
 WHERE department_id=20;



/**
�޿��� 1500���� 3000������ ����� �޿��� 5%�� ȸ��� �����ϱ�� �Ͽ���. �̸� �̸�, �޿�, ȸ��(-2�ڸ����� �ݿø�)�� ����Ͻÿ�.
	-- ȸ��  = sal * 0.05	
	-- -2�ڸ����� �ݿø� : ���� 2��° �ڸ����� �ݿø�.. 100������  
**/
SELECT first_name �̸�,salary �޿�, ROUND(salary*0.05,-2) ȸ��
FROM employees
WHERE salary BETWEEN 1500 AND 3000;




/**
�Ի��Ϻ��� ���ݱ����� ��¥���� ����Ͻÿ�. �μ���ȣ, �̸�, �Ի���, ������, �ٹ��ϼ�(�Ҽ�����������), �ٹ����,
 �ٹ�����(30�� ����)�� ����Ͻÿ�.
	-- ���� ��¥ : sysdate 
	-- �ٹ� �ϼ� : ���糯¥ - �Ի��� = sysdate - hire_date  -> ��¥ - ��¥ : �ϼ� ����
	-- �ٹ� ��� : to_char(sysdate,'YYYY')-to_char(hiredate,'YYYY')
	-- �ٹ� ���� : �ٹ��ϼ� / 1��(30��)
**/
SELECT department_id �μ���ȣ, first_name �̸�, hire_date �Ի���, sysdate ������,
       ROUND(sysdate-hire_date, 0) �ٹ��ϼ�,
       TO_CHAR(sysdate,'YYYY')-TO_CHAR(hire_date,'YYYY') �ٹ����,
       (ROUND((sysdate-hire_date)/30, 0)) �ٹ�����
FROM employees;  



/**
�Ի��Ϸκ��� ���ñ����� �ϼ��� ���Ͽ� �̸�, �Ի���, �ٹ��ϼ��� ����Ͻÿ�.
--ROUND(sysdate-hire_date,0) �ٹ��ϼ�
**/
SELECT first_name �̸�, hire_date �Ի���, ROUND(sysdate-hire_date,0) �ٹ��ϼ�
from employees;


/**
�Ի����� 2012�� 7�� 5���� ���·� �̸�, �Ի����� ����Ͻÿ�.
	-- ��¥ ���� �տ� fm �� ���� '0'�� ǥ������ �ʴ´ٴ� ��.. 
	-- 'fmYYYY"��" MM"��" DD"��' 
**/
SELECT first_name �̸�, TO_CHAR(hire_date,'fmYYYY"��" MM"��" DD"��"') �Ի���
from employees;




/**
�̸�(first_name)�� ���ڼ��� 6���̻��� ����� �̸��� �տ��� 3�ڸ� ���Ͽ� �ҹ��ڷ� �̸����� ����Ͻÿ�.
	-- substr(str, position, length) : str ���ڸ� positin ���� length���� ��ŭ ǥ��
	-- lower(str)  �ҹ��� ��ȯ
	-- length(str)  str�� ����
**/
SELECT LOWER(SUBSTR(first_name,1,3)) �ҹ���
FROM employees
WHERE length(first_name) >=6;


