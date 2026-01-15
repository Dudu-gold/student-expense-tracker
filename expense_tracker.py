import sqlite3
from datetime import datetime


class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.datetime = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

class Expense_tracker:
    def __init__(self,  db_path="data/expense.db"):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)
        
    
    def add_expenses(self, amount, category, description):
        conn = self.connect()
        cursor = conn.cursor()
        
        ALLOWED_CATEGORIES = ["Food", "Transport", "Drink", "Data", "Others"]
        
        category = category.strip().title()
        if category not in ALLOWED_CATEGORIES:
            print(f"Invalid category. Allowed categories are: {', '.join(ALLOWED_CATEGORIES)}")
            return

        cursor.execute('''
            INSERT INTO expenses (amount, category, description,datetime)
            VALUES (?,?,?, datetime('now'))
         ''', (amount, category, description))

        conn.commit()
        conn.close()
        print("Expense added successfully.")

        

    


    def view_expenses(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT id, amount, category, description, datetime FROM expenses")
        rows = cursor.fetchall()

        if not rows:
            print("No expenses recorded.")
            return
        
        for row in rows:
            print(f"{row[0]}. {row[2]} - #{row[1]} ({row[3]}) on {row[4]}")

        conn.close()

    def total_expense(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT SUM(amount) FROM expenses")
        total = cursor.fetchone()[0]

        print(f"Total Expenses: #{total if total else 0}")

        conn.close()
        
    
       

def main():
    tracker = Expense_tracker()

    while True:
        print("\n1. Add Expense")
        print("2. View Expense")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.add_expenses(amount, category, description)

        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.total_expense()
        elif choice == "4":
            print("Goodbye!")

        else: 
            print("Invalid choice")

if __name__ == "__main__":         
    main()




        



