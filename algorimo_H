import numpy as np
import random

# Función para calcular la distancia entre dos ciudades
def calcular_distancia(ciudad1, ciudad2):
    return np.linalg.norm(ciudad1 - ciudad2)

# Función para construir una solución de forma aleatoria
def construir_solucion(feromonas, distancias):
    num_ciudades = len(feromonas)
    solucion = [random.randint(0, num_ciudades - 1)]
    disponibles = list(range(num_ciudades))
    disponibles.remove(solucion[0])
    
    for _ in range(num_ciudades - 1):
        ciudad_actual = solucion[-1]
        probabilidades = []
        
        for ciudad in disponibles:
            probabilidad = (feromonas[ciudad_actual][ciudad] ** alpha) * \
                           ((1.0 / distancias[ciudad_actual][ciudad]) ** beta)
            probabilidades.append(probabilidad)
        
        suma_probabilidades = sum(probabilidades)
        probabilidades = [p / suma_probabilidades for p in probabilidades]
        
        siguiente_ciudad = np.random.choice(disponibles, p=probabilidades)
        solucion.append(siguiente_ciudad)
        disponibles.remove(siguiente_ciudad)
    
    return solucion

# Función para evaluar una solución calculando su longitud total
def evaluar_solucion(solucion, distancias):
    longitud_total = 0
    for i in range(len(solucion)):
        ciudad_actual = solucion[i]
        ciudad_siguiente = solucion[(i + 1) % len(solucion)]
        longitud_total += distancias[ciudad_actual][ciudad_siguiente]
    return longitud_total

# Parámetros del algoritmo
num_ciudades = 10  # Número de ciudades
num_hormigas = 20  # Número de hormigas
num_iteraciones = 100  # Número de iteraciones
alpha = 1.0  # Peso de la feromona
beta = 2.0  # Peso de la visibilidad
rho = 0.1  # Tasa de evaporación de feromonas

# Generar ciudades y calcular distancias
ciudades = np.random.rand(num_ciudades, 2)
distancias = np.zeros((num_ciudades, num_ciudades))
for i in range(num_ciudades):
    for j in range(num_ciudades):
        distancias[i][j] = calcular_distancia(ciudades[i], ciudades[j])

# Inicializar feromonas
feromonas = np.ones((num_ciudades, num_ciudades))

# Ciclo principal del algoritmo
for iteracion in range(num_iteraciones):
    mejores_soluciones = []
    
    for _ in range(num_hormigas):
        solucion = construir_solucion(feromonas, distancias)
        longitud = evaluar_solucion(solucion, distancias)
        mejores_soluciones.append((solucion, longitud))
    
    mejores_soluciones.sort(key=lambda x: x[1])
    mejor_solucion_actual = mejores_soluciones[0]
    
    # Actualizar feromonas
    for i in range(num_ciudades):
        for j in range(num_ciudades):
            feromonas[i][j] *= (1.0 - rho)
    
    for i in range(num_ciudades):
        ciudad_actual = mejor_solucion_actual[0][i]
        ciudad_siguiente = mejor_solucion_actual[0][(i + 1) % num_ciudades]
        feromonas[ciudad_actual][ciudad_siguiente] += (1.0 / mejor_solucion_actual[1])
    
    print(f"Iteración {iteracion + 1}: Longitud de la mejor solución = {mejor_solucion_actual[1]}")

# Mostrar la mejor solución encontrada
mejor_solucion = mejores_soluciones[0][0]
print("Mejor solución encontrada:", mejor_solucion)
print("Longitud de la mejor solución:", mejores_soluciones[0][1])
