
# Student Expense Tracker

This is a Python application to track student expenses.

## Database

- Uses **SQLite** to store expenses.
- The database file (`expense.db`) is **not included** in the repo.
- To create the database, table and migrate from .json file which i was using before. run:

```bash
python create_table.py
python migration.py

---

## Features

- Add expenses with:
  - **Amount** (numeric)
  - **Category** (Food, Transport, Drink, Data, Others)
  - **Description** (optional note)
- View all recorded expenses in a list
- Calculate the total expenses
- Saves data in a JSON file (`expense.json`) automatically
- Clean and simple command-line interface

---

## Getting Started

### Prerequisites

- Python 3.x installed on your machine

### How to Run

1. Clone the repository or download the files:

```bash
git clone https://github.com/Dudu-gold/student-expense-tracker.git
````

2. Open the project folder:

```bash
cd student-expense-tracker
```

3. Run the program:

```bash
python expense_tracker.py
```

4. Follow the on-screen menu:

* `1` → Add Expense
* `2` → View Expenses
* `3` → Total Expense
* `4` → Exit

---

## Folder Structure

```
student-expense-tracker/
├── data/                     
│   ├── expense.db            
│   ├── queries.sql           
│   └── old_expenses.json     
│
├── expense_tracker.py        
├── create_table.py           
├── migration.py              
├── README.md                 
└── .gitignore                
---

## Usage Example

```
1. Add Expense
2. View Expense
3. Total Expense
4. Exit
Choose an option: 1
Enter amount: 500
Enter category: Food
Enter description: Lunch
Expense added successfully.
```

---
## Author

**Duduyemi Olalekan omoniyi** – [GitHub Profile](https://github.com/Dudu-gold)

```