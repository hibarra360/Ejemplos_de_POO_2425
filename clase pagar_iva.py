# Definición de la clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}: ${self.precio:.2f}"

# Definición de la clase Factura
class Factura:
    def __init__(self):
        self.productos = []
        self.iva = 0.15  # 15% de IVA

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_subtotal(self):
        return sum(producto.precio for producto in self.productos)

    def calcular_iva(self):
        return self.calcular_subtotal() * self.iva

    def calcular_total(self):
        return self.calcular_subtotal() + self.calcular_iva()

    def __str__(self):
        factura_str = "\n".join(str(producto) for producto in self.productos)
        factura_str += f"\nSubtotal: ${self.calcular_subtotal():.2f}"
        factura_str += f"\nIVA (15%): ${self.calcular_iva():.2f}"
        factura_str += f"\nTotal: ${self.calcular_total():.2f}"
        return factura_str

# Ejemplo de uso
producto1 = Producto("Laptop", 1000.00)
producto2 = Producto("Mouse", 50.00)
producto3 = Producto("Teclado", 75.00)

factura = Factura()
factura.agregar_producto(producto1)
factura.agregar_producto(producto2)
factura.agregar_producto(producto3)

print(factura)