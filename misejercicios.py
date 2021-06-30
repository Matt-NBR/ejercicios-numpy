import numpy as np

# 42
# Se crea un arreglo que va de 100 elementos que va desde el cero hasta el 99
Arreglo = np.arange(100)
# Se pide al usuario que ingrese un número, este puede ser flotante o entero
Entrada = float(input("Ingrese numero "))
# Se obtiene el valor absoluto de la diferencia de cada elemento del arreglo para obtener el valor mas cercano
index = (np.abs(Arreglo-Entrada)).argmin()
# Se imprimen el valor en la posición indicada por el index, que en este caso por ir en orden seria el mismo valor del index
print(Arreglo[index], Arreglo, index)

# 43
# Se crea una estructura con 3 filas y dos columnas completadas por unos, una columna de posiciones y otra de colores rgb
Z = np.ones(3, [('position', [('x', int, 1),  # en la posición X se aceptara un entero
                              ('y', int, 1)]),  # en la posición Y se aceptara un entero
                ('color',    [('r', int, 1),  # en la posición r se aceptara un entero
                              # en la posición g se aceptara un entero
                              ('g', int, 1),
                              ('b', int, 1)])])  # en la posición b se aceptara un entero
print(Z)


# 46
# Lectura del archivo lectura.txt
# El metodo genfromtxt lee el archivo aun este mismo tenga valores valores nulos luego del delimitador
Lectura = np.genfromtxt("lectura.txt", delimiter=",")
print(Lectura)


# 49
# Se crea un arreglo de dos dimensiones con 10 filas y 10 columnas
Z = np.zeros((10, 10))
# Se remplaza un valor del arreglo Z en la posicion 5 por un valor aletorio del rango hasta el 5
print(np.put(Z, np.arange(10), 5, 'wrap'))


# 51
# Creación de una matriz con numeros randomicos del 0 al 10, la
matriz1 = np.random.randint(0, 10, (3, 3))
# Impresión de la matriz
print(matriz1)
# Ordenamiento de la matriz por valores de columna
print(matriz1[matriz1[:, 1].argsort()])
