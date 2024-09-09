#actualizacion de 2 a 3 decimales
def redondear_a_dos_decimales(numero):
    """
    Redondea un número a dos decimales y lo devuelve como una cadena.

    Parámetros:
    numero (float): El número a redondear.

    Retorna:
    str: El número redondeado a dos decimales como una cadena.
    """
    # Redondear el número a dos decimales
    numero_redondeado = round(numero, 3)

    # Formatear el número como una cadena con dos decimales
    return f"{numero_redondeado:.2f}"


# Solicitar al usuario que introduzca un número
try:
    numero = float(input("Introduce un número: "))

    # Redondear y mostrar el número formateado
    numero_formateado = redondear_a_dos_decimales(numero)
    print(f"El número redondeado a dos decimales es: {numero_formateado}")
except ValueError:
    print("Por favor, introduce un número válido.")
