# Library Management System 📚

A comprehensive Command Line Interface (CLI) application for managing a library database with authors and books. This project demonstrates Object-Relational Mapping (ORM) concepts using SQLAlchemy and provides an intuitive user interface for library management operations.

## Features

- **Author Management**: Create, view, search, and delete authors
- **Book Management**: Create, view, search, and delete books
- **Advanced Search**: Find books by author, genre, title, or ISBN
- **Statistics**: View comprehensive library statistics and reports
- **Data Validation**: Input validation for emails, ISBNs, and publication years
- **User-Friendly Interface**: Intuitive menu-driven navigation with clear feedback

## Project Structure

```
.
├── Pipfile                    # Python dependencies and virtual environment configuration
├── Pipfile.lock              # Locked dependency versions
├── README.md                 # This file - project documentation
└── lib/                      # Main application directory
    ├── models/               # Database models and ORM setup
    │   ├── __init__.py       # Database configuration and base setup
    │   ├── author.py         # Author model with ORM methods
    │   └── book.py           # Book model with ORM methods
    ├── cli.py                # Main CLI application interface
    ├── helpers.py            # Helper functions for CLI operations
    └── debug.py              # Debug utilities and sample data generation
```

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pipenv (for dependency management)

### Installation Steps

1. **Clone or download the project**
   ```bash
   cd /path/to/project
   ```

2. **Install dependencies**
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment**
   ```bash
   pipenv shell
   ```

4. **Run the application**
   ```bash
   python lib/cli.py
   ```

## Usage

### Main Menu Options

The application provides a hierarchical menu system:

1. **Manage Authors** - Create, view, search, and delete authors
2. **Manage Books** - Create, view, search, and delete books  
3. **Search & Find** - Advanced search capabilities
4. **View Statistics** - Library statistics and reports

### Key Features

#### Author Management
- **Create Author**: Add new authors with name and email validation
- **View All Authors**: Display all authors with book counts
- **Find by ID/Name**: Search for specific authors
- **Delete Author**: Remove authors and their associated books

#### Book Management
- **Create Book**: Add new books with ISBN and year validation
- **View All Books**: Display all books with author information
- **Find by ID/Title**: Search for specific books
- **Delete Book**: Remove individual books

#### Advanced Search
- **Books by Author**: Find all books by a specific author
- **Books by Genre**: Filter books by genre
- **Partial Matching**: Search with partial text matching

#### Statistics & Reports
- Total authors and books count
- Books by genre breakdown
- Recent books (last 10 years)
- Average book age
- Most prolific author

## Database Models

### Author Model (`lib/models/author.py`)

The Author model represents library authors with the following attributes:

- **id**: Primary key (auto-generated)
- **name**: Author's full name (required)
- **email**: Author's email address (required, unique)
- **created_at**: Timestamp of record creation
- **books**: One-to-many relationship with Book model

**Key Methods:**
- `create(name, email)`: Create a new author
- `get_all()`: Retrieve all authors
- `find_by_id(author_id)`: Find author by ID
- `find_by_name(name)`: Find authors by name (partial match)
- `find_by_email(email)`: Find author by email
- `delete()`: Delete the author and associated books
- `update(name, email)`: Update author information

**Properties:**
- `book_count`: Number of books by this author
- `display_name`: Formatted author name with email

### Book Model (`lib/models/book.py`)

The Book model represents library books with the following attributes:

- **id**: Primary key (auto-generated)
- **title**: Book title (required)
- **isbn**: International Standard Book Number (required, unique)
- **publication_year**: Year of publication (required)
- **genre**: Book genre/category (required)
- **created_at**: Timestamp of record creation
- **author_id**: Foreign key linking to Author model
- **author**: Many-to-one relationship with Author model

**Key Methods:**
- `create(title, isbn, publication_year, genre, author_id)`: Create a new book
- `get_all()`: Retrieve all books
- `find_by_id(book_id)`: Find book by ID
- `find_by_title(title)`: Find books by title (partial match)
- `find_by_author_id(author_id)`: Find books by author
- `find_by_genre(genre)`: Find books by genre
- `find_by_isbn(isbn)`: Find book by ISBN
- `delete()`: Delete the book
- `update(...)`: Update book information

**Properties:**
- `display_title`: Formatted book title with author name
- `is_recent`: Boolean indicating if book is from last 10 years
- `age`: Age of the book in years

## CLI Interface (`lib/cli.py`)

The main CLI application provides a user-friendly interface with:

- **Hierarchical Menus**: Organized navigation through different sections
- **Input Validation**: Comprehensive validation for all user inputs
- **Error Handling**: Graceful error handling with informative messages
- **User Feedback**: Clear success/error messages with emojis for better UX
- **Keyboard Interrupt Handling**: Proper handling of Ctrl+C interruptions

### Menu Structure

```
Main Menu
├── Manage Authors
│   ├── View All Authors
│   ├── Add New Author
│   ├── Find Author by ID
│   ├── Find Author by Name
│   └── Delete Author
├── Manage Books
│   ├── View All Books
│   ├── Add New Book
│   ├── Find Book by ID
│   ├── Find Book by Title
│   └── Delete Book
├── Search & Find
│   ├── Find Books by Author
│   ├── Find Books by Genre
│   ├── Find Author by Name
│   └── Find Book by Title
└── View Statistics
    ├── View Library Statistics
    ├── View All Authors
    └── View All Books
```

## Helper Functions (`lib/helpers.py`)

The helpers module contains utility functions that support the CLI operations:

### Validation Functions
- `validate_email(email)`: Validates email format using regex
- `validate_isbn(isbn)`: Validates ISBN format (10 or 13 digits)
- `validate_year(year_str)`: Validates publication year (1000-2024)

### Display Functions
- `display_authors(authors, title)`: Formatted display of author lists
- `display_books(books, title)`: Formatted display of book lists
- `show_statistics()`: Comprehensive library statistics

### CRUD Operations
- `create_author()`: Interactive author creation with validation
- `create_book()`: Interactive book creation with author selection
- `find_author_by_id()`: Find and display author by ID
- `find_author_by_name()`: Find and display authors by name
- `find_book_by_id()`: Find and display book by ID
- `find_book_by_title()`: Find and display books by title
- `find_books_by_author()`: Find and display books by author
- `find_books_by_genre()`: Find and display books by genre
- `delete_author()`: Interactive author deletion with confirmation
- `delete_book()`: Interactive book deletion with confirmation

### Utility Functions
- `get_user_input(prompt, validator, error_msg)`: Generic input function with validation
- `exit_program()`: Graceful program exit
- `initialize_database()`: Database initialization

## Debug Utilities (`lib/debug.py`)

The debug module provides utilities for development and testing:

- **Sample Data Generation**: Create realistic test data using Faker library
- **Database Management**: Clear data, reset database, show database info
- **Development Tools**: Debug menu for testing and development

### Debug Menu Options
1. **Create Sample Data**: Generate 5 authors and 15 books with realistic data
2. **Clear All Data**: Remove all data from the database
3. **Show Database Info**: Display current database state
4. **Reset Database**: Clear data and recreate tables

## Database Configuration (`lib/models/__init__.py`)

The database configuration module handles:

- **SQLAlchemy Setup**: Engine, session, and base configuration
- **Database URL**: Configurable via environment variable (defaults to SQLite)
- **Table Creation**: Automatic table creation function
- **Session Management**: Database session factory

## Key Features and Best Practices

### Object-Oriented Programming
- **Encapsulation**: Each model encapsulates its data and behavior
- **Inheritance**: Models inherit from SQLAlchemy Base class
- **Polymorphism**: Consistent interface across all models
- **Abstraction**: Clean separation between data layer and presentation layer

### Database Design
- **One-to-Many Relationship**: Author to Books relationship
- **Foreign Key Constraints**: Proper referential integrity
- **Unique Constraints**: Email and ISBN uniqueness
- **Cascade Deletion**: Deleting author removes associated books

### User Experience
- **Input Validation**: Comprehensive validation with helpful error messages
- **Confirmation Dialogs**: Safety confirmations for destructive operations
- **Clear Navigation**: Intuitive menu structure with back options
- **Rich Feedback**: Success/error messages with visual indicators
- **Graceful Error Handling**: Proper exception handling throughout

### Code Organization
- **Separation of Concerns**: Clear separation between models, CLI, and helpers
- **Modular Design**: Each module has a specific responsibility
- **Reusable Functions**: Helper functions designed for reusability
- **Clean Imports**: Organized import statements

## Dependencies

- **SQLAlchemy**: Object-Relational Mapping and database operations
- **Faker**: Sample data generation for testing (development only)

## Future Enhancements

Potential improvements for future versions:

1. **User Authentication**: Add user login and role-based access
2. **Book Borrowing**: Implement borrowing/returning functionality
3. **Advanced Search**: Full-text search capabilities
4. **Data Export**: Export data to CSV/JSON formats
5. **Web Interface**: Add a web-based interface
6. **Book Reviews**: Add rating and review system
7. **Inventory Management**: Track book availability and copies

## Contributing

This project follows standard Python development practices:

1. Use meaningful variable and function names
2. Add docstrings to all functions and classes
3. Handle exceptions gracefully
4. Validate all user inputs
5. Follow PEP 8 style guidelines

## License

This project is created for educational purposes as part of the Phase 3 curriculum requirements.

---

**Happy Library Managing! 📚✨**