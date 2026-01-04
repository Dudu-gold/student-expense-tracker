import json
from datetime import datetime

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.datetime = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description" : self.description,
            "datetime" : self.datetime
        }

class Expense_tracker:
    def __init__(self,  filename="expense.json"):
        self.filename = filename
        self.expenses = self.load_expenses()
    
    def load_expenses(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def save_expenses(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)
    
    def add_expenses(self, amount, category, description):
        try:
            amount = float(amount)
            category = category.title()

            if category not in ["Food", "Transport", "Drink", "Data", "Others"]:
                print("Invalid category. Please choose from Food, Transport, Drink, Data, Others.")
                return
            
            expense = Expense(amount, category, description)
            self.expenses.append(expense.to_dict())
            self.save_expenses()
            print("Expense added successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")


    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        for i, expense in enumerate(self.expenses, start=1):
            print(
                f"{i}. {expense['category']} - ₦{expense['amount']}"
                f"({expense['description']}) on {expense.get('datetime', 'Unknown date')}"
            )

    def total_expense(self):
        
    
        total = sum(expense.get("amount", 0) for expense in self.expenses)

        print(f"Total Expenses : ₦{total}")


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




        



