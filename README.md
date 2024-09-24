# Money Manager Application

The **Money Manager Application** is a command-line interface (CLI) tool designed to help users manage their personal finances. It allows users to create accounts, add transactions, set budgets for different spending categories, and keep track of their financial balance. Users can also generate reports, export their transaction history or current balance to CSV files, and delete their accounts if needed.

## Features

- **Create User Account**: Users can create an account by providing their name and salary.
- **Add Transactions**: Record various financial transactions (e.g., Groceries, Salary, Entertainment).
- **Set Budgets**: Set budget limits for specific categories to manage spending.
- **Check Balance**: Calculate the current balance by subtracting total expenses from the salary.
- **Generate Reports**: View transaction reports for each user.
- **Export Data**: Export transaction history or balance to CSV files.
- **Delete User Account**: Delete a user's account and all associated data.
- **Exit the Application**: Safely exit the CLI tool.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features-in-detail)
  - [1. Create User Account](#1-create-user-account)
  - [2. Add Transaction](#2-add-transaction)
  - [3. Generate Report](#3-generate-report)
  - [4. Set Budget](#4-set-budget)
  - [5. Export Transactions to CSV](#5-export-transactions-to-csv)
  - [6. Export Balance to CSV](#6-export-balance-to-csv)
  - [7. Check Balance](#7-check-balance)
  - [8. Delete User Account](#8-delete-user-account)
  - [9. Exit](#9-exit)

## Installation

### Prerequisites
Before running the application, ensure you have the following installed:
- **Python 3.x**
- **SQLite** (built-in with SQLAlchemy)
- **SQLAlchemy** (Python ORM for database handling)

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Mikemunene16/money_manager-1.git
    ```

2. Install the dependencies:
    ```bash
    pip install sqlalchemy alembic
    ```

### Database Setup
The database is managed using SQLite. To initialize the database, run the following command:
```bash
python -c "from app.models import create_db; create_db()"
```
This will create the necessary tables (`users`, `transactions`, `budgets`, and `categories`) in a SQLite database named `money_manager.db`.

## Usage

To start the application, run the following command:
```bash
./app/cli.py
```

Once the app is running, you will be prompted with the main menu of options:

```
Options:
1. Create User
2. Add Transaction
3. Generate Report
4. Set Budget
5. Export Transactions to CSV
6. Export Balance to CSV
7. Check Balance
8. Delete Account
9. Exit
```

Choose an option by entering the corresponding number (1-9) and following the prompts.

## Features in Detail

### 1. Create User Account
A user can create a new account by entering their name and salary. The system generates a unique `User ID`, which the user should save for future actions like adding transactions or checking their balance.

#### Example:
```
Enter your name: John Snow
Enter your salary: 5000
Hello John Doe! Account created successfully!! Your User ID is 1. Please save it for future use.
```

### 2. Add Transaction
Users can add financial transactions to their account. When adding a transaction, the user provides the amount spent, the category (e.g., Groceries, Salary, Entertainment), and their `User ID`.

#### Example:
```
Enter amount: 150
Enter category (e.g., Groceries, Salary, Entertainment): Groceries
Enter your User ID: 1
Transaction added successfully!
```

### 3. Generate Report
The user can generate a summary report of all their transactions. This feature takes the `User ID` as input and displays a list of all transactions associated with that user.

#### Example:
```
Enter your User ID: 1
Transaction Report for User ID 1:
- Groceries: 150 on 2024-09-22
- Salary: 5000 on 2024-09-20
```

### 4. Set Budget
Users can set a budget for specific categories (e.g., Groceries, Entertainment) by providing the category name, budget amount, and `User ID`. This helps them track spending within limits.

#### Example:
```
Enter category (e.g., Groceries, Entertainment): Groceries
Enter budget amount: 500
Enter your User ID: 1
Budget set successfully!
```

### 5. Export Transactions to CSV
The user can export all of their transactions to a CSV file for easy tracking. The file will be named based on the user’s `User ID` (e.g., `transactions_1.csv`).

#### Example:
```
Enter your User ID: 1
Transactions exported to transactions_1.csv
```

### 6. Export Balance to CSV
The user can export their current balance to a CSV file. This file includes the user’s name, `User ID`, and balance.

#### Example:
```
Enter your User ID: 1
Balance exported to balance_1.csv
```

### 7. Check Balance
The user can check their current balance, which is calculated by subtracting all recorded expenses from their salary. If the balance is low (below 100), a warning will be displayed.

#### Example:
```
Enter your User ID: 1
Your current balance is: 4850
```

### 8. Delete User Account
This feature allows users to delete their account, which will also delete all their associated transactions and budgets. This is a permanent action and cannot be undone.

#### Example:
```
Enter your User ID to delete: 1
User John Snow deleted successfully.
```

### 9. Exit
This option allows the user to safely exit the application.
