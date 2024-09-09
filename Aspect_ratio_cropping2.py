import math


def convertir_a_16_9(y_resolution):
    """
    Convierte una resolución arbitraria de altura (Y) a una resolución con aspecto 16:9.

    Parámetros:
    y_resolution (int): Resolución en el eje Y (altura).

    Retorna:
    int: Resolución en el eje X (ancho) correspondiente a un aspecto de 16:9.
    """
    # Relación de aspecto 16:9 implica que x/y = 16/9
    # Entonces, x = (16/9) * y
    aspect_ratio = 16 / 9
    x_resolution = aspect_ratio * y_resolution

    # Redondeamos hacia arriba para obtener el valor entero más cercano
    x_resolution = math.ceil(x_resolution)

    return x_resolution


# Solicitar la altura (Y) al usuario
try:
    y_resolution = int(input("Introduce la resolución en el eje Y (altura de la imagen o video): "))

    # Verificar si la entrada es un número positivo
    if y_resolution <= 0:
        print("Por favor, introduce un número positivo para la altura.")
    else:
        # Convertir a una resolución con aspecto 16:9
        x_resolution_16_9 = convertir_a_16_9(y_resolution)

        # Mostrar el resultado al usuario
        print(
            f"Para mantener una altura de {y_resolution} píxeles y convertir a un aspecto 16:9, el ancho debe ser de {x_resolution_16_9} píxeles.")
except ValueError:
    print("Por favor, introduce un número válido para la altura.")
