# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado."
        else:
            return f"El libro '{self.titulo}' no está disponible."

    def devolver(self):
        self.disponible = True
        return f"El libro '{self.titulo}' ha sido devuelto."

    def __str__(self):
        estado = "disponible" if self.disponible else "no disponible"
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn}) - {estado}"

# Definición de la clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        return f"El libro '{libro.titulo}' ha sido agregado a la biblioteca."

    def listar_libros(self):
        return [str(libro) for libro in self.libros]

# Creación de objetos y uso de la biblioteca
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-3-16-148410-0")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-0-14-243723-0")

biblioteca = Biblioteca()
print(biblioteca.agregar_libro(libro1))  # Agregar libro a la biblioteca
print(biblioteca.agregar_libro(libro2))  # Agregar otro libro

print(biblioteca.listar_libros())  # Listar todos los libros

print(libro1.prestar())  # Prestar un libro
print(libro1.prestar())  # Intentar prestar el mismo libro nuevamente

print(libro1.devolver())  # Devolver el libro
print(biblioteca.listar_libros())  # Listar todos los libros nuevamente