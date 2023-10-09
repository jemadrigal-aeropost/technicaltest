from flask import Flask, jsonify
from flask_mysqldb import MySQL
from decimal import Decimal

class product:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def productSearch(self, product_name):
        try:
            con = self.db_connection.connection.cursor()
            con.execute("select product_id, product_name, price, stock_quantity from products where upper(product_name) like upper('{0}')".format(product_name))
            data = con.fetchall()
            product_list = []
            for prod in data:
                product_list.append( {'product_id':prod[0], 'product_name':prod[1], 'price':prod[2], 'stock_quantity':prod[3]} )

            return jsonify({'product_list':product_list, 'status':1, 'error':None})
        except Exception as ex:
            print(ex)
            return jsonify({'product_list':[], 'status':-1, 'error':'ProductImpl productSearch Error getting the products'})

    def cartTotal(self, products_id_list):
        try:
            total = 0
            ids = self.getProductsId(products_id_list)
            con = self.db_connection.connection.cursor()
            con.execute("select product_id, product_name, price from products where product_id in ({0})".format(ids))
            data = con.fetchall()
            product_list = []
            for prod in data:
                quantity = self.searchQuantity(products_id_list, prod[0])
                total_items = (quantity * prod[2])
                total = total + total_items
                product_list.append( {'product_id':prod[0], 'product_name':prod[1], 'price':prod[2] ,'quantity':quantity, 'subtotal':total_items} )

            return jsonify({'product_list':product_list, 'total':total, 'status':1, 'error':None})
        except Exception as ex:
            print(ex)
            return jsonify({'product_list':[], 'total':0, 'status':-1, 'error':'ProductImpl cartTotal Error calculating cart totals'})

    def discountCalculation(self, products_list):
        try:
            total = 0
            ids = self.getProductsId(products_list)
            con = self.db_connection.connection.cursor()
            con.execute("select product_id, product_name, price from products where product_id in ({0})".format(ids))
            data = con.fetchall()
            product_list = []
            for prod in data:
                quantity = self.searchQuantity(products_list, prod[0])
                total_items = (quantity * prod[2])
                discount = total_items * (self.serchDiscount(products_list, prod[0]) / Decimal(str(100)))
                total = total + (total_items - discount)
                product_list.append( {'product_id':prod[0], 'product_name':prod[1], 'price':prod[2] ,'quantity':quantity, 'discount':discount, 'subtotal':total_items,'line_total':total_items - discount} )

            return jsonify({'product_list':product_list, 'total':total, 'status':1, 'error':None})
        except Exception as ex:
            print(ex)
            return jsonify({'product_list':[], 'total':0, 'status':-1, 'error':'ProductImpl discountCalculation Error calculating cart discounts'})

    def topSellingProducts(self):
        try:
            con = self.db_connection.connection.cursor()
            con.execute("select sum(o.quantity) as quantitySold, p.product_id, p.product_name from test.products p join test.orderitems o on p.product_id = o.product_id group by p.product_id, p.product_name order by sum(o.quantity) desc")
            data = con.fetchall()
            print(data)
            product_list = []
            for prod in data:
                product_list.append( {'quantitySold':prod[0], 'product_id':prod[1], 'prod_name':prod[2]} )

            return jsonify({'product_list':product_list, 'status':1, 'error':None})
        except Exception as ex:
            print(ex)
            return jsonify({'product_list':[], 'status':-1, 'error':'ProductImpl topSellingProducts Error calculating top selling products'})


    def getProductsId(self, products_id_list):
            ids = [str(product['product_id']) for product in products_id_list]
            return ", ".join(ids)
    
    def searchQuantity(self, products_id_list, product_id):
        for prod in products_id_list:
            if prod['product_id'] == product_id:
                return prod['quantity']
        return 0
    
    def serchDiscount(self, products_id_list, product_id):
        for prod in products_id_list:
            if prod['product_id'] == product_id:
                return prod['discount']
        return 0

    