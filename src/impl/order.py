from flask import Flask, jsonify
from flask_mysqldb import MySQL
import datetime


class order:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def getNewOrderCode(self):
            try:
                con = self.db_connection.connection.cursor()
                con.execute("SELECT AUTO_INCREMENT FROM information_schema.tables WHERE table_name = 'orders' AND table_schema = 'test'")
                data = con.fetchone()
            
                return data[0]
            except Exception as ex:
                print(ex)
                return jsonify({'customer':None, 'status':-1, 'error':'CustomerImpl getCustomerById Error getting the customer'})

    def createOrder(self, data):
        try:
            order_id = self.getNewOrderCode()
            order_date = datetime.datetime.now()
            con = self.db_connection.connection.cursor()
            print(data['items'])
            con.execute("insert into orders(customer_id,order_date) values({0},'{1}')".format(data['customer_id'],order_date))
            for item in data['items']:
                print(item)
                con.execute("insert into orderitems(order_id,product_id, quantity, subtotal) values({0},{1},{2},{3})".format(order_id,item['product_id'],item['quantity'],item['subtotal']))

            self.db_connection.connection.commit()

           
            return jsonify({'status':1, 'error':None})
        except Exception as ex:
            print(ex)
            return jsonify({'status':-1, 'error':'OrderImpl createOrder Error saving order'})
