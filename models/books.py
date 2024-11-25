from sqlalchemy import Column, ForeignKey, Integer, String, Date
from db.database import Base
from sqlalchemy.orm import relationship


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    category = Column(String(200), nullable=False)
    name = Column(String(255), nullable=False, unique=True) 
    stock = Column(Integer, nullable=False)
    autor = Column(String(255), nullable=False)

    library_loan = relationship('LibraryLoan', back_populates='book')

