import customtkinter as ctk
from controllers.library import Library

class CreateUserView(ctk.CTkFrame):
    # Instancia de la clase Library para gestionar las operaciones relacionadas con los usuarios
    library = Library()

    def __init__(self, parent, controller):
        # Inicialización de la clase base (CTkFrame) y configuración del controlador
        super().__init__(parent)
        self.controller = controller

        # Título de la vista "Crear Usuario"
        title_label = ctk.CTkLabel(self, text="Crear Usuario", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Botón para regresar a la vista principal (Home)
        self.tohome = ctk.CTkButton(self, text="Regresar al home", command=self.to_home, fg_color="#1f6aa5")
        self.tohome.pack(pady=10, padx=50, fill="x")
        
        # Llamada al método para crear los campos de entrada (nombre e identificación)
        self.create_input_fields()

        # Botón para guardar el usuario
        save_button = ctk.CTkButton(self, text="Guardar Usuario", command=self.save_user, fg_color="#1f6aa5")
        save_button.pack(pady=20, padx=50, fill="x")

        # Mensaje de confirmación o error
        self.message_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.message_label.pack(pady=(10, 5))

    def to_home(self):
        """Método para regresar a la vista principal (Home)"""
        from views.home_view import HomeView
        # Cambiar a la vista HomeView
        self.controller.show_frame(HomeView)

    def create_input_fields(self):
        """Crea los campos de entrada para nombre e identificación"""
        # Campo para el nombre del usuario
        name_label = ctk.CTkLabel(self, text="Nombre", font=("Arial", 14))
        name_label.pack(pady=(10, 5))
        self.name_input = ctk.CTkEntry(self, placeholder_text="Introduce el nombre del usuario")
        self.name_input.pack(pady=5, padx=50, fill="x")

        # Campo para la identificación del usuario
        identification_label = ctk.CTkLabel(self, text="Identificación", font=("Arial", 14))
        identification_label.pack(pady=(10, 5))
        self.identification_input = ctk.CTkEntry(self, placeholder_text="Introduce la identificación (11 dígitos)")
        self.identification_input.pack(pady=5, padx=50, fill="x")

    def save_user(self):
        """Lógica para guardar el usuario"""
        # Obtener los valores de los campos de entrada
        name = self.name_input.get()
        identification = self.identification_input.get()

        # Validar que ambos campos estén llenos
        if not name or not identification:
            # Mostrar mensaje de error si los campos están vacíos
            self.message_label.configure(text="Todos los campos son obligatorios.", text_color="red")
            return

        # Lógica para crear el usuario a través del controlador Library
        message = self.library.create_user(name, identification)  # Método que debe estar implementado en la clase Library
        # Mostrar el mensaje de éxito o error
        self.message_label.configure(text=message, text_color="green")
