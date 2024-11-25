from models.admins import Admins
from db.database import SessionLocal


class Auth():

    def login(self, username, password):
        is_loged = False
        db = SessionLocal()
        admin_db = db.query(Admins).filter(Admins.username == username).first()

        if(password == admin_db.password):
            is_loged = True

        db.close()
        return is_loged 