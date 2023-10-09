from flask import Flask, jsonify
from flask_mysqldb import MySQL

class customer:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def getCustomerById(self, id):
            try:
                con = self.db_connection.connection.cursor()
                con.execute("SELECT * FROM customers where customer_id = {0}".format(id))
                data = con.fetchone()
                customer = {'customer_id':data[0], 'first_name':data[1], 'last_name':data[2], 'email':data[3], 'phone':data[4]} if data != None else None
            
                return jsonify({'customer':customer, 'status':1, 'error': 'Customer {0} does not exist'.format(id) if customer == None else  None})
            except Exception as ex:
                print(ex)
                return jsonify({'customer':None, 'status':-1, 'error':'CustomerImpl getCustomerById Error getting the customer'})