import math
#Actualizacion de los litros por hora

def calcular_litros(time_hours):
    """
    Calcula la cantidad de litros de agua que Nathan beberá, dado el tiempo en horas de ciclismo.

    Nathan bebe 0.8 litros de agua por cada hora de ciclismo.

    Parámetros:
    time_hours (float): Tiempo de ciclismo en horas.

    Retorna:
    int: Litros de agua que Nathan beberá, redondeados hacia abajo.
    """
    # Nathan bebe 0.5 litros por hora
    litros = 0.8 * time_hours

    # Redondeamos hacia abajo para obtener el número entero más pequeño
    litros_redondeados = math.floor(litros)

    return litros_redondeados


# Solicitar al usuario el tiempo de ciclismo en horas
try:
    time_hours = float(input("Introduce el tiempo de ciclismo en horas: "))

    # Verificar si la entrada es un número positivo
    if time_hours < 0:
        print("Por favor, introduce un tiempo positivo en horas.")
    else:
        # Calcular la cantidad de litros que Nathan beberá
        litros_bebidos = calcular_litros(time_hours)

        # Mostrar el resultado al usuario
        print(f"Nathan beberá aproximadamente {litros_bebidos} litros de agua durante su viaje en bicicleta.")
except ValueError:
    print("Por favor, introduce un valor numérico válido para el tiempo en horas.")
