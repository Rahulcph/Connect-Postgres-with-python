import psycopg2
from faker import Faker
import random
#from login import password

# Initialize Faker for generating fake data
fakes = Faker('en_IN')

# Database connection parameters
db_user = "postgres"
db_password = "Nokia@123"  # Replace with your actual password
db_host = "localhost"  # or your database host
db_port = "5432"       # default PostgreSQL port
db_name = "ems"

def create_table():

    query = '''CREATE TABLE IF NOT EXISTS employee (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255), 
            company VARCHAR(255), 
            salary INTEGER,
            hire_date DATE, 
            city VARCHAR(50)
            );
            '''
    
    conn = psycopg2.connect(
        dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port )
    
    cursor = conn.cursor()
    
    # Execute the creation query
    cursor.execute(query)
    conn.commit()
    print("Table 'employee' created successfully.")


def insert_data():
    """Inserts a single row of fake data into the employee table."""
    # Generate fake data
    name = fakes.name()
    email = fakes.email()
    company = fakes.company()
    salary = random.randint(40000, 100000)
    hire_date = fakes.date()
    city = fakes.city()

    # Use parameterized query to safely insert data
    query = """
        INSERT INTO employee (name, email, company, salary, hire_date, city) 
        VALUES (%s, %s, %s, %s, %s, %s);
    """
    conn = psycopg2.connect(
        dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port )
    
    cursor = conn.cursor()

    cursor.execute(query, (name, email, company, salary, hire_date, city))
    conn.commit()
    print(f'Inserted data: {name}, {email}, {company}, {salary}, {hire_date}, {city}')

# create_table()

# for _ in range(100):
#     insert_data()

def show_data():

    query = """select * from employee;"""
    conn = psycopg2.connect(
        dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port )
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows


# to create the table run this command 
#create_table()
# we are going to insert data now
#insert_data()
#we are going to insert bulk data 
#for i in range(96):
 #   insert_data()
#we are going to display data 

rows = show_data()
for row in rows:
   print(row)
