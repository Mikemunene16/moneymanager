from models import Budget, Category
from models import SessionLocal

def set_budget(user_id, category_name, amount):
    db = SessionLocal()

    # Get or create the category
    category = db.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        db.add(category)
        db.commit()

    # Set the budget for the category
    budget = Budget(amount=amount, category_id=category.id, user_id=user_id)
    db.add(budget)
    db.commit()

    db.close()