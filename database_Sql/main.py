import psycopg2

connection = psycopg2.connect(database="dvdrental", user="postgres", password="Nokia@123", host="localhost", port=5432)
cursor = connection.cursor()
cursor.execute("SELECT * from customer;")

# Fetch the column names from the cursor description 
#column_names = [desc[0] for desc in cursor.description] 
# Print the column names 
#print(column_names) 

file = open("data.txt","w")
while True:
# Fetch all rows from database
   records = cursor.fetchall()
   for record in records:
      record = str(record)
  #if record[2].startswith("S"):
      file.write(record)
      file.write('\n')

# Close the cursor and the   


