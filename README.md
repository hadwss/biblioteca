# Biblioteca
Este proyecto es una aplicación de escritorio diseñada para gestionar de manera eficiente el inventario de una biblioteca, permitiendo a los usuarios registrar, buscar, prestar y devolver libros. Está pensado para bibliotecas pequeñas o medianas que deseen modernizar sus procesos y ofrecer una mejor experiencia a sus usuarios.

La aplicación sigue el patrón de diseño Modelo-Vista-Controlador (MVC) y utiliza Python junto con Tkinter para la interfaz gráfica. Es una solución ligera, accesible y fácil de usar.

Características
Gestión de libros:
Registrar nuevos libros con atributos como título, autor, género, y cantidad disponible.
Actualizar información de libros existentes.
Eliminar libros del inventario.
Búsqueda de libros:
Permite buscar por título, autor o género.
Préstamos y devoluciones:
Registrar préstamos de libros a usuarios con fechas de vencimiento.
Gestionar devoluciones, actualizando la disponibilidad.
Reportes:
Generar reportes de libros más prestados o atrasos en devoluciones.
Control de usuarios:
Registrar usuarios que interactúan con la biblioteca (lectores o administradores).
Validar credenciales de acceso.
Tecnologías Utilizadas
Lenguaje de programación: Python
Biblioteca para IU: Tkinter
Base de datos: SQLite (integrada y ligera)
Generación de reportes: PDFkit o similar
Estructura del Proyecto
El sistema está organizado siguiendo el patrón MVC:

# Modelo:
Clases para representar libros, usuarios, y préstamos.
Manejo de la base de datos SQLite.
# Vista:
Interfaces gráficas intuitivas creadas con Tkinter.
Ventanas para registrar libros, realizar búsquedas, gestionar préstamos, etc.
# Controlador:
Maneja la interacción entre la vista y el modelo.
Lógica de validación, consultas y actualizacione
