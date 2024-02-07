import sqlite3

connection = sqlite3.connect("TEST.db")

cursor  = connection.cursor()

table_info = """create table EMPLOYEE (NAME VARCHAR(25), DEPARTMENT VARCHAR(25),SALARY INT)"""

cursor.execute(table_info)

cursor.execute('''Insert Into EMPLOYEE values('DAVIS','DATA SCIENCE',50000)''')
cursor.execute('''Insert Into EMPLOYEE values('RAHUL','DEVELOPMENT',40000)''')
cursor.execute('''Insert Into EMPLOYEE values('SHADDY','DATA SCIENCE',50000)''')


connection.commit()
connection.close()