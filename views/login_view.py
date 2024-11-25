# Importación de las bibliotecas necesarias
import customtkinter as ctk
from controllers.auth import Auth
from views.home_view import HomeView

# Vista para el inicio de sesión (Login)
class LoginView(ctk.CTkFrame):
    # Instanciamos la clase Auth para manejar la autenticación
    auth = Auth()

    def __init__(self, parent, controller):
        # Inicialización de la clase base (CTkFrame) y configuración del controlador
        super().__init__(parent)
        self.controller = controller

        # Título de la vista de Login
        title_label = ctk.CTkLabel(self, text="Library Login", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Campo para ingresar el nombre de usuario (Username)
        username_label = ctk.CTkLabel(self, text="Username", font=("Arial", 14))
        username_label.pack(pady=(10, 5))
        # Campo de entrada para el nombre de usuario
        self.username_input = ctk.CTkEntry(self, placeholder_text="Enter your username")
        self.username_input.pack(pady=5, padx=50, fill="x")

        # Campo para ingresar la contraseña (Password)
        password_label = ctk.CTkLabel(self, text="Password", font=("Arial", 14))
        password_label.pack(pady=(10, 5))
        # Campo de entrada para la contraseña, con un asterisco para ocultarla
        self.password_input = ctk.CTkEntry(self, placeholder_text="Enter your password", show="*")
        self.password_input.pack(pady=5, padx=50, fill="x")

        # Botón para iniciar sesión
        login_button = ctk.CTkButton(self, text="Login", command=self.login_action, fg_color="#1f6aa5")
        login_button.pack(pady=20, padx=50, fill="x")

    def login_action(self):
        """ Acción de login para verificar las credenciales """
        # Obtener los valores ingresados en los campos de usuario y contraseña
        username = self.username_input.get()
        password = self.password_input.get()

        # Verificar si las credenciales son correctas usando la clase Auth
        if self.auth.login(username=username, password=password):
            # Si la autenticación es exitosa, mostramos un mensaje y cambiamos a la vista Home
            print("Se inició sesión correctamente.")
            self.controller.show_frame(HomeView)  # Cambiar a la vista HomeView
        else:
            # Si las credenciales son incorrectas, mostramos un mensaje de error
            print("Error en las credenciales. Intenta de nuevo.")
            # Aquí se podría agregar un mensaje visual de error si se desea
