import pandas as pd
import sqlite3
import os

# Ensure required libraries are installed
try:
    import openpyxl
    import xlrd
    import matplotlib.pyplot as plt
except ImportError:
    os.system('pip install openpyxl xlrd matplotlib')
    import openpyxl
    import xlrd
    import matplotlib.pyplot as plt

# Create CSV dataset
csv_content ="""
id,name,age
1,John Doe,28
2,Jane Smith,34
3,Emily Davis,22
"""
with open('data.csv', 'w') as file:
    file.write(csv_content)

# Import CSV data
try:
    df_csv = pd.read_csv('data.csv')
    print("CSV Data:")
    print(df_csv)
except Exception as e:
    print(f"Error reading CSV file: {e}")

# Create Excel dataset
excel_data ={
    'id': [1, 2, 3],
    'name': ['John Doe', 'Jane Smith', 'Emily Davis'],
    'age': [28, 34, 22]
}
df_excel_create = pd.DataFrame(excel_data)
df_excel_create.to_excel('data.xlsx', sheet_name='Sheet1', index=False)

# Import Excel data
try:
    df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')
    print("\nExcel Data:")
    print(df_excel)
except Exception as e:
    print(f"Error reading Excel file: {e}")

# Create JSON dataset
json_content = [
    {"id": 1, "name": "John Doe", "age": 28},
    {"id": 2, "name": "Jane Smith", "age": 34},
    {"id": 3, "name": "Emily Davis", "age": 22}
]
with open('data.json', 'w') as file:
    pd.DataFrame(json_content).to_json(file, orient='records')

# Import JSON data
try:
    df_json = pd.read_json('data.json')
    print("\nJSON Data:")
    print(df_json)
except Exception as e:
    print(f"Error reading JSON file: {e}")

# Create SQL database and table
try:
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS table_name (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    ''')
    cursor.execute('INSERT INTO table_name (id, name, age) VALUES (1, "John Doe", 28)')
    cursor.execute('INSERT INTO table_name (id, name, age) VALUES (2, "Jane Smith", 34)')
    cursor.execute('INSERT INTO table_name (id, name, age) VALUES (3, "Emily Davis", 22)')
    conn.commit()

    # Import SQL data
    df_sql = pd.read_sql_query('SELECT * FROM table_name', conn)
    print("\nSQL Data:")
    print(df_sql)
except Exception as e:
    print(f"Error with SQL database: {e}")
finally:
    conn.close()



































