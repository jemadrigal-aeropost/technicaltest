from flask import Flask, jsonify
from flask_mysqldb import MySQL

class employee:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def getAllEmployees(self):
        try:
            con = self.db_connection.connection.cursor()
            con.execute("SELECT * FROM employees")
            data = con.fetchall()
            employee_list = []
            for emp in data:
                employee_list.append( {'employee_id':emp[0], 'first_name':emp[1], 'last_name':emp[2], 'email':emp[3], 'phone':emp[4], 'salary':emp[5]} )

            return jsonify({'employee_list':employee_list, 'status':1, 'error':None})
        except Exception as ex:
            print(ex)
            return jsonify({'employee_list':[], 'status':-1, 'error':'EmployeeImpl getAllEmployees Error getting the employees'})

    def getAllEmployeesSalary(self,max_salary):
        try:
            con = self.db_connection.connection.cursor()
            con.execute("SELECT * FROM employees where salary > {0}".format(max_salary))
            data = con.fetchall()
            employee_list = []
            for emp in data:
                employee_list.append( {'employee_id':emp[0], 'first_name':emp[1], 'last_name':emp[2], 'email':emp[3], 'phone':emp[4], 'salary':emp[5]} )

            return jsonify({'employee_list':employee_list, 'status':1, 'error':None})
        except Exception as ex:
            print(ex)
            return jsonify({'employee_list':[], 'status':-1, 'error':'EmployeeImpl getAllEmployees Error getting the employees'})

    def getEmployeeById(self, id):
        try:
            con = self.db_connection.connection.cursor()
            con.execute("SELECT * FROM employees where employee_id = {0}".format(id))
            data = con.fetchone()
            employee = {'employee_id':data[0], 'first_name':data[1], 'last_name':data[2], 'email':data[3], 'phone':data[4], 'salary':data[5]} if data != None else None
           
            return jsonify({'employee':employee, 'status':1, 'error': 'employee {0} does not exist'.format(id) if employee == None else  None})
        except Exception as ex:
            print(ex)
            return jsonify({'employee':None, 'status':-1, 'error':'EmployeeImpl getEmployeeById Error getting the employees'})
    
    def createEmployee(self, employee):
        try:
            con = self.db_connection.connection.cursor()
            con.execute("insert into employees(first_name,last_name,email,phone,salary) values('{0}','{1}','{2}','{3}',{4})".format(employee['first_name'],employee['last_name'],employee['email'], employee['phone'],employee['salary']))
            self.db_connection.connection.commit()
           
            return jsonify({'status':1, 'error':None})
        except Exception as ex:
            print(ex)
            return jsonify({'status':-1, 'error':'EmployeeImpl createEmployee Error saving employee'})