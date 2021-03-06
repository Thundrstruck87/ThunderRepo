# This program will connect to a SQL database and ask the user input information into the table.
#
# make sure to have pyodbc and pandas installed
# pip install pyodbc
# pip install pandas
#
# import pandas as pd
import time
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;' # Replace server_name with the name of your SQL server
                      'Database=carparts;'  # Replace carparts with the database you want to use
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('''
                  SELECT * FROM carparts.dbo.modifications
               
                ''')
                                                            # Replace carparts with your database, replace modifications with your table name
conn.commit()

#
#    This code is currently broken and would of replaced lines 16 - 20. This code would have been included to print the
#    COLUMN names along with the data that's in the rows. Please go to https://tinyurl.com/y3dm3h86 for an update
#
#               Keep in mind, the 'import pandas as pd' (line 7) is also commented out until this is fixed
#
# sql_query = pd.read_sql_query('SELECT * FROM carparts.dbo.modifications', conn)
# print(sql_query)
# print(type(sql_query))
#



# Menu starts below

#answer = str(input("Would you like to enter in another? (yes/no): "))
while answer.casefold() == "yes":
  database = "carparts"
  print("Welcome to the program!")
  print()
  print("You are connected to {} database".format(database))
  print()
  print()
  print("The current columns in the table are...")
  print()
  conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=server_name;'
                        'Database=carparts;'
                        'Trusted_Connection=yes;')

  cursor = conn.cursor()
  cursor.execute('SELECT * FROM carparts.dbo.modifications where 1=2')
  headers = [i[0] for i in cursor.description]
  print(headers)
  print()
  print("Categories are: engine, suspension, exhaust, or transmission")
  print()
  category = str(input("Please enter category: "))
  print()
  description = str(input("Please enter the description of the part: "))
  print()
  purchase_date = input("Please enter the purchase date in (YYYY-MM-DD): ")
  print()
  price = int(input("Please enter the price amount: "))
  print()
  vehicle = str(input("What vehicle is this for? (Model): "))
  print()
  print("Thanks!")
  time.sleep(3)
  print("\n" * 5)  # This will the clear screen of any previous code
  print("Adding the category, description, purchase date, price, and vehicle to the table...")
  time.sleep(2)

  cursor.execute('''
                    INSERT INTO carparts.dbo.modifications (category, description, purchase_date, price, vehicle)
                    VALUES
                    ('{}', '{}', '{}', '{}', '{}')
                   '''.format(category, description, purchase_date, price, vehicle))
    conn.commit()
    print()
    print("The data has been entered!")
    print()
    print(answer)
else:
    print("Thanks, have a great day!")
