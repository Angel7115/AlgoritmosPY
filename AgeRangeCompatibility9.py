import math


def rango_edad(age):
    """
    Calcula el rango de edad mínimo y máximo basado en la regla clásica de citas o una fórmula alternativa para edades <= 14.

    Parámetros:
    age (int): Edad de la persona (1 <= age <= 100).

    Retorna:
    str: Rango de edad en el formato "min-max", donde min y max son enteros.
    """
    if age > 14:
        # Usar la regla clásica "mitad de la edad más siete"
        min_age = age / 2 + 7
        max_age = (age - 7) * 2
    else:
        # Usar la fórmula alternativa para edades <= 14
        min_age = age - 0.10 * age
        max_age = age + 0.10 * age

    # Redondear hacia abajo a enteros
    min_age = math.floor(min_age)
    max_age = math.floor(max_age)

    return f"{min_age}-{max_age}"


# Solicitar al usuario la edad
try:
    edad = int(input("Introduce la edad de la persona (1-100): "))

    # Verificar que la edad esté en el rango válido
    if 1 <= edad <= 100:
        # Calcular el rango de edad
        rango = rango_edad(edad)

        # Mostrar el resultado al usuario
        print(f"El rango de edad recomendado es: {rango}")
    else:
        print("Por favor, introduce una edad entre 1 y 100.")
except ValueError:
    print("Por favor, introduce un valor numérico válido para la edad.")
