from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base, get_session

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    # One-to-many relationship with books
    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}', email='{self.email}')>"
    
    @property
    def book_count(self):
        """Return the number of books by this author"""
        from .book import Book
        session = get_session()
        try:
            count = session.query(Book).filter(Book.author_id == self.id).count()
            return count
        finally:
            session.close()
    
    @property
    def display_name(self):
        """Return formatted author name"""
        return f"{self.name} ({self.email})"
    
    # ORM Methods
    @classmethod
    def create(cls, name, email):
        """Create a new author"""
        session = get_session()
        try:
            author = cls(name=name, email=email)
            session.add(author)
            session.commit()
            # Refresh the object to ensure it's properly loaded
            session.refresh(author)
            return author
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    @classmethod
    def get_all(cls):
        """Get all authors"""
        session = get_session()
        try:
            return session.query(cls).all()
        finally:
            session.close()
    
    @classmethod
    def find_by_id(cls, author_id):
        """Find author by ID"""
        session = get_session()
        try:
            return session.query(cls).filter(cls.id == author_id).first()
        finally:
            session.close()
    
    @classmethod
    def find_by_name(cls, name):
        """Find author by name"""
        session = get_session()
        try:
            return session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()
        finally:
            session.close()
    
    @classmethod
    def find_by_email(cls, email):
        """Find author by email"""
        session = get_session()
        try:
            return session.query(cls).filter(cls.email == email).first()
        finally:
            session.close()
    
    def delete(self):
        """Delete this author"""
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
    
    def update(self, name=None, email=None):
        """Update author information"""
        session = get_session()
        try:
            if name:
                self.name = name
            if email:
                self.email = email
            session.add(self)
            session.commit()
            return self
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
