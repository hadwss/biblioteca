from sqlalchemy import Column, ForeignKey, Integer, String, Date
from db.database import Base
from sqlalchemy.orm import relationship


class LibraryLoan(Base):
    __tablename__ = 'library_loan'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    loan_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)

    user = relationship('Users', back_populates='library_loan')
    book = relationship('Books', back_populates='library_loan')
