def nba_extrap(ppg, mpg):
    """
    Extrapola los puntos por juego (ppg) de un jugador a 48 minutos basándose en los puntos por juego y minutos jugados.

    Parámetros:
    ppg (float): Puntos por juego actuales del jugador.
    mpg (float): Minutos por juego actuales del jugador.

    Retorna:
    float: Puntos extrapolados para 48 minutos, redondeado a la décima más cercana.
    """
    if mpg == 0:
        # Si los minutos jugados son 0, no se puede extrapolar, así que retornamos 0.
        return 0

    # Extrapolar puntos por 48 minutos usando la regla de tres simple
    puntos_por_48_minutos = (ppg * 48) / mpg

    # Redondear el resultado a la décima más cercana
    return round(puntos_por_48_minutos, 1)


# Solicitar al usuario los puntos por juego y minutos por juego
try:
    ppg = float(input("Introduce los puntos por juego del jugador: "))
    mpg = float(input("Introduce los minutos por juego del jugador: "))

    # Verificar que los valores sean positivos o cero
    if ppg < 0 or mpg < 0:
        print("Por favor, introduce valores no negativos para los puntos y minutos.")
    else:
        # Calcular los puntos extrapolados para 48 minutos
        puntos_extrapolados = nba_extrap(ppg, mpg)

        # Mostrar el resultado al usuario
        print(f"Los puntos extrapolados para 48 minutos son: {puntos_extrapolados:.1f}")
except ValueError:
    print("Por favor, introduce valores numéricos válidos para los puntos y minutos.")
