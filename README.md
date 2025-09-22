# Library Management System

Hey! This is my Phase 3 project - a command line library management system. I built this to manage authors and books in a library database. It's a CLI app that lets you add, search, and manage library data.

## What it does

Basically, you can:
- Add authors and books to the library
- Search for stuff by name, genre, or whatever
- See statistics about your library
- Delete things when you need to

## How to run it

First, make sure you have Python 3.8+ and pipenv installed.

```bash
# Install the dependencies
pipenv install

# Run the app
python main.py
```

That's it! The app will start and show you a menu.

## Project structure

```
.
├── Pipfile                    # Dependencies
├── Pipfile.lock              # Locked versions  
├── README.md                 # This file
├── main.py                   # Entry point
└── lib/                      # Main code
    ├── models/               # Database stuff
    │   ├── __init__.py       # Database setup
    │   ├── author.py         # Author model
    │   └── book.py           # Book model
    ├── cli.py                # Main menu system
    ├── helpers.py            # Helper functions
    └── debug.py              # Testing utilities
```

## The models

### Author
- Has a name and email
- Can have multiple books
- Email has to be unique

### Book  
- Has title, ISBN, year, genre
- Belongs to one author
- ISBN has to be unique

## Main features

### Author management
- Create new authors
- View all authors
- Find authors by name or ID
- Delete authors (and their books)

### Book management
- Add books to authors
- View all books
- Find books by title, genre, or author
- Delete individual books

### Search
- Find books by author
- Find books by genre
- Search authors by name
- Search books by title

### Statistics
- See how many authors/books you have
- Books by genre breakdown
- Most prolific author
- Recent books (last 10 years)

## How I built it

I used SQLAlchemy for the database stuff. The Author and Book models have a one-to-many relationship - one author can have many books.

The CLI uses a simple menu system with while loops to keep the user in the app until they choose to exit. I added input validation for emails, ISBNs, and years to make sure people don't enter garbage data.

## Testing

I included a debug.py file that can generate sample data using the Faker library. Just run:

```bash
python lib/debug.py
```

This will let you create test authors and books to play around with.

## Dependencies

- SQLAlchemy - for database stuff
- Faker - for generating test data

## What I learned

This project helped me understand:
- How to build a proper CLI interface
- SQLAlchemy ORM and database relationships
- Input validation and error handling
- Organizing code into modules
- User experience in command line apps

The hardest part was getting the SQLAlchemy sessions right - I had some issues with detached instances at first, but I figured it out by refreshing objects after commits.

## Future improvements

If I had more time, I'd add:
- User authentication
- Book borrowing system
- Better search with full-text
- Export to CSV
- Maybe a web interface

But for now, this CLI version does everything the requirements asked for!

---

Thanks for checking out my project! 🚀