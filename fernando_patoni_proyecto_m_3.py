# Programa que simula la maquina de galton
import numpy as np  # Importa la biblioteca NumPy para trabajar con arreglos numéricos
import matplotlib.pyplot as plt  # Importa la biblioteca Matplotlib para trazar gráficos
from random import randint  # Importa la función randint de la biblioteca random para generar números enteros aleatorios

# Función para simular la máquina de Galton
def simular_maquina_galton(cantidad_canicas, niveles_obstaculos):
    lanes = [0] * (niveles_obstaculos + 1)  # Crea una lista para contar las canicas en cada contenedor

    for _ in range(cantidad_canicas):  # Bucle para simular el lanzamiento de canicas
        stored = -1  # Inicializa la variable para rastrear la posición de la canica
        for _ in range(niveles_obstaculos):  # Bucle para simular la caída en los niveles
            stored += randint(0, 1)  # Decide aleatoriamente si la canica cae a la izquierda o derecha
        lanes[stored] += 1  # Incrementa el contador del contenedor en el que aterriza la canica

    return lanes  # Devuelve una lista con la distribución de canicas en los contenedores

# Función para graficar el histograma
def graficar_histograma(resultados):
    X = np.arange(0, len(resultados))  # Crea un arreglo de valores en el eje x
    plt.suptitle('Histograma de una Máquina de Galton')  # Establece el título del gráfico
    plt.bar(X, resultados, width=1.00)  # Crea un histograma con las barras
    plt.xlabel('Distribución de Canicas')  # Etiqueta del eje x
    plt.ylabel('Cantidad de Canicas')  # Etiqueta del eje y
    plt.xticks(X, range(len(resultados)))  # Establece las marcas en el eje x
    plt.show()  # Muestra el gráfico en pantalla

niveles_obstaculos = 12  # Número de niveles de obstáculos en la máquina de Galton
cantidad_canicas = 3000  # Cantidad de canicas utilizadas en la simulación

# Realizar la simulación y graficar el histograma
resultados = simular_maquina_galton(cantidad_canicas, niveles_obstaculos)
graficar_histograma(resultados)