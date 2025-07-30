/*Создайте функцию для расчета площади круга, если известен его радиус.*/
Delimiter //

CREATE  FUNCTION area_circle(r DECIMAL(10,2))
RETURNS DECIMAL(10,2) DETERMINISTIC
RETURN PI() * POW(r, 2) //
DELIMITER ;\

/*Создайте функцию для расчета гипотенузы треугольника, если известны длины его катетов.*/
DELIMITER //
CREATE function calc_hypotenuse(a DECIMAL(10,2), b DECIMAL(10,2))
returns DECIMAL(10,2)
deterministic
return sqrt(pow(a, 2) + pow(b, 2))
delimiter ;
