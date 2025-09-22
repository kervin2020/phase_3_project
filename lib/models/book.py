from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from . import Base, get_session
from datetime import datetime

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    isbn = Column(String(13), unique=True, nullable=False)
    publication_year = Column(Integer, nullable=False)
    genre = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    # Foreign key relationship with author
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    author = relationship("Author", back_populates="books")
    
    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author_id={self.author_id})>"
    
    @property
    def display_title(self):
        """Return formatted book title with author"""
        from .author import Author
        session = get_session()
        try:
            author = session.query(Author).filter(Author.id == self.author_id).first()
            return f"{self.title} by {author.name if author else 'Unknown Author'}"
        finally:
            session.close()
    
    @property
    def is_recent(self):
        """Check if book was published in the last 10 years"""
        current_year = datetime.now().year
        return (current_year - self.publication_year) <= 10
    
    @property
    def age(self):
        """Return the age of the book in years"""
        current_year = datetime.now().year
        return current_year - self.publication_year
    
    # ORM Methods
    @classmethod
    def create(cls, title, isbn, publication_year, genre, author_id):
        """Create a new book"""
        session = get_session()
        try:
            book = cls(
                title=title,
                isbn=isbn,
                publication_year=publication_year,
                genre=genre,
                author_id=author_id
            )
            session.add(book)
            session.commit()
            # Refresh the object to ensure it's properly loaded
            session.refresh(book)
            return book
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    @classmethod
    def get_all(cls):
        """Get all books"""
        session = get_session()
        try:
            return session.query(cls).all()
        finally:
            session.close()
    
    @classmethod
    def find_by_id(cls, book_id):
        """Find book by ID"""
        session = get_session()
        try:
            return session.query(cls).filter(cls.id == book_id).first()
        finally:
            session.close()
    
    @classmethod
    def find_by_title(cls, title):
        """Find books by title"""
        session = get_session()
        try:
            return session.query(cls).filter(cls.title.ilike(f"%{title}%")).all()
        finally:
            session.close()
    
    @classmethod
    def find_by_author_id(cls, author_id):
        """Find books by author ID"""
        session = get_session()
        try:
            return session.query(cls).filter(cls.author_id == author_id).all()
        finally:
            session.close()
    
    @classmethod
    def find_by_genre(cls, genre):
        """Find books by genre"""
        session = get_session()
        try:
            return session.query(cls).filter(cls.genre.ilike(f"%{genre}%")).all()
        finally:
            session.close()
    
    @classmethod
    def find_by_isbn(cls, isbn):
        """Find book by ISBN"""
        session = get_session()
        try:
            return session.query(cls).filter(cls.isbn == isbn).first()
        finally:
            session.close()
    
    def delete(self):
        """Delete this book"""
        session = get_session()
        try:
            session.delete(self)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def update(self, title=None, isbn=None, publication_year=None, genre=None, author_id=None):
        """Update book information"""
        session = get_session()
        try:
            if title:
                self.title = title
            if isbn:
                self.isbn = isbn
            if publication_year:
                self.publication_year = publication_year
            if genre:
                self.genre = genre
            if author_id:
                self.author_id = author_id
            session.add(self)
            session.commit()
            return self
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
