# Luis Romero paralelo 2
# Cristian Montes paralelo 3
import datetime
import random
import math
from tabulate import tabulate


def quitar_salto_linea():  # Quita salto de linea a cada string obtenido del archivo de instancia.
    for i in range(len(lineas_instancia)):
        lineas_instancia[i] = lineas_instancia[i].replace("\n", "")  # Reemplaza el salto de linea por un string vacío.
    return None


def obtener_enteros(lista_strings):  # Transforma una lista con números de tipo string en una con tipos int.
    lista_enteros = []
    for i in range(len(lista_strings)):
        lista_enteros.append(int(lista_strings[i]))  # Transformación.
    return lista_enteros


def crear_matriz_clientes():  # Crea una matriz que contiene números enteros que representan la cantidad de clientes que
    matriz = []               # prefieren la tienda i y j.
    for linea in lineas_instancia[2:]:                    # No considera el número de tiendas y largo de las tiendas.
        matriz.append(obtener_enteros(linea.split(",")))  # Se agrega una lista de números enteros a la matriz.
    return matriz


def agregar_ubicacion_tiendas():  # Asocia un valor a la indexación original de la lista largo_tiendas, para facilitar
    lista = largo_tiendas.copy()  # el calculo de la función objetivo
    for i in range(len(lista)):
        lista[i] = [i, lista[i]]  # [Ubicación lista original, valor]
    return lista


# ----------------------------------------------------------------------------------------------------------------------
# Swap two values randomly in list.URL https://stackoverflow.com/questions/47724017/swap-two-values-randomly-in-list
# Algoritmo basado en la respuesta del usuario juanpa.arrivillaga
def swap(lista):                  # Cambia aleatoriamente dos elementos al interior de una lista
    while True:
        indice1, indice2 = random.sample(range(len(lista)), 2)
        if indice1 != indice2:    # Evita que los indices de la lista elegidos sean iguales
            break
    dato1, dato2 = lista[indice1], lista[indice2]
    lista[indice1] = dato2
    lista[indice2] = dato1
    return lista
# ----------------------------------------------------------------------------------------------------------------------


def calcular_distancia(indice1, indice2, resultado):                   # Calcula la distancia entre dos tiendas
    distancia = resultado[indice1][1] / 2 + resultado[indice2][1] / 2  # largo_tienda/2 + largo_tienda/2
    if (indice2 - indice1) > 1:                                        # Si hay tiendas entre ambas tiendas
        for i in range(indice1 + 1, indice2):
            distancia += resultado[i][1]                    # Agrega el largo de los puestos que hay entre ambos indices
    return distancia


def calcular_funcion_objetivo(lista):
    fun_objetivo = 0
    for i in range(num_tiendas-1):
        for j in range(i+1, num_tiendas):
            distancia = calcular_distancia(i, j, lista)  # Calcula distancia entre las tiendas
            fun_objetivo += distancia * matriz_clientes[lista[i][0]][lista[j][0]]
            # lista =[[posición original, largo tienda],[posición original, largo tienda],...]
            # lista =[[0,20], [1,30], [2,15],...]
            # lista[i][0] = 0 y lista[j][0] = 1
            # Con ambos indices se obtiene la cantidad de clientes que circulan entre ambas tiendas de la matriz_clientes
    return fun_objetivo


def encontrar_mejor_solucion():
    temperatura = T_inicial
    num_iteraciones = 0
    resultados = []
    solucion = len_tiendas_con_ubicacion.copy()
    random.shuffle(solucion)  # Se genera una solución inicial random
    fo_solucion = calcular_funcion_objetivo(solucion)  # Se calcula la función objetivo de la solución actual
    resultados.append([num_iteraciones, round(fo_solucion), round(temperatura, 3)])
    #print("Calculando", end="")

    while temperatura > T_minima:
        num_iteraciones += 1
        '''   print(".", end="")
        if num_iteraciones % 100 == 0 and num_iteraciones >= 100:
            print()
            print(" " * 10, end="") '''
        nuevo_vecino = swap(solucion.copy())
        # Se genera una nueva solución al intercambiar dos elementos de la lista entre si

        fo_solucion = calcular_funcion_objetivo(solucion)
        fo_new_vecino = calcular_funcion_objetivo(nuevo_vecino)
        # -------------------Criterio de metropolis---------------------------
        diferencia = fo_new_vecino - fo_solucion
        if diferencia < 0:
            solucion = nuevo_vecino.copy()
            fo_solucion = fo_new_vecino
        else:
            p = math.exp(-diferencia/temperatura)
            if random.random() < p:
                solucion = nuevo_vecino.copy()
                fo_solucion = fo_new_vecino
        # ---------------------------------------------------------------------

        temperatura = temperatura * alfa  # Se disminuye la temperatura

        resultados.append([num_iteraciones, round(fo_solucion), round(temperatura, 3)])
   # print()
   # print(tabulate(resultados, headers=["Iteración", "Función Objetivo", "Temperatura actual"]))

    return solucion


def mostrar_solucion(lista):
    contador = 0
    for ubicacion, valor in lista:
        contador += 1
        print(valor, " ", end="")
        if contador == 40:
            contador = 0
            print()
            print(" "*24, end="")

'''
Generación solución inicial: Aleatoria
Operador de vecindario: Swap
Criterio de aceptación: Criterio de metropolis
Esquema de enfriamiento: Geométrico 
Criterio de termino: Temperatura mínima
'''

# Main
t_e_inicio = datetime.datetime.now()
# ----------------------------------------------------------------------------------------------------------------------
archivo = "Instancias/QAP_sko56_04_n.txt"
T_inicial = 999
alfa = 0.99
T_minima = 0.0001
# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------Procesamiento de datos en archivo-----------------------------------------------------
instancia = open(archivo, "r")                                   # Abre el archivo que contiene la instancia a resolver
lineas_instancia = instancia.readlines()                         # Lista con todas las lineas del archivo
quitar_salto_linea()
num_tiendas = int(lineas_instancia[0])                           # Contiene el número de tiendas
largo_tiendas = obtener_enteros(lineas_instancia[1].split(","))  # Contiene una lista con el largo de las tiendas como enteros
# largo tiendas = [5, 6, 4] si se usa S3.txt

len_tiendas_con_ubicacion = agregar_ubicacion_tiendas()          # Contiene una matriz con la ubicación inicial de la tienda y su largo
# len_tiendas_con_ubicacion = [[0,5], [1,6], [4,2]] si se usa S3.txt

matriz_clientes = crear_matriz_clientes()                        # Matriz que contiene la cantidad de clientes que prefieren cierto par de tiendas
instancia.close()                                                # Cierra el archivo que contiene la instancia a resolver
# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------Búsqueda de solución optima-----------------------------------------------------
solucion_final = encontrar_mejor_solucion()
#so_minima = solucion_final.copy()
# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------Calculo tiempo de ejecución----------------------------------------------------
# How to get the execution time of code in milliseconds in Python.
# URL: https://www.adamsmith.haus/python/answers/how-to-get-the-execution-time-of-code-in-milliseconds-in-python
# t_e_inicio = datetime.datetime.now()                       # Almacena la hora de inicio de la ejecución
t_e_final = datetime.datetime.now()                          # Almacena la hora de termino de la ejecución
tiempo_ejecucion = (t_e_final - t_e_inicio).total_seconds()  # Almacena el tiempo de ejecución de la búsqueda en seg.
# ----------------------------------------------------------------------------------------------------------------------

print("\nOrden final de tiendas: ", end="")
mostrar_solucion(solucion_final)
print()
print("Funcion objetivo solucion:", calcular_funcion_objetivo(solucion_final))
print("Tiempo de ejecución: ", tiempo_ejecucion)
