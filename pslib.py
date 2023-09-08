import random

# Definir la longitud de las cadenas
longitud_cadena = 4

# Función para generar una cadena binaria aleatoria
def generar_cadena_aleatoria():
    return ''.join(random.choice('01') for _ in range(longitud_cadena))

# Función para aplicar mutaciones
def mutar(cadena):
    indice_mutacion = random.randint(0, longitud_cadena - 1)
    nueva_cadena = cadena[:indice_mutacion] + ('0' if cadena[indice_mutacion] == '1' else '1') + cadena[indice_mutacion + 1:]
    return nueva_cadena

# Inicializar la población aleatoriamente
poblacion = [generar_cadena_aleatoria() for _ in range(10)]

# Mostrar la población inicial
print("Población inicial:")
for cadena in poblacion:
    decimal = int(cadena, 2)
    print(f"Binario: {cadena}, Decimal: {decimal}")

# Realizar mutaciones y mostrar cada generación
num_generaciones = 1
for generacion in range(num_generaciones):
    poblacion_mutada = [mutar(cadena) for cadena in poblacion]

    # Mostrar la población mutada
    print(f"\nGeneración {generacion + 1} (Mutada):")
    for cadena in poblacion_mutada:
        decimal = int(cadena, 2)
        print(f"Binario: {cadena}, Decimal: {decimal}")

    poblacion = poblacion_mutada
import random

# Definir la longitud de las cadenas
longitud_cadena = 4

# Función para generar una cadena binaria aleatoria
def generar_cadena_aleatoria():
    return ''.join(random.choice('01') for _ in range(longitud_cadena))

# Función para aplicar mutaciones
def mutar(cadena):
    indice_mutacion = random.randint(0, longitud_cadena - 1)
    nueva_cadena = cadena[:indice_mutacion] + ('0' if cadena[indice_mutacion] == '1' else '1') + cadena[indice_mutacion + 1:]
    return nueva_cadena

# Inicializar la población aleatoriamente
poblacion = [generar_cadena_aleatoria() for _ in range(10)]

# Mostrar la población inicial
print("Población inicial:")
for cadena in poblacion:
    decimal = int(cadena, 2)
    print(f"Binario: {cadena}, Decimal: {decimal}")

# Realizar mutaciones y mostrar cada generación
num_generaciones = 1
for generacion in range(num_generaciones):
    poblacion_mutada = [mutar(cadena) for cadena in poblacion]

    # Mostrar la población mutada
    print(f"\nGeneración {generacion + 1} (Mutada):")
    for cadena in poblacion_mutada:
        decimal = int(cadena, 2)
        print(f"Binario: {cadena}, Decimal: {decimal}")

    poblacion = poblacion_mutada
