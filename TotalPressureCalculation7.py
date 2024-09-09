def calcular_presion_total(M1, M2, m1, m2, V, T):
    """
    Calcula la presión total ejercida por dos gases en un recipiente usando la fórmula de los gases ideales.

    Parámetros:
    M1 (float): Masa molar del primer gas en g/mol.
    M2 (float): Masa molar del segundo gas en g/mol.
    m1 (float): Masa del primer gas en gramos.
    m2 (float): Masa del segundo gas en gramos.
    V (float): Volumen del recipiente en dm³.
    T (float): Temperatura en grados Celsius.

    Retorna:
    float: La presión total en atmósferas (atm).
    """
    # Convertir la temperatura de Celsius a Kelvin
    T_kelvin = T + 273.15

    # Constante de gas ideal en dm³⋅atm⋅K⁻¹⋅mol⁻¹
    R = 0.082

    # Calcular los moles de cada gas
    n1 = m1 / M1
    n2 = m2 / M2

    # Aplicar la fórmula de los gases ideales para calcular la presión total
    P_total = (n1 + n2) * R * T_kelvin / V

    return P_total


# Solicitar los valores al usuario
try:
    M1 = float(input("Introduce la masa molar del primer gas (g/mol): "))
    M2 = float(input("Introduce la masa molar del segundo gas (g/mol): "))
    m1 = float(input("Introduce la masa del primer gas (g): "))
    m2 = float(input("Introduce la masa del segundo gas (g): "))
    V = float(input("Introduce el volumen del recipiente (dm³): "))
    T = float(input("Introduce la temperatura (°C): "))

    # Verificar que los valores sean positivos
    if M1 <= 0 or M2 <= 0 or m1 < 0 or m2 < 0 or V <= 0 or T < -273.15:
        print("Por favor, introduce valores positivos y la temperatura no puede ser menor a -273.15°C.")
    else:
        # Calcular la presión total
        presion_total = calcular_presion_total(M1, M2, m1, m2, V, T)

        # Mostrar el resultado al usuario
        print(f"La presión total ejercida por los gases es: {presion_total:.2f} atm.")
except ValueError:
    print("Por favor, introduce valores numéricos válidos para todos los parámetros.")
