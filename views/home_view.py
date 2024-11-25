# Importación de las bibliotecas necesarias
import customtkinter as ctk
from tkinter import ttk
from controllers.library import Library
from views.create_book import CreateBookView
from views.create_user import CreateUserView
from views.return_book import ReturnBookView

# Vista principal de la Biblioteca (Home)
class HomeView(ctk.CTkFrame):
    # Instancia de la clase Library para gestionar los libros
    library = Library()
    treeview = None  # Variable para almacenar la vista de los libros

    def __init__(self, parent, controller):
        # Inicialización de la clase base (CTkFrame) y configuración del controlador
        super().__init__(parent)
        self.controller = controller

        # Título de la vista Home
        title_label = ctk.CTkLabel(self, text="Library Home", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Botón para crear un nuevo libro
        self.create = ctk.CTkButton(self, text="Create Book", command=self.create_action, fg_color="#1f6aa5")
        self.create.pack(pady=10, padx=50, fill="x")

        # Botón para crear un nuevo usuario
        self.userssss = ctk.CTkButton(self, text="Create User", command=self.user_create, fg_color="#1f6aa5")
        self.userssss.pack(pady=10, padx=50, fill="x")

        # Botón para devolver un libro
        self.return_book = ctk.CTkButton(self, text="Return Book", command=self.return_book, fg_color="#1f6aa5")
        self.return_book.pack(pady=10, padx=50, fill="x")

        # Campo para buscar un libro por ID
        id_label = ctk.CTkLabel(self, text="Enter Book ID", font=("Arial", 14))
        id_label.pack(pady=(10, 5))
        self.id_input = ctk.CTkEntry(self, placeholder_text="Enter the book ID here")
        self.id_input.pack(pady=5, padx=50, fill="x")

        # Botón para realizar la búsqueda
        search_button = ctk.CTkButton(self, text="Search", command=self.search_action, fg_color="#1f6aa5")
        search_button.pack(pady=10, padx=50, fill="x")

        # Etiqueta para mostrar el mensaje de resultados de la búsqueda
        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 12), text_color="#ff0000")
        self.result_label.pack(pady=20, padx=20, fill="x")

        # Vista de los libros en un Treeview (tabla)
        self.treeview = ttk.Treeview(self, columns=("ID", "Name", "Author", "Stock"), show="headings")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Name", text="Name")
        self.treeview.heading("Author", text="Author")
        self.treeview.heading("Stock", text="Stock")
        self.treeview.pack(pady=20, padx=20)

        # Campo para ingresar la identificación del usuario
        self.identification_label = ctk.CTkLabel(self, text="Identification", font=("Arial", 14))
        self.identification_label.pack(pady=(10, 5))
        self.identification_input = ctk.CTkEntry(self, placeholder_text="Enter the user identification here")
        self.identification_input.pack(pady=5, padx=50, fill="x")

        # Botón para realizar el préstamo del libro
        loan_button = ctk.CTkButton(self, text="Loan Book", command=self.loan_action, fg_color="#28a745", state="disabled")
        loan_button.pack(pady=10, padx=50, fill="x")

        # Etiqueta para mostrar mensajes relacionados al préstamo de libros
        self.label_loan = ctk.CTkLabel(self, text="", font=("Arial", 14), fg_color="#ff0000")
        self.label_loan.pack(pady=(10, 5))

        # Guardar el botón de préstamo como atributo para habilitarlo más tarde
        self.loan_button = loan_button

    def search_action(self):
        """ Acción de búsqueda de libro por ID """
        # Realizar la búsqueda del libro usando la ID ingresada
        book = self.library.search_books(self.id_input.get())
        
        # Limpiar los resultados previos en el Treeview
        self.result_label.configure(text="")
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        if book:
            # Si se encuentra el libro, habilitar el botón de préstamo y mostrar los detalles
            self.loan_button.configure(state="enabled")
            self.treeview.insert("", "end", values=(book.id, book.name, book.autor, book.stock))
        else:
            # Si no se encuentra el libro, deshabilitar el botón de préstamo y mostrar mensaje de error
            self.loan_button.configure(state="disabled")
            self.result_label.configure(text="No se encontraron libros")

    def loan_action(self):
        """ Acción de préstamo de libro """
        # Realizar el préstamo del libro usando la ID del libro y la identificación del usuario
        self.label_loan.configure(text=f"{self.library.loan_books(self.id_input.get(), self.identification_input.get())}")

    def create_action(self):
        """ Acción de creación de un nuevo libro """
        # Mostrar la vista para crear un nuevo libro
        self.controller.show_frame(CreateBookView)

    def user_create(self):
        """ Acción de creación de un nuevo usuario """
        # Mostrar la vista para crear un nuevo usuario
        self.controller.show_frame(CreateUserView)

    def return_book(self):
        """ Acción para devolver un libro """
        # Mostrar la vista para devolver un libro
        self.controller.show_frame(ReturnBookView)
