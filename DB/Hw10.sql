use northwind;
/*Для каждого product_id выведите inventory_id 
а также предыдущий и последующей inventory_id по убыванию quantity*/
SELECT 
    product_id,
    inventory_id,
    quantity,
    LAG(inventory_id) OVER (PARTITION BY product_id ORDER BY quantity DESC) AS previous_inventory_id,
    LEAD(inventory_id) OVER (PARTITION BY product_id ORDER BY quantity DESC) AS next_inventory_id
FROM 
    order_details
ORDER BY 
    product_id, 
    quantity DESC;

/* Выведите максимальный и минимальный unit_price для каждого order_id с помощью 
функции FIRST VALUE  Вывести order_id и полученные значения*/
SELECT DISTINCT
    order_id,
    FIRST_VALUE(unit_price) OVER (
        PARTITION BY order_id 
        ORDER BY unit_price DESC
    ) AS max_unit_price,
    FIRST_VALUE(unit_price) OVER (
        PARTITION BY order_id 
        ORDER BY unit_price ASC
    ) AS min_unit_price
FROM order_details
ORDER BY order_id;
/* Выведите order_id и столбец с разнице между  unit_price для каждой заказа и 
минимальным unit_price в рамках одного заказа Задачу решить двумя способами - с 
помощью First VAlue и MIN Выведите order_id и столбец с разнице между  unit_price 
для каждой заказа и минимальным unit_price в рамках одного заказа 
Задачу решить двумя способами - с помощью First VAlue и MIN*/
#1 Способ
SELECT 
    order_id,
    unit_price,
    unit_price - FIRST_VALUE(unit_price) OVER (
        PARTITION BY order_id 
        ORDER BY unit_price ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS diff_from_min_price
FROM order_details
ORDER BY order_id, unit_price;
#2 способ
SELECT 
    order_id,
    unit_price,
    unit_price - MIN(unit_price) OVER (
        PARTITION BY order_id
    ) AS diff_from_min_price
FROM order_details
ORDER BY order_id, unit_price;
/*Присвойте ранг каждой строке используя RANK по убыванию quantity*/
SELECT 
    *,
    RANK() OVER (ORDER BY quantity DESC) AS quantity_rank
FROM 
    order_details
ORDER BY 
    quantity DESC;
    
/*Из предыдущего запроса выберите только строки с рангом до 10 включительно*/
SELECT *
FROM (
    SELECT 
        *,
        RANK() OVER (ORDER BY quantity DESC) AS quantity_rank
    FROM 
        order_details
) AS ranked_data
WHERE 
    quantity_rank <= 10
ORDER BY 
    quantity_rank;
