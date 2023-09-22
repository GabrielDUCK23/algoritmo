import math
import random

# Función de costo (puedes reemplazarla con tu propia función)
def costo(solucion):
    # En este ejemplo, asumiremos que estamos minimizando una función ficticia
    return sum(solucion)

# Función para generar una solución vecina
def vecino(solucion, temperatura):
    # En este ejemplo, se generan soluciones vecinas cambiando un valor aleatorio
    indice = random.randint(0, len(solucion) - 1)
    nueva_solucion = solucion[:]
    nueva_solucion[indice] += random.uniform(-temperatura, temperatura)
    return nueva_solucion

# Función de aceptación
def aceptar_nueva_solucion(solucion_actual, nueva_solucion, temperatura):
    # Calcula la diferencia de costos entre la solución actual y la nueva solución
    delta_costo = costo(nueva_solucion) - costo(solucion_actual)

    # Si la nueva solución es mejor o se acepta con una probabilidad menor
    if delta_costo < 0 or random.random() < math.exp(-delta_costo / temperatura):
        return nueva_solucion
    else:
        return solucion_actual

# Algoritmo de recocido simulado
def recocido_simulado(solucion_inicial, temperatura_inicial, factor_enfriamiento, num_iteraciones):
    solucion_actual = solucion_inicial
    mejor_solucion = solucion_actual
    temperatura = temperatura_inicial

    for i in range(num_iteraciones):
        nueva_solucion = vecino(solucion_actual, temperatura)
        solucion_actual = aceptar_nueva_solucion(solucion_actual, nueva_solucion, temperatura)

        # Actualiza la mejor solución encontrada hasta ahora
        if costo(solucion_actual) < costo(mejor_solucion):
            mejor_solucion = solucion_actual

        # Enfría la temperatura
        temperatura *= factor_enfriamiento

    return mejor_solucion

if __name__ == "__main__":
    # Parámetros del algoritmo
    solucion_inicial = [0, 0, 0, 0, 0]  # Solución inicial (puedes cambiarla)
    temperatura_inicial = 100.0  # Temperatura inicial
    factor_enfriamiento = 0.95  # Factor de enfriamiento
    num_iteraciones = 1000  # Número de iteraciones

    mejor_solucion = recocido_simulado(solucion_inicial, temperatura_inicial, factor_enfriamiento, num_iteraciones)

    print("Mejor solución encontrada:", mejor_solucion)
    print("Costo de la mejor solución:", costo(mejor_solucion))
