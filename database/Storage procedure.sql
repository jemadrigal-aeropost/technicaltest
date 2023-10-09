CREATE PROCEDURE `getTotalRevenueByCustomerId`(in customer_id int, 
										 out totalRevenue DECIMAL(10,2))
BEGIN

	select sum(i.subtotal) into totalRevenue
    from test.customers c join test.orders o on c.customer_id = o.customer_id
	     join test.orderitems i on o.order_id = i.order_id  
    where c.customer_id = customer_id;

END


CREATE PROCEDURE `getTotalRevenueByEmail`(in email VARCHAR(100), 
										 out totalRevenue DECIMAL(10,2))
BEGIN

	select sum(i.subtotal) into totalRevenue
    from test.customers c join test.orders o on c.customer_id = o.customer_id
	     join test.orderitems i on o.order_id = i.order_id  
    where c.email = email;

END