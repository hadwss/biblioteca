# Importación de las bibliotecas necesarias
import customtkinter as ctk
from controllers.library import Library
from tkinter import ttk

# Vista para devolver libros
class ReturnBookView(ctk.CTkFrame):
    # Instanciamos la clase Library para utilizar sus métodos
    library = Library()

    def __init__(self, parent, controller):
        # Inicialización de la clase base y configuración de la vista
        super().__init__(parent)
        self.controller = controller

        # Título de la vista
        title_label = ctk.CTkLabel(self, text="Devolver Libro", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Botón para regresar a la vista principal (Home)
        self.tohome = ctk.CTkButton(self, text="Regresar al home", command=self.to_home, fg_color="#1f6aa5")
        self.tohome.pack(pady=10, padx=50, fill="x")

        # Campo para ingresar el ID del préstamo
        loan_id_label = ctk.CTkLabel(self, text="ID de Préstamo", font=("Arial", 14))
        loan_id_label.pack(pady=(10, 5))
        self.loan_id_input = ctk.CTkEntry(self, placeholder_text="Introduce el ID del préstamo")
        self.loan_id_input.pack(pady=5, padx=50, fill="x")

        # Botón para ejecutar la acción de devolver el libro
        return_button = ctk.CTkButton(self, text="Devolver Libro", command=self.return_book, fg_color="#1f6aa5")
        return_button.pack(pady=20, padx=50, fill="x")

        # Etiqueta para mostrar mensajes de confirmación o error
        self.message_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.message_label.pack(pady=(10, 5))

        # Etiqueta para mostrar el título de los préstamos activos
        self.treeview_label = ctk.CTkLabel(self, text="Préstamos Activos", font=("Arial", 14))
        self.treeview_label.pack(pady=(10, 5))

        # Treeview para mostrar los préstamos activos
        self.treeview = ttk.Treeview(self, columns=("loan_id", "user_name", "book_name", "loan_date", "due_date"), show="headings")
        
        # Configuración de las columnas del Treeview
        self.treeview.heading("loan_id", text="ID Préstamo")
        self.treeview.heading("user_name", text="Usuario")
        self.treeview.heading("book_name", text="Libro")
        self.treeview.heading("loan_date", text="Fecha Préstamo")
        self.treeview.heading("due_date", text="Fecha Devolución")

        # Ajuste de tamaños y alineación de las columnas
        self.treeview.column("loan_id", width=100, anchor="center")
        self.treeview.column("user_name", width=150, anchor="center")
        self.treeview.column("book_name", width=200, anchor="center")
        self.treeview.column("loan_date", width=150, anchor="center")
        self.treeview.column("due_date", width=150, anchor="center")

        # Barra de desplazamiento para el Treeview
        treeview_scroll = ctk.CTkScrollbar(self, orientation="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=treeview_scroll.set)
        treeview_scroll.pack(side="right", fill="y")

        # Empaquetamos el Treeview en la interfaz
        self.treeview.pack(pady=10, padx=50, fill="both", expand=True)

        # Cargar los préstamos activos al inicio
        self.load_loans()

    def to_home(self):
        # Método para regresar a la vista principal (HomeView)
        from views.home_view import HomeView
        self.controller.show_frame(HomeView)

    def return_book(self):
        """Lógica para devolver el libro"""
        loan_id = self.loan_id_input.get()

        # Comprobamos si el ID del préstamo está vacío
        if not loan_id:
            # Mostramos mensaje de error si no se proporciona un ID
            self.message_label.configure(text="El ID del préstamo es obligatorio.", text_color="red")
            return

        # Lógica para devolver el libro utilizando el ID proporcionado
        message = self.library.return_book(loan_id)
        self.message_label.configure(text=message, text_color="green")
        
        # Recargamos la lista de préstamos después de devolver un libro
        self.load_loans()

    def load_loans(self):
        """Carga todos los préstamos en el Treeview"""
        # Primero, eliminamos todas las filas actuales en el Treeview
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Obtenemos todos los préstamos activos desde la biblioteca
        loans = self.library.get_all_loans()

        # Insertamos cada préstamo en el Treeview
        for loan in loans:
            # Obtenemos detalles del libro y del usuario asociados a este préstamo
            book_name = loan.book.name if loan.book else "Desconocido"
            user_name = loan.user.name if loan.user else "Desconocido"
            
            # Insertamos los detalles del préstamo en el Treeview
            self.treeview.insert("", "end", values=(loan.id, user_name, book_name, loan.loan_date, loan.due_date))
