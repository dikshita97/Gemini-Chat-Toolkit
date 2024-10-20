# Import Libraries
import sqlite3
import random
from datetime import datetime, timedelta

## Connect to SQlite
connection = sqlite3.connect("employees.db")

# Create a cursor object to insert record,create table
cursor = connection.cursor()

## create the table
table_info="""
CREATE TABLE EMPLOYEES (ID INT PRIMARY KEY, NAME VARCHAR(100), DEPARTMENT VARCHAR(100), SALARY INT,JOINING_DATE DATE);
"""
cursor.execute(table_info)

# Function to generate a random date
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Function to generate a random name
def random_name():
    first_names = ['John', 'Jane', 'Alex', 'Emily', 'Chris', 'Katie', 'Michael', 'Sarah', 'David', 'Laura']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Departments
departments = ['Engineering', 'Human Resources', 'Marketing', 'Finance', 'Sales', 'Support']

# Insert 100 records
for i in range(1, 101):
    name = random_name()
    department = random.choice(departments)
    salary = random.randint(30000, 100000)
    join_date = random_date(datetime(2015, 1, 1), datetime(2023, 1, 1)).strftime('%Y-%m-%d')
    cursor.execute(f'''INSERT INTO EMPLOYEES (ID, NAME, DEPARTMENT, SALARY, JOINING_DATE) VALUES ({i}, '{name}', '{department}', {salary}, '{join_date}')''')

## Dispaly ALl the records
print("The inserted records are")
data = cursor.execute('''Select * from EMPLOYEES''')
for row in data:
    print(row)

    
# Commit the transaction
connection.commit()

# Close the connection
connection.close()