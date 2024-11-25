from sqlalchemy import Column, ForeignKey, Integer, String, Date
from db.database import Base
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    identification = Column(String(11), nullable=False, unique=True)

    library_loan = relationship('LibraryLoan', back_populates='user')

