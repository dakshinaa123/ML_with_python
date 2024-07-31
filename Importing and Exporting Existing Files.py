import pandas as pd
# Importing data from a CSV file
df = pd.read_csv('data.csv')
print(df)
# Importing data from a Excel file
df = pd.read_excel('data_demo.xlsx', sheet_name='Sheet1')
print(df)
# Importing data from a JSON file
df = pd.read_json('data.json')
print(df)
# Importing data from a SQL database
conn = sqlite3.connect()
df = pd.read_sql_query('select * from table_name', conn)
print(df)


# Exporting data to a CSV file
df.to_csv('output.csv', index='False')

# Exporting data to an Excel Fil3e
df.to_excel('output.xlsx',sheet_name='Sheet1', index=False)

# Exporting data to a JSON file
df.to_json('output.json')

# Exporting data to a SQL database
conn = sqlite3.connect('database.db')
df.to_sql('table_name',conn, if_exists='replace', index=False)