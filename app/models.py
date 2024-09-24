from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, configure_mappers
from datetime import datetime

DATABASE_URL = "sqlite:///money_manager.db"

# Set up database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define models
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

    transactions = relationship('Transaction', back_populates='user', overlaps="categories", cascade="all, delete-orphan")
    budgets = relationship('Budget', back_populates='user', cascade="all, delete-orphan")
    categories = relationship('Category', secondary='transactions', overlaps="transactions")

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)

    category = relationship('Category', back_populates='transactions', overlaps="categories")
    user = relationship('User', back_populates='transactions', overlaps="categories")

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    transactions = relationship('Transaction', back_populates='category', overlaps="categories")

class Budget(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    amount = Column(Float, nullable=False)

    user = relationship('User', back_populates='budgets')
    category = relationship('Category')


configure_mappers()


# Function to create database and tables
def create_db():
    Base.metadata.create_all(bind=engine)