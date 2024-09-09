#Actualizacion de Tasa de cambio CNY 6.55 a 7.11 dia 09/09/24
def convertir_usd_a_cny(cantidad_usd):
    """
    Convierte una cantidad en USD a CNY utilizando una tasa de cambio de 6.75.

    Parámetros:
    cantidad_usd (int): Cantidad en dólares estadounidenses (USD).

    Retorna:
    str: La cantidad equivalente en yuanes chinos (CNY), formateada con dos decimales, seguida de 'Chinese Yuan'.
    """
    # Tasa de conversión USD a CNY
    tasa_conversion = 7.11

    # Realizamos la conversión
    cantidad_cny = cantidad_usd * tasa_conversion

    # Formateamos la cantidad con dos decimales y la convertimos en cadena
    cantidad_cny_formateada = f"{cantidad_cny:.2f} Chinese Yuan"

    return cantidad_cny_formateada


# Solicitar al usuario la cantidad en USD
try:
    cantidad_usd = int(input("Introduce la cantidad en dólares estadounidenses (USD): "))

    # Verificar si la entrada es un número positivo
    if cantidad_usd < 0:
        print("Por favor, introduce una cantidad positiva en USD.")
    else:
        # Convertir a yuanes chinos
        resultado_cny = convertir_usd_a_cny(cantidad_usd)

        # Mostrar el resultado al usuario
        print(f"El equivalente de {cantidad_usd} USD es: {resultado_cny}.")
except ValueError:
    print("Por favor, introduce una cantidad válida en dólares (solo números enteros).")
