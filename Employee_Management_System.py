#Python program to store Employee information in MYSQL

import mysql.connector

con = mysql.connector.connect(
	host="localhost",user="root",password="Tiger@1998",port='3306',database="emp"

)
def Add_Employee():
	id = input("Enter Employee Id : ")
	if(check_employee(id) == True):
		print("Employee already exists \n Try Again\n ")
		menu()
	else:
		Name = input("Enter Employee Name: ")
		Post = input("Enter Employee Post: ")
		Salary = input("Enter Employee Salary: ")
		data = (id,Name,Post,Salary)

		sql = 'insert into employees values(%s,%s,%s,%s)'
		c=con.cursor()
		c.execute(sql,data)
		con.commit()
		print("Employee Added Successfully ")
		menu()

def Promote_EMployee():
	id = int(input("Enter Employee ID "))
	if(check_employee(id) == False):
		print("Employee does not exists \n Try Again\n")
		menu()
	else:
		amount = int(input("Enter increased salary"))
		sql = 'select salary from employees where id=%s'
		data = (id,)
		c= con.cursor()
		c.execute(sql,data)
		r = c.fetchone()
		t = r[0]+str(amount)
		sql = 'update employees set salary=%s where id=%s'
		d = (t,id)
		c.execute(sql,d)
		con.commit()
		print("Employee Promoted")
		menu()

def Remove_Employee():
	id = input("Enter Employee id: ")
	if(check_employee(id) == False):
		print("Employee does not exists\nTry again\n")
		menu()
	else:
		sql = 'delete from employees where id=%s'
		data =(id,)
		c = con.cursor()
		c.execute(sql,data)
		con.commit()
		print("Employee Removed")
		menu()

def check_employee(employee_id):
	sql = 'select * from employees where id=%s'
	c = con.cursor(buffered=True)
	data = (employee_id,)
	c.execute(sql,data)
	r = c.rowcount
	if r==1:
		return True
	else:
		return False

def Display_Employees():
	sql = 'select * from employees'
	c = con.cursor()
	c.execute(sql)
	r= c.fetchall()
	for i in r:
		print("Employee Id : ", i[0])
		print("Employee Name : ", i[1])
		print("Employee Post : ", i[2])
		print("Employee Salary : ", i[3])
		print("---------------------\
		        -----------------------------\
		        ------------------------------\
		        ---------------------")
	menu()

def menu():
	print("Welcome to Employee Management")
	print("Press")
	print("1 to add employee")
	print("2 to remove employee")
	print("3 to Promote employee")
	print("4 to display employee")
	print("5 to exit")

	ch = int(input("Enter your choice "))
	if ch == 1:
		Add_Employee()
	elif ch == 2:
		Remove_Employee()
	elif ch == 3:
		Promote_EMployee()
	elif ch == 4:
		Display_Employees()
	elif ch == 5:
		exit(0)
	else:
		print("Invalid choice")
		menu()

menu()