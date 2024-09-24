from models import Transaction
from models import SessionLocal

def generate_report(user_id):
    db = SessionLocal()
    transactions = db.query(Transaction).filter(Transaction.user_id == user_id).all()

    if transactions:
        print("ID   Amount   Category   Date")
        for txn in transactions:
            print(f"{txn.id}    {txn.amount}    {txn.category.name}    {txn.timestamp}")
    else:
        print("No transactions found.")
    db.close()
