from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os

# Database setup
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///library.db')
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def create_tables():
    """Create all tables in the database"""
    # Import models to ensure they are registered
    from . import author, book
    Base.metadata.create_all(engine)

def get_session():
    """Get a new database session"""
    return Session()
