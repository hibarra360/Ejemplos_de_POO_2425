# Definición de la clase
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

    def mostrar_edad(self):
        print(f"{self.nombre} tiene {self.edad} años.")

# Creación de objetos (instancias de la clase)
mi_perro = Perro("Fido", 3)
otro_perro = Perro("Rex", 5)

# Uso de métodos de la clase
mi_perro.ladrar()
mi_perro.mostrar_edad()

otro_perro.ladrar()
otro_perro.mostrar_edad()