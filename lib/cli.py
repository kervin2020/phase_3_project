#!/usr/bin/env python3
"""
Library Management System CLI
A command-line interface for managing authors and books in a library database.
"""

from helpers import (
    exit_program,
    initialize_database,
    create_author,
    create_book,
    display_authors,
    display_books,
    find_author_by_id,
    find_author_by_name,
    find_book_by_id,
    find_book_by_title,
    find_books_by_author,
    find_books_by_genre,
    delete_author,
    delete_book,
    show_statistics
)
from models.author import Author
from models.book import Book

def main():
    """Main CLI application loop"""
    print("🏛️  Welcome to the Library Management System! 📚")
    print("=" * 50)
    
    # Initialize database
    if not initialize_database():
        print("❌ Failed to initialize database. Exiting...")
        return
    
    while True:
        main_menu()
        choice = input("\n> ").strip()
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            author_menu()
        elif choice == "2":
            book_menu()
        elif choice == "3":
            search_menu()
        elif choice == "4":
            statistics_menu()
        else:
            print("❌ Invalid choice. Please select a number from 0-4.")

def main_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("📚 MAIN MENU")
    print("=" * 50)
    print("0. Exit Program")
    print("1. Manage Authors")
    print("2. Manage Books")
    print("3. Search & Find")
    print("4. View Statistics")

def author_menu():
    """Author management submenu"""
    while True:
        print("\n" + "=" * 40)
        print("👤 AUTHOR MANAGEMENT")
        print("=" * 40)
        print("0. Back to Main Menu")
        print("1. View All Authors")
        print("2. Add New Author")
        print("3. Find Author by ID")
        print("4. Find Author by Name")
        print("5. Delete Author")
        
        choice = input("\n> ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            authors = Author.get_all()
            display_authors(authors, "All Authors")
        elif choice == "2":
            create_author()
        elif choice == "3":
            find_author_by_id()
        elif choice == "4":
            find_author_by_name()
        elif choice == "5":
            delete_author()
        else:
            print("❌ Invalid choice. Please select a number from 0-5.")

def book_menu():
    """Book management submenu"""
    while True:
        print("\n" + "=" * 40)
        print("📖 BOOK MANAGEMENT")
        print("=" * 40)
        print("0. Back to Main Menu")
        print("1. View All Books")
        print("2. Add New Book")
        print("3. Find Book by ID")
        print("4. Find Book by Title")
        print("5. Delete Book")
        
        choice = input("\n> ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            books = Book.get_all()
            display_books(books, "All Books")
        elif choice == "2":
            create_book()
        elif choice == "3":
            find_book_by_id()
        elif choice == "4":
            find_book_by_title()
        elif choice == "5":
            delete_book()
        else:
            print("❌ Invalid choice. Please select a number from 0-5.")

def search_menu():
    """Search and find submenu"""
    while True:
        print("\n" + "=" * 40)
        print("🔍 SEARCH & FIND")
        print("=" * 40)
        print("0. Back to Main Menu")
        print("1. Find Books by Author")
        print("2. Find Books by Genre")
        print("3. Find Author by Name")
        print("4. Find Book by Title")
        
        choice = input("\n> ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            find_books_by_author()
        elif choice == "2":
            find_books_by_genre()
        elif choice == "3":
            find_author_by_name()
        elif choice == "4":
            find_book_by_title()
        else:
            print("❌ Invalid choice. Please select a number from 0-4.")

def statistics_menu():
    """Statistics and reports submenu"""
    while True:
        print("\n" + "=" * 40)
        print("📊 STATISTICS & REPORTS")
        print("=" * 40)
        print("0. Back to Main Menu")
        print("1. View Library Statistics")
        print("2. View All Authors")
        print("3. View All Books")
        
        choice = input("\n> ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            show_statistics()
        elif choice == "2":
            authors = Author.get_all()
            display_authors(authors, "All Authors")
        elif choice == "3":
            books = Book.get_all()
            display_books(books, "All Books")
        else:
            print("❌ Invalid choice. Please select a number from 0-3.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please try again or contact support.")
