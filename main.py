# Luis Romero

def quitar_salto_linea():  # Quita salto de linea a cada string obtenido del archivo de instancia.
    for i in range(len(lineas_instancia)):
        lineas_instancia[i] = lineas_instancia[i].replace("\n", "")  # Reemplaza el salto de linea por un string vacío.
    return None


def obtener_enteros(lista_strings):  # Transforma una lista con números en de tipo string en una con tipos int.
    lista_enteros = []
    for i in range(len(lista_strings)):
        lista_enteros.append(int(lista_strings[i]))  # Transformación.
    return lista_enteros


def crear_matriz_clientes():  # Crea una matriz que contiene números enteros que representan la cantidad de clientes que
    lista = []                # prefieren la tienda i y j.
    for linea in lineas_instancia[2:]:  # No considera el número de tiendas y largo de las tiendas.
        lista.append(obtener_enteros(linea.split(",")))  # Se entrega como parámetro a obtener_enteros.
    return lista                                         # una lista de strings sin coma.

#tomar la lista del largo de tienda y transformarla en un arreglo 2D que tenga el campo [posicion original, largo tienda]
# por cada tienda. Por ejemplo [[0,4][1,4][2,10][3,1][4,30][5,3]]
#crear solucion random, la profe menciono la funcion shuffle que toma una lista y la ordena de manera random
#crear calculo del esfuerzo (las sumatorias)


# Main
instancia = open("Instancias/S8.txt", "r")  # Abre el archivo que contiene la instancia a resolver
lineas_instancia = instancia.readlines()  # Lista con todas las lineas del archivo
quitar_salto_linea()
num_tiendas = int(lineas_instancia[0])  # Contiene el número de tiendas
largo_tiendas = obtener_enteros(lineas_instancia[1].split(","))  # Contiene el largo de las tiendas como enteros
matriz_clientes = crear_matriz_clientes()  # Matriz que contiene la cantidad de clientes que prefieren cierto par de tiendas
#mostrar por pantalla
print(lineas_instancia)
print(num_tiendas, largo_tiendas)

for i in matriz_clientes:
    print(i)
instancia.close()  # Abre el archivo que contiene la instancia a resolver
