from models.books import Books
from db.database import SessionLocal
from sqlalchemy.exc import IntegrityError
from models.books import Books
from models.users import Users
from models.libraryloan import LibraryLoan
from datetime import datetime, timedelta
from sqlalchemy import update

class Library():
    def search_books(self, id_book):
        db = SessionLocal()
        book_db = db.query(Books).filter(Books.id == id_book).first()
        db.close()
        return book_db 
    
    def loan_books(self, id_book, user_identification):
        db = SessionLocal()
        user_db = db.query(Users).filter(Users.identification == user_identification).first()
        message = "No se pudo realizar el préstamo"
        if user_db:
            book = db.query(Books).filter(Books.id == id_book).first()
            if book and book.stock > 0:
                loan_db = LibraryLoan(
                    user_id=user_db.id,
                    book_id=id_book,
                    due_date=(datetime.now() + timedelta(days=4)),
                    loan_date=datetime.now()
                )
                db.add(loan_db)
                db.execute(
                    update(Books).
                    where(Books.id == id_book).
                    values(stock=(book.stock - 1))
                )
                db.commit()
                db.refresh(loan_db)
                message = f"Préstamo exitoso al usuario con nombre: {user_db.name}"
        else:
            message = "No se pudo realizar el préstamo"
        db.close()
        return message
    
    def create_book(self, category, name, stock, autor):
        db = SessionLocal()
        message = "El libro no pudo ser creado"
        try:
            # Crear una instancia del libro con los valores proporcionados
            new_book = Books(category=category, name=name, stock=stock, autor=autor)
            db.add(new_book)
            db.commit()  # Guardar los cambios
            db.refresh(new_book)  # Refrescar la instancia para obtener los datos actuales de la base de datos
            message = f"Libro '{name}' creado exitosamente."
        except IntegrityError:  # Si ocurre un error de integridad, como un nombre duplicado
            db.rollback()  # Hacer rollback para deshacer cambios
            message = "Ya existe un libro con ese nombre."
        except Exception as e:
            db.rollback()
            message = f"Error: {str(e)}"
        finally:
            db.close()
        return message

    def create_user(self, name, identification):
        db = SessionLocal()
        existing_user = db.query(Users).filter(Users.identification == identification).first()
        if existing_user:
            db.close()
            return "El usuario ya existe."
        
        new_user = Users(name=name, identification=identification)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        db.close()

        return f"Usuario '{name}' creado exitosamente."
    
    def return_book(self, loan_id):
        db = SessionLocal()
        # Buscar el préstamo por el ID
        loan = db.query(LibraryLoan).filter(LibraryLoan.id == loan_id).first()

        if not loan:
            db.close()
            return "El préstamo no existe."

        # Buscar el libro relacionado con el préstamo
        book = db.query(Books).filter(Books.id == loan.book_id).first()

        # Devolver el libro (incrementar stock)
        if book:
            book.stock += 1
            db.commit()

            # Eliminar el préstamo
            db.delete(loan)
            db.commit()

            return f"Libro devuelto exitosamente: {book.name}"

        db.close()
        return "Error al devolver el libro."

    def get_all_loans(self):
        db = SessionLocal()
        loans = db.query(LibraryLoan).join(Books).join(Users).all()  # Obtiene los préstamos con información de libros y usuarios
        print(loans)
        return loans
