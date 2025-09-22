from models.author import Author
from models.book import Book
from models import create_tables
import re

def exit_program():
    """Exit the program with a goodbye message"""
    print("\nThank you for using the Library Management System!")
    print("Goodbye! 📚")
    exit()

def initialize_database():
    """Initialize the database and create tables"""
    try:
        create_tables()
        print("✅ Database initialized successfully!")
        return True
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        return False

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_isbn(isbn):
    """Validate ISBN format (basic validation)"""
    # Remove hyphens and spaces
    clean_isbn = re.sub(r'[-\s]', '', isbn)
    # Check if it's 10 or 13 digits
    return len(clean_isbn) in [10, 13] and clean_isbn.isdigit()

def validate_year(year_str):
    """Validate publication year"""
    try:
        year = int(year_str)
        current_year = 2024
        return 1000 <= year <= current_year
    except ValueError:
        return False

def get_user_input(prompt, validator=None, error_msg="Invalid input. Please try again."):
    """Get user input with validation"""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("❌ Input cannot be empty. Please try again.")
                continue
            
            if validator and not validator(user_input):
                print(f"❌ {error_msg}")
                continue
            
            return user_input
        except KeyboardInterrupt:
            print("\n\nOperation cancelled.")
            return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None

def display_authors(authors, title="Authors"):
    """Display a list of authors in a formatted way"""
    if not authors:
        print(f"\n📝 No {title.lower()} found.")
        return
    
    print(f"\n📚 {title}:")
    print("=" * 60)
    for author in authors:
        print(f"ID: {author.id} | {author.display_name}")
        print(f"   Books: {author.book_count}")
        print("-" * 40)

def display_books(books, title="Books"):
    """Display a list of books in a formatted way"""
    if not books:
        print(f"\n📖 No {title.lower()} found.")
        return
    
    print(f"\n📚 {title}:")
    print("=" * 80)
    for book in books:
        print(f"ID: {book.id} | {book.display_title}")
        print(f"   ISBN: {book.isbn} | Year: {book.publication_year} | Genre: {book.genre}")
        print(f"   Age: {book.age} years old {'(Recent)' if book.is_recent else ''}")
        print("-" * 50)

def create_author():
    """Create a new author"""
    print("\n📝 Creating New Author")
    print("=" * 30)
    
    name = get_user_input("Enter author name: ")
    if not name:
        return None
    
    email = get_user_input(
        "Enter author email: ",
        validator=validate_email,
        error_msg="Please enter a valid email address."
    )
    if not email:
        return None
    
    # Check if email already exists
    existing_author = Author.find_by_email(email)
    if existing_author:
        print(f"❌ Author with email '{email}' already exists!")
        return None
    
    try:
        author = Author.create(name=name, email=email)
        print(f"✅ Author '{author.name}' created successfully!")
        return author
    except Exception as e:
        print(f"❌ Error creating author: {e}")
        return None

def create_book():
    """Create a new book"""
    print("\n📖 Creating New Book")
    print("=" * 30)
    
    # First, show available authors
    authors = Author.get_all()
    if not authors:
        print("❌ No authors found. Please create an author first.")
        return None
    
    display_authors(authors, "Available Authors")
    
    # Get author ID
    author_id_input = get_user_input("Enter author ID: ")
    if not author_id_input:
        return None
    
    try:
        author_id = int(author_id_input)
        author = Author.find_by_id(author_id)
        if not author:
            print(f"❌ Author with ID {author_id} not found!")
            return None
    except ValueError:
        print("❌ Please enter a valid author ID number.")
        return None
    
    # Get book details
    title = get_user_input("Enter book title: ")
    if not title:
        return None
    
    isbn = get_user_input(
        "Enter ISBN (10 or 13 digits): ",
        validator=validate_isbn,
        error_msg="Please enter a valid ISBN (10 or 13 digits)."
    )
    if not isbn:
        return None
    
    # Check if ISBN already exists
    existing_book = Book.find_by_isbn(isbn)
    if existing_book:
        print(f"❌ Book with ISBN '{isbn}' already exists!")
        return None
    
    year_input = get_user_input(
        "Enter publication year: ",
        validator=validate_year,
        error_msg="Please enter a valid year (1000-2024)."
    )
    if not year_input:
        return None
    
    publication_year = int(year_input)
    
    genre = get_user_input("Enter genre: ")
    if not genre:
        return None
    
    try:
        book = Book.create(
            title=title,
            isbn=isbn,
            publication_year=publication_year,
            genre=genre,
            author_id=author_id
        )
        print(f"✅ Book '{book.title}' by {author.name} created successfully!")
        return book
    except Exception as e:
        print(f"❌ Error creating book: {e}")
        return None

def find_author_by_id():
    """Find and display an author by ID"""
    author_id_input = get_user_input("Enter author ID: ")
    if not author_id_input:
        return
    
    try:
        author_id = int(author_id_input)
        author = Author.find_by_id(author_id)
        if author:
            display_authors([author], "Author Found")
            if author.books:
                display_books(author.books, f"Books by {author.name}")
        else:
            print(f"❌ Author with ID {author_id} not found!")
    except ValueError:
        print("❌ Please enter a valid author ID number.")

def find_author_by_name():
    """Find and display authors by name"""
    name = get_user_input("Enter author name (partial match): ")
    if not name:
        return
    
    authors = Author.find_by_name(name)
    display_authors(authors, f"Authors matching '{name}'")

def find_book_by_id():
    """Find and display a book by ID"""
    book_id_input = get_user_input("Enter book ID: ")
    if not book_id_input:
        return
    
    try:
        book_id = int(book_id_input)
        book = Book.find_by_id(book_id)
        if book:
            display_books([book], "Book Found")
        else:
            print(f"❌ Book with ID {book_id} not found!")
    except ValueError:
        print("❌ Please enter a valid book ID number.")

def find_book_by_title():
    """Find and display books by title"""
    title = get_user_input("Enter book title (partial match): ")
    if not title:
        return
    
    books = Book.find_by_title(title)
    display_books(books, f"Books matching '{title}'")

def find_books_by_author():
    """Find and display books by author"""
    authors = Author.get_all()
    if not authors:
        print("❌ No authors found.")
        return
    
    display_authors(authors, "Available Authors")
    
    author_id_input = get_user_input("Enter author ID: ")
    if not author_id_input:
        return
    
    try:
        author_id = int(author_id_input)
        author = Author.find_by_id(author_id)
        if not author:
            print(f"❌ Author with ID {author_id} not found!")
            return
        
        books = Book.find_by_author_id(author_id)
        display_books(books, f"Books by {author.name}")
    except ValueError:
        print("❌ Please enter a valid author ID number.")

def find_books_by_genre():
    """Find and display books by genre"""
    genre = get_user_input("Enter genre (partial match): ")
    if not genre:
        return
    
    books = Book.find_by_genre(genre)
    display_books(books, f"Books in genre '{genre}'")

def delete_author():
    """Delete an author and their books"""
    authors = Author.get_all()
    if not authors:
        print("❌ No authors found.")
        return
    
    display_authors(authors, "Available Authors")
    
    author_id_input = get_user_input("Enter author ID to delete: ")
    if not author_id_input:
        return
    
    try:
        author_id = int(author_id_input)
        author = Author.find_by_id(author_id)
        if not author:
            print(f"❌ Author with ID {author_id} not found!")
            return
        
        # Show what will be deleted
        print(f"\n⚠️  This will delete:")
        print(f"   - Author: {author.display_name}")
        print(f"   - {author.book_count} book(s) by this author")
        
        confirm = get_user_input("Are you sure? Type 'yes' to confirm: ")
        if confirm and confirm.lower() == 'yes':
            author.delete()
            print(f"✅ Author '{author.name}' and their books deleted successfully!")
        else:
            print("❌ Deletion cancelled.")
    except ValueError:
        print("❌ Please enter a valid author ID number.")
    except Exception as e:
        print(f"❌ Error deleting author: {e}")

def delete_book():
    """Delete a book"""
    books = Book.get_all()
    if not books:
        print("❌ No books found.")
        return
    
    display_books(books, "Available Books")
    
    book_id_input = get_user_input("Enter book ID to delete: ")
    if not book_id_input:
        return
    
    try:
        book_id = int(book_id_input)
        book = Book.find_by_id(book_id)
        if not book:
            print(f"❌ Book with ID {book_id} not found!")
            return
        
        print(f"\n⚠️  This will delete: {book.display_title}")
        
        confirm = get_user_input("Are you sure? Type 'yes' to confirm: ")
        if confirm and confirm.lower() == 'yes':
            book.delete()
            print(f"✅ Book '{book.title}' deleted successfully!")
        else:
            print("❌ Deletion cancelled.")
    except ValueError:
        print("❌ Please enter a valid book ID number.")
    except Exception as e:
        print(f"❌ Error deleting book: {e}")

def show_statistics():
    """Show library statistics"""
    authors = Author.get_all()
    books = Book.get_all()
    
    print("\n📊 Library Statistics")
    print("=" * 30)
    print(f"Total Authors: {len(authors)}")
    print(f"Total Books: {len(books)}")
    
    if books:
        # Genre statistics
        genres = {}
        for book in books:
            genres[book.genre] = genres.get(book.genre, 0) + 1
        
        print(f"\n📚 Books by Genre:")
        for genre, count in sorted(genres.items()):
            print(f"   {genre}: {count}")
        
        # Recent books
        recent_books = [book for book in books if book.is_recent]
        print(f"\n🆕 Recent Books (last 10 years): {len(recent_books)}")
        
        # Average book age
        if books:
            avg_age = sum(book.age for book in books) / len(books)
            print(f"📅 Average Book Age: {avg_age:.1f} years")
    
    if authors:
        # Author with most books
        author_with_most_books = max(authors, key=lambda a: a.book_count)
        print(f"\n👑 Most Prolific Author: {author_with_most_books.name} ({author_with_most_books.book_count} books)")
