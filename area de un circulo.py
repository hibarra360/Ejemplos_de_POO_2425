# Programa para calcular el área de un círculo
# Este programa solicita al usuario el radio de un círculo y calcula su área.

import math


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    :param radio: El radio del círculo (float)
    :return: El área del círculo (float)
    """
    area = math.pi * (radio ** 2)
    return area


def main():
    # Solicitar al usuario el radio del círculo
    radio = float(input("Introduce el radio del círculo: "))

    # Verificar que el radio sea positivo
    if radio > 0:
        # Calcular el área del círculo
        area = calcular_area_circulo(radio)

        # Mostrar el resultado
        print(f"El área del círculo con radio {radio} es {area:.2f}")
    else:
        print("El radio debe ser un número positivo.")


# Ejecutar la función principal
if __name__ == "__main__":
    main()
