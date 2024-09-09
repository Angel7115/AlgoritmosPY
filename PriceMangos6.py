def calcular_costo_mangos(cantidad, precio_por_mango):
    """
    Calcula el costo total de los mangos aplicando la oferta "3 por el precio de 2".
    También calcula cuántos mangos se pagan y cuántos son gratis.

    Parámetros:
    cantidad (int): Número de mangos comprados.
    precio_por_mango (float): Precio por mango en la moneda local.

    Retorna:
    tuple: (costo_total, mangos_pagados, mangos_gratis)
    """
    # Por cada 3 mangos, solo se pagan 2
    grupos_de_tres = cantidad // 3  # Cada grupo de 3 tiene 1 mango gratis
    mangos_pagados = cantidad - grupos_de_tres  # Los mangos que se pagan son todos menos los mangos gratis
    mangos_gratis = grupos_de_tres  # Los mangos gratis son exactamente los grupos de 3

    # Calculamos el costo total
    costo_total = mangos_pagados * precio_por_mango

    return costo_total, mangos_pagados, mangos_gratis


# Solicitar al usuario la cantidad de mangos y el precio por mango
try:
    cantidad_mangos = int(input("Introduce la cantidad de mangos que deseas comprar: "))
    precio_por_mango = float(input("Introduce el precio por mango (en tu moneda local): "))

    # Verificar si los valores son positivos
    if cantidad_mangos < 0 or precio_por_mango < 0:
        print("Por favor, introduce valores positivos para la cantidad y el precio.")
    else:
        # Calcular el costo total, la cantidad de mangos pagados y los mangos gratis
        costo_total, mangos_pagados, mangos_gratis = calcular_costo_mangos(cantidad_mangos, precio_por_mango)

        # Mostrar el resultado al usuario
        print(f"El costo total de {cantidad_mangos} mangos es: {costo_total:.2f} (aplicando la oferta '3 por 2').")
        print(f"Pagaste por {mangos_pagados} mangos y obtuviste {mangos_gratis} gratis gracias a la oferta.")
except ValueError:
    print("Por favor, introduce valores numéricos válidos para la cantidad de mangos y el precio por mango.")
