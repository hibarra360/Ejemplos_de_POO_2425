class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):  # Para mostrar información del producto
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"


class Inventario:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self._productos):
            print("Error: Ya existe un producto con ese ID.")
            return

        self._productos.append(producto)
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id):
        for i, producto in enumerate(self._productos):
            if producto.get_id() == id:
                del self._productos[i]
                print("Producto eliminado correctamente.")
                return

        print("Error: No se encontró ningún producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self._productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado correctamente.")
                return

        print("Error: No se encontró ningún producto con ese ID.")

    def buscar_producto(self, nombre):
        resultados = [producto for producto in self._productos if nombre.lower() in producto.get_nombre().lower()]
        return resultados

    def mostrar_inventario(self):
        if not self._productos:
            print("El inventario está vacío.")
            return

        print("Inventario:")
        for producto in self._productos:
            print(producto)


# Interfaz de usuario en la consola
inventario = Inventario()

while True:
    print("\n--- Sistema de Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto(s)")
    print("5. Mostrar inventario")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    try:
        if opcion == '1':
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (o presione Enter para omitir): ")
            precio = input("Ingrese el nuevo precio (o presione Enter para omitir): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                print("Resultados de la búsqueda:")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            break

        else:
            print("Opción inválida. Intente de nuevo.")

    except ValueError:
        print("Error: Ingrese valores válidos para cantidad y precio.")