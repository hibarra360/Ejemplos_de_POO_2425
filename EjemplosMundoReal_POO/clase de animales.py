# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo encapsulado
        self.__edad = edad      # Atributo encapsulado

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau"

# Clase derivada
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        return "Miau"

# Ejemplo de polimorfismo
def imprimir_sonido(animal):
    print(f"{animal.get_nombre()} dice {animal.hacer_sonido()}")

# Crear instancias de las clases
perro = Perro("Rex", 5, "Labrador")
gato = Gato("Mimi", 3, "Blanco")

# Usar los métodos para demostrar la funcionalidad
print(f"El perro se llama {perro.get_nombre()}, tiene {perro.get_edad()} años y es de raza {perro.raza}.")
print(f"El gato se llama {gato.get_nombre()}, tiene {gato.get_edad()} años y es de color {gato.color}.")

# Demostración de polimorfismo
imprimir_sonido(perro)
imprimir_sonido(gato)
