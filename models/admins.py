from sqlalchemy import Column, ForeignKey, Integer, String, Date
from db.database import Base
from sqlalchemy.orm import relationship

class Admins(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    

