import json
import sqlite3

with open("data/expense.json", "r") as file:
    expenses = json.load(file)

conn = sqlite3.connect("data/expense.db")
cursor = conn.cursor()

for expense in expenses:
    cursor.execute('''
        INSERT INTO expenses (amount, category, description, datetime)
        VALUES (?, ?, ?, ?)''', (
            expense["amount"],
            expense["category"],
            expense["description"],
            expense["datetime"]
        ))
    
conn.commit()
conn.close()

print("json data successfully migrated to Sqlite.")