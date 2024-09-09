#pruebaCommit
#Mensaje de prueba cambio commit rep local y repositorio
def calcular_edades(humanYears):
    # Inicializamos las variables para los años de gato y de perro
    catYears = 0
    dogYears = 0

    # Calculamos los años de gato
    if humanYears >= 1:
        catYears += 15  # Primer año del gato
    if humanYears >= 2:
        catYears += 9   # Segundo año del gato
    if humanYears > 2:
        catYears += (humanYears - 2) * 4  # Cada año adicional suma 4 años de gato

    # Calculamos los años de perro
    if humanYears >= 1:
        dogYears += 15  # Primer año del perro
    if humanYears >= 2:
        dogYears += 9   # Segundo año del perro
    if humanYears > 2:
        dogYears += (humanYears - 2) * 5  # Cada año adicional suma 5 años de perro

    return [humanYears, catYears, dogYears]

# Solicitar al usuario el número de años humanos
humanYears = int(input("Introduce el número de años humanos: "))

# Calcular y mostrar el resultado
resultado = calcular_edades(humanYears)
print(f" Años humanos: {resultado[0]} ;\n Años humanos en gato: {resultado[1]} ; \n Años humano en perro: {resultado[2]} ;")


print("\n", type(resultado))