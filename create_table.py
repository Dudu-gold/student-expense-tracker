import sqlite3

conn = sqlite3.connect('data/expense.db')
cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS 
               expenses(
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      amount REAL, 
      category TEXT,
      description TEXT,
      datetime TEXT)''')  

conn.commit()
conn.close()

print("Database and table created successfully.")
            