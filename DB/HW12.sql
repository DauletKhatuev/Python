/*Вывести id департамента , в котором работает сотрудник, в зависимости от Id сотрудника*/
DELIMITER $$
CREATE FUNCTION GetDepId(emp_id INT)
RETURNS INT
READS SQL DATA
BEGIN
	DECLARE dept_id INT;
	SELECT department_id into dept_id FROM  210225_Khatuev.employees WHERE id = emp_id;
    return dept_id;
END $$
DELIMITER ;

/*Создайте хранимую процедуру get_employee_age, которая принимает id сотрудника 
(IN-параметр) и возвращает его возраст через OUT-параметр.*/
DELIMITER //

CREATE PROCEDURE get_employee_age_proc(
    IN emp_id INT,
    OUT emp_age INT
)
BEGIN
    SELECT age INTO emp_age
    FROM employees
    WHERE id = emp_id;
END //

DELIMITER ;
CALL get_employee_age(123, @age);
SELECT @age AS employee_age;

/*Создайте хранимую процедуру increase_salary, которая принимает зарплату сотрудника (INOUT-параметр) и уменьшает ее на 10%.Создайте хранимую процедуру increase_salary, 
которая принимает зарплату сотрудника (INOUT-параметр) и уменьшает ее на 10%.*/

DELIMITER $$

CREATE PROCEDURE increase_salary(INOUT emp_salary DECIMAL(10,2)) 
BEGIN
    SET emp_salary = emp_salary * 0.9;
END $$

DELIMITER ;