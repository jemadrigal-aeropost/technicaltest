from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config.config import config 
from impl.employee import employee
from impl.product import product

app = Flask(__name__)

db_connection = MySQL(app)

@app.route('/')
def index():
    return "<h1>Technical test</h1>"

def not_found_page(err):
    return "<h1>Invalid URL</h1>",404    

@app.route('/employee',methods=['GET'])
def getAllEmployees():
    try:
        return employee(db_connection).getAllEmployees()
    except Exception as ex:
        return jsonify({'employee_list':[], 'status':-1, 'error':'Main getAllEmployees Error getting the employees'})

@app.route('/employees/<max_salary>',methods=['GET'])
def getAllEmployeesSalary(max_salary):
    try:
        return employee(db_connection).getAllEmployeesSalary(max_salary)
    except Exception as ex:
        return jsonify({'employee_list':[], 'status':-1, 'error':'Main getAllEmployeesSalary Error getting the employees'})

@app.route('/employee/<id>',methods=['GET'])
def getAllEmployeeById(id):
    try:
        return employee(db_connection).getEmployeeById(id)
    except Exception as ex:
        return jsonify({'employee':None, 'status':-1, 'error':'Main getEmployeeById Error getting the employees'})

@app.route('/create/',methods=['POST'])
def createEmployee():
    try:
        print(request.json)
        return employee(db_connection).createEmployee(request.json)
    except Exception as ex:
        print(ex)
        return jsonify({'status':-1, 'error':'Main createEmployee Error saving employee'})

@app.route('/productSearch/<product_name>',methods=['GET'])
def productSearch(product_name):
    try:
        return product(db_connection).productSearch(product_name)
    except Exception as ex:
        return jsonify({'product_list':[], 'status':-1, 'error':'Main productSearch Error getting the products'})

@app.route('/cartTotal/',methods=['POST'])
def cartTotal():
    try:
        return product(db_connection).cartTotal(request.json)
    except Exception as ex:
        print(ex)
        return jsonify({'product_list':[], 'total':0, 'status':-1, 'error':'Main cartTotal Error calculating cart totals'})

@app.route('/discountCalculation/',methods=['POST'])
def discountCalculation():
    try:
        return product(db_connection).discountCalculation(request.json)
    except Exception as ex:
        print(ex)
        return jsonify({'product_list':[], 'total':0, 'status':-1, 'error':'Main discountCalculation Error calculating cart discounts'})

@app.route('/topSellingProducts/',methods=['GET'])
def topSellingProducts():
    try:
        return product(db_connection).topSellingProducts()
    except Exception as ex:
        print(ex)
        return jsonify({'product_list':[], 'status':-1, 'error':'Main topSellingProducts Error calculating top selling products'})


if __name__ == '__main__':
    app.config.from_object(config['configuration'])
    app.register_error_handler(404, not_found_page)
    app.run()