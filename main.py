# Importación de bibliotecas necesarias
import customtkinter as ctk
from views.login_view import LoginView
from views.home_view import HomeView
from models.admins import Admins
from models.books import Books
from models.libraryloan import LibraryLoan
from models.users import Users
from db.database import init_db
from views.create_book import CreateBookView
from views.create_user import CreateUserView
from views.return_book import ReturnBookView

# Clase principal de la aplicación, que hereda de CTk
class App(ctk.CTk):
    def __init__(self):
        # Inicializamos la clase base
        super().__init__()
        
        # Configuramos el título y tamaño de la ventana principal
        self.title("Bibliofy")
        self.geometry("1000x1000")
        
        # Creamos un contenedor para todas las vistas
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)
        
        # Diccionario que almacenará las vistas de la aplicación
        self.frames = {}

        # Inicializamos todas las vistas que se usarán en la aplicación
        # Se asocia cada vista con su clase correspondiente
        for F in (LoginView, HomeView, CreateBookView, CreateUserView, ReturnBookView):
            # Instanciamos la vista y la almacenamos en el diccionario de frames
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
        
        # Mostramos la vista de inicio (LoginView) al iniciar la aplicación
        self.show_frame(LoginView)

    def show_frame(self, view_class):
        """Método para mostrar una vista y ocultar la anterior"""
        
        # Primero, ocultamos todos los frames para asegurar que solo uno se muestre
        for frame in self.frames.values():
            frame.pack_forget()

        # Luego, mostramos el frame correspondiente a la vista que se pasa como argumento
        frame = self.frames[view_class]
        frame.pack(fill="both", expand=True)

# Comprobamos si este archivo es el principal para ejecutar la aplicación
if __name__ == '__main__':
    # Inicializamos la base de datos al iniciar la aplicación
    init_db()
    
    # Creamos una instancia de la clase App y arrancamos el loop principal de la aplicación
    app = App()
    app.mainloop()
