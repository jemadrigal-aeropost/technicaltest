-- 1.Insert a new product with the following details: Product Name: "Laptop", Price: 1000.00,Stock Quantity: 50.
insert into test.products(product_name,price,stock_quantity)
values('Laptop', 1000.00, 50);

-- 2.Update the stock quantity of the product with product_id = 3 to 75
update test.products
set stock_quantity = 75
where product_id = 3;

-- 3.Delete the order with order_id = 10 and its associated order items.
delete
from test.orderitems
where order_id = 10;

delete
from test.orders
where order_id = 10;

-- 4.Retrieve the customer's first and last names who placed the order with order_id = 5.
select c.first_name, c.last_name
from test.customers c join test.orders o on c.customer_id = o.customer_id
where o.order_id = 5;

-- 5.Calculate the total revenue generated by each product (sum of subtotals from orderitems).
select sum(o.subtotal), p.product_id, p.product_name
from test.products p join test.orderitems o on p.product_id = o.product_id
group by p.product_id, p.product_name
order by sum(o.subtotal) desc

