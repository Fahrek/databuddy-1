CREATE TABLE sales_range 
(salesman_id  NUMBER(5), 
salesman_name VARCHAR2(30), 
sales_amount  NUMBER(10), 
sales_date    DATE)
PARTITION BY RANGE(sales_date) 
(
PARTITION sales_jan2014 VALUES LESS THAN(TO_DATE('02/01/2014','DD/MM/YYYY')),
PARTITION sales_feb2014 VALUES LESS THAN(TO_DATE('03/01/2014','DD/MM/YYYY')),
PARTITION sales_mar2014 VALUES LESS THAN(TO_DATE('04/01/2014','DD/MM/YYYY')),
PARTITION sales_apr2014 VALUES LESS THAN(TO_DATE('05/01/2014','DD/MM/YYYY'))
);


(10, 'Jones', 'Hawaii', 100, '05-JAN-2014')
(21, 'Smith', 'Florida', 150, '15-JAN-2014')
(32, 'Lee', 'Colorado', 130, '21-JAN-2014') 


CREATE TABLE sales_composite 
(salesman_id  NUMBER(5), 
 salesman_name VARCHAR2(30), 
 sales_amount  NUMBER(10), 
 sales_date    DATE)
PARTITION BY RANGE(sales_date) 
SUBPARTITION BY HASH(salesman_id)
SUBPARTITION TEMPLATE(
SUBPARTITION sp1 TABLESPACE data1,
SUBPARTITION sp2 TABLESPACE data2,
SUBPARTITION sp3 TABLESPACE data3,
SUBPARTITION sp4 TABLESPACE data4)
(PARTITION sales_jan2000 VALUES LESS THAN(TO_DATE('02/01/2000','DD/MM/YYYY'))
 PARTITION sales_feb2000 VALUES LESS THAN(TO_DATE('03/01/2000','DD/MM/YYYY'))
 PARTITION sales_mar2000 VALUES LESS THAN(TO_DATE('04/01/2000','DD/MM/YYYY'))
 PARTITION sales_apr2000 VALUES LESS THAN(TO_DATE('05/01/2000','DD/MM/YYYY'))
 PARTITION sales_may2000 VALUES LESS THAN(TO_DATE('06/01/2000','DD/MM/YYYY')));