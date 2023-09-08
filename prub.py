import random


tasa_mutacion = 0.1
num_bits = 4
Poblacion = 30
NUMgeneraciones = 4


# Función para convertir un número binario en su equivalente decimal
def binario_a_decimal(binario):
    return int(binario, 2)

# Función de aptitud: calcula la aptitud usando la fórmula aptitud = x^2 + 2
def calcular_aptitud(individuo):
    x = binario_a_decimal(individuo)
    aptitud = x**2 + 2
    return aptitud



# Función de mutación: cambia un bit aleatorio en el individuo
def mutar(individuo, tasa_mutacion):
    individuo_lista = list(individuo)
    for i in range(len(individuo_lista)):
        if random.random() < tasa_mutacion:
            individuo_lista[i] = '0' if individuo_lista[i] == '1' else '1'
    return ''.join(individuo_lista)




# Inicialización de la población aleatoria
poblacionArrays = [''.join(random.choice('01') for _ in range(num_bits)) for _ in range(Poblacion)]

# Algoritmo genético
for generacion in range(NUMgeneraciones):
    print(f"Generación {generacion + 1}:")
    aptitudes = []
    for individuo in poblacionArrays:
        aptitud = calcular_aptitud(individuo)
        aptitudes.append(aptitud)
        print(f"Decimal: {binario_a_decimal(individuo)}, Binario: {individuo}, Aptitud: {aptitud}")
    
    poblacion_mutada = [mutar(individuo, tasa_mutacion) for individuo in poblacionArrays]


    # Encuentra el individuo con la mayor aptitud
    mejor_individuo_idx = aptitudes.index(max(aptitudes))
    mejor_individuo = poblacionArrays[mejor_individuo_idx]
    Mejores = []
    Mejores.append(mejor_individuo_idx)

    
    print(f"Mejor individuo en la generación {generacion + 1}: Decimal: {binario_a_decimal(mejor_individuo)}, Binario: {mejor_individuo}, Aptitud: {max(aptitudes)}")
    print("\n")
    print("Mejores",Mejores)
    
    # Reemplazar la población con los individuos mutados
    poblacionArrays = poblacion_mutada
    