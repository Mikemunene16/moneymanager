#!/usr/bin/env python3

from models import Transaction, Budget, Category, User
from models import SessionLocal
from reports import generate_report
from budget import set_budget
import csv

def main():
    while True:
        print("\nOptions:")
        print("1. Create User")
        print("2. Add Transaction")
        print("3. Generate Report")
        print("4. Set Budget")
        print("5. Export Transactions to CSV")
        print("6. Export Balance to CSV")
        print("7. Check Balance")
        print("8. Delete Account")
        print("9. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            create_user()
        elif choice == '2':
            add_transaction()
        elif choice == '3':
            generate_report_cli()
        elif choice == '4':
            set_budget_cli()
        elif choice == '5':
            export_transactions_to_csv()
        elif choice == '6':
            export_balance_to_csv()
        elif choice == '7':
            check_balance()
        elif choice == '8':
            delete_user()
        elif choice == '9':
            print("Exiting the application.")
            break  # Corrected exit logic
        else:
            print("Invalid choice. Please try again.")

def create_user():
    try:
        name = input("Enter your name: ").strip()
        salary = float(input("Enter your salary: "))
        
        db = SessionLocal()
        user = User(name=name, salary=salary)
        db.add(user)
        db.commit()

        print(f"Hello {name}! Account created successfully!! Your User ID is {user.id}. Please save it for future use.")
    except Exception as e:
        print(f"Error creating user: {e}")
    finally:
        db.close()

def add_transaction():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Groceries, Salary, Entertainment): ").strip()
        user_id = int(input("Enter your User ID: ").strip())

        db = SessionLocal()

        # Check if category exists, otherwise create it
        category_obj = db.query(Category).filter_by(name=category).first()
        if not category_obj:
            category_obj = Category(name=category)
            db.add(category_obj)
            db.commit()

        transaction = Transaction(amount=amount, category_id=category_obj.id, user_id=user_id)
        db.add(transaction)
        db.commit()
        print("Transaction added successfully!")

    except Exception as e:
        print(f"Error adding transaction: {e}")
    finally:
        db.close()

def generate_report_cli():
    try:
        user_id = int(input("Enter your User ID: ").strip())
        generate_report(user_id)
    except Exception as e:
        print(f"Error generating report: {e}")

def set_budget_cli():
    try:
        category = input("Enter category (e.g., Groceries, Entertainment): ").strip()
        amount = float(input("Enter budget amount: ").strip())
        user_id = int(input("Enter your User ID: ").strip())

        set_budget(user_id, category, amount)
        print("Budget set successfully!")

    except Exception as e:
        print(f"Error setting budget: {e}")

def export_transactions_to_csv():
    try:
        user_id = int(input("Enter your User ID: ").strip())
        db = SessionLocal()
        transactions = db.query(Transaction).filter(Transaction.user_id == user_id).all()

        if not transactions:
            print("No transactions found for this user.")
            return

        with open(f'transactions_{user_id}.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Amount', 'Category', 'Date'])
            for txn in transactions:
                writer.writerow([txn.id, txn.amount, txn.category.name, txn.timestamp])

        print(f"Transactions exported to transactions_{user_id}.csv")

    except Exception as e:
        print(f"Error exporting transactions: {e}")
    finally:
        db.close()

def export_balance_to_csv():
    try:
        user_id = int(input("Enter your User ID: ").strip())
        db = SessionLocal()
        user = db.query(User).filter_by(id=user_id).first()

        if user:
            total_spent = sum([t.amount for t in user.transactions])
            balance = user.salary - total_spent
            with open(f'balance_{user_id}.csv', 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['User ID', 'Name', 'Balance'])
                writer.writerow([user.id, user.name, balance])

            print(f"Balance exported to balance_{user_id}.csv")
        else:
            print("User not found.")
    except Exception as e:
        print(f"Error exporting balance: {e}")
    finally:
        db.close()

def check_balance():
    try:
        user_id = int(input("Enter your User ID: ").strip())
        db = SessionLocal()
        user = db.query(User).filter_by(id=user_id).first()
        
        if user:
            total_spent = sum([t.amount for t in user.transactions])
            balance = user.salary - total_spent
            print(f"Your current balance is: {balance}")
            if balance < 100:  # Low balance warning
                print("Warning: Your balance is running low!")
        else:
            print("User not found.")
    except Exception as e:
        print(f"Error checking balance: {e}")
    finally:
        db.close()

def delete_user():
    try:
        user_id = int(input("Enter your User ID to delete: ").strip())
        db = SessionLocal()
        user = db.query(User).filter_by(id=user_id).first()

        if user:
            db.delete(user)
            db.commit()
            print(f"User {user.name} deleted successfully.")
        else:
            print("User not found.")
    except Exception as e:
        print(f"Error deleting user: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()