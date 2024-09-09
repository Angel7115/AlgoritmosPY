def calcular_tercer_angulo(angulo1, angulo2):
    """
    Calcula el tercer ángulo de un triángulo dado que la suma de los ángulos interiores de un triángulo es siempre 180 grados.

    Parámetros:
    angulo1 (int): Primer ángulo del triángulo.
    angulo2 (int): Segundo ángulo del triángulo.

    Retorna:
    int: El tercer ángulo del triángulo.
    """
    # La suma de los ángulos interiores de cualquier triángulo es siempre 180 grados
    tercer_angulo = 180 - (angulo1 + angulo2)

    return tercer_angulo


# Solicitar los dos ángulos al usuario
try:
    angulo1 = int(input("Introduce el primer ángulo del triángulo (en grados): "))
    angulo2 = int(input("Introduce el segundo ángulo del triángulo (en grados): "))

    # Verificar que los ángulos sean positivos y que la suma no exceda 180
    if angulo1 > 0 and angulo2 > 0 and angulo1 + angulo2 < 180:
        # Calcular el tercer ángulo
        tercer_angulo = calcular_tercer_angulo(angulo1, angulo2)

        # Mostrar el resultado al usuario
        print(f"El tercer ángulo del triángulo es: {tercer_angulo} grados.")
    else:
        print(
            "Por favor, asegúrate de que ambos ángulos sean positivos y que la suma de ambos sea menor que 180 grados.")
except ValueError:
    print("Por favor, introduce valores válidos para los ángulos (solo números enteros).")
