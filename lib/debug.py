"""
Debug utilities for the Library Management System
This module provides functions to help with debugging and testing the application.
"""

from models.author import Author
from models.book import Book
from models import create_tables, get_session
from faker import Faker
import random

fake = Faker()

def create_sample_data():
    """Create sample data for testing purposes"""
    print("🎭 Creating sample data...")
    
    # Create sample authors
    authors = []
    for i in range(5):
        try:
            author = Author.create(
                name=fake.name(),
                email=fake.email()
            )
            authors.append(author)
            print(f"✅ Created author: {author.name}")
        except Exception as e:
            print(f"❌ Error creating author: {e}")
    
    # Create sample books
    genres = ["Fiction", "Non-Fiction", "Science Fiction", "Mystery", "Romance", "Biography", "History", "Poetry"]
    
    for i in range(15):
        try:
            author = random.choice(authors)
            book = Book.create(
                title=fake.catch_phrase(),
                isbn=fake.isbn13(),
                publication_year=random.randint(1950, 2024),
                genre=random.choice(genres),
                author_id=author.id
            )
            print(f"✅ Created book: {book.title} by {author.name}")
        except Exception as e:
            print(f"❌ Error creating book: {e}")
    
    print("🎉 Sample data creation completed!")

def clear_all_data():
    """Clear all data from the database"""
    print("🗑️  Clearing all data...")
    
    session = get_session()
    try:
        # Delete all books first (due to foreign key constraints)
        session.query(Book).delete()
        session.query(Author).delete()
        session.commit()
        print("✅ All data cleared successfully!")
    except Exception as e:
        session.rollback()
        print(f"❌ Error clearing data: {e}")
    finally:
        session.close()

def show_database_info():
    """Show information about the current database state"""
    print("📊 Database Information")
    print("=" * 30)
    
    authors = Author.get_all()
    books = Book.get_all()
    
    print(f"Authors: {len(authors)}")
    print(f"Books: {len(books)}")
    
    if authors:
        print("\nAuthors:")
        for author in authors:
            # Get book count directly from database to avoid session issues
            session = get_session()
            try:
                book_count = session.query(Book).filter(Book.author_id == author.id).count()
                print(f"  - {author.name} ({author.email}) - {book_count} books")
            finally:
                session.close()
    
    if books:
        print("\nBooks:")
        for book in books:
            # Get author name directly from database to avoid session issues
            session = get_session()
            try:
                author = session.query(Author).filter(Author.id == book.author_id).first()
                author_name = author.name if author else "Unknown Author"
                print(f"  - {book.title} by {author_name} ({book.genre})")
            finally:
                session.close()

def reset_database():
    """Reset the database by clearing all data and recreating tables"""
    print("🔄 Resetting database...")
    
    try:
        clear_all_data()
        create_tables()
        print("✅ Database reset successfully!")
    except Exception as e:
        print(f"❌ Error resetting database: {e}")

def main():
    """Debug menu for testing and development"""
    while True:
        print("\n" + "=" * 40)
        print("🐛 DEBUG MENU")
        print("=" * 40)
        print("0. Exit")
        print("1. Create Sample Data")
        print("2. Clear All Data")
        print("3. Show Database Info")
        print("4. Reset Database")
        
        choice = input("\n> ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            create_sample_data()
        elif choice == "2":
            confirm = input("Are you sure you want to clear all data? (yes/no): ")
            if confirm.lower() == 'yes':
                clear_all_data()
            else:
                print("❌ Operation cancelled.")
        elif choice == "3":
            show_database_info()
        elif choice == "4":
            confirm = input("Are you sure you want to reset the database? (yes/no): ")
            if confirm.lower() == 'yes':
                reset_database()
            else:
                print("❌ Operation cancelled.")
        else:
            print("❌ Invalid choice. Please select a number from 0-4.")

if __name__ == "__main__":
    main()
