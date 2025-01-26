class Archivo:
    def __init__(self, nombre):
        """
        Constructor de la clase Archivo.
        Inicializa el nombre del archivo y abre el archivo en modo escritura.
        """
        self.nombre = nombre
        self.archivo = open(nombre, 'w')
        print(f"Archivo '{self.nombre}' abierto.")

    def escribir(self, texto):
        """
        Método para escribir texto en el archivo.
        """
        self.archivo.write(texto)
        print(f"Escrito en el archivo '{self.nombre}': {texto}")

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Cierra el archivo si está abierto.
        """
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre}' cerrado.")

# Demostración del uso de la clase Archivo
archivo = Archivo("ejemplo.txt")
archivo.escribir("Hola, mundo!")
del archivo  # Esto invoca al destructor explícitamente
