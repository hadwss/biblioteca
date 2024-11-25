import customtkinter as ctk
from controllers.library import Library

class CreateBookView(ctk.CTkFrame):
    # Instancia de la clase Library que se usará para gestionar los libros
    library = Library()

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # El controlador que se pasa desde la aplicación principal

        # Título de la vista
        title_label = ctk.CTkLabel(self, text="Crear Libro", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)
        
        # Botón para regresar al Home
        self.tohome = ctk.CTkButton(self, text="Regresar al home", command=self.to_home, fg_color="#1f6aa5")
        self.tohome.pack(pady=10, padx=50, fill="x")
        
        # Llamada al método para crear los campos de entrada (Categoría, Nombre, Stock, Autor)
        self.create_input_fields()

        # Botón para guardar el libro
        save_button = ctk.CTkButton(self, text="Guardar Libro", command=self.save_book, fg_color="#1f6aa5")
        save_button.pack(pady=20, padx=50, fill="x")

        # Etiqueta para mostrar mensajes de confirmación o error
        self.messague = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.messague.pack(pady=(10, 5))

    def create_input_fields(self):
        """Función para crear los campos de entrada del formulario de libro."""
        # Campo: Categoría
        category_label = ctk.CTkLabel(self, text="Categoría", font=("Arial", 14))
        category_label.pack(pady=(10, 5))
        self.category_input = ctk.CTkEntry(self, placeholder_text="Introduce la categoría")
        self.category_input.pack(pady=5, padx=50, fill="x")

        # Campo: Nombre
        name_label = ctk.CTkLabel(self, text="Nombre", font=("Arial", 14))
        name_label.pack(pady=(10, 5))
        self.name_input = ctk.CTkEntry(self, placeholder_text="Introduce el nombre del libro")
        self.name_input.pack(pady=5, padx=50, fill="x")

        # Campo: Stock
        stock_label = ctk.CTkLabel(self, text="Stock", font=("Arial", 14))
        stock_label.pack(pady=(10, 5))
        self.stock_input = ctk.CTkEntry(self, placeholder_text="Introduce el stock (cantidad)", validate="key")
        self.stock_input.pack(pady=5, padx=50, fill="x")

        # Campo: Autor
        autor_label = ctk.CTkLabel(self, text="Autor", font=("Arial", 14))
        autor_label.pack(pady=(10, 5))
        self.autor_input = ctk.CTkEntry(self, placeholder_text="Introduce el nombre del autor")
        self.autor_input.pack(pady=5, padx=50, fill="x")

    def to_home(self):
        """Función para regresar a la vista principal HomeView"""
        from views.home_view import HomeView
        # Cambia la vista a HomeView
        self.controller.show_frame(HomeView)

    def save_book(self):
        """Lógica para guardar el libro, llama al controlador Library."""
        category = self.category_input.get()
        name = self.name_input.get()
        stock = self.stock_input.get()
        autor = self.autor_input.get()

        # Llamar a la función del controlador para crear el libro
        self.messague.configure(text=f'{self.library.create_book(category=category, name=name, stock=stock, autor=autor)}')
