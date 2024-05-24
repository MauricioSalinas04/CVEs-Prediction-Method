# Importa las funciones del archivo1.py
import math
from montante import montante
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

def imprimirConjuntos(valores_x, valores_y, valores_gx):
    # Determina la longitud máxima
    max_length = len(valores_gx)

    print("x    y   g(x)")

    for i in range(max_length):
        # Usa '?' si los índices i están fuera del rango de las listas más cortas
        x_value = valores_x[i] if i < len(valores_x) else (str(valores_x[i]+i) + "?\t")
        y_value = valores_y[i] if i < len(valores_y) else "?\t"
        g_value = valores_gx[i]
        print(f"[{x_value}, {y_value}, {g_value}]")


def getElements(valores_x,  valores_y):

    # Crear variables
    x = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0
    x6 = 0
    y = 0
    xy = 0
    x2y = 0
    x3y = 0

    senx = 0
    cosx = 0
    tgx = 0
    lnx = 0
    senx2 = 0
    cosx2 = 0
    tgx2 = 0
    lnx2 = 0

    # Obtener cada elemento mediante sumatoria
    for i in range(len(valores_x)):
        n = len(valores_x)
        x += valores_x[i] 
        x2 += (valores_x[i]) ** 2
        x3 += (valores_x[i]) ** 3
        x4 += (valores_x[i]) ** 4
        x5 += (valores_x[i]) ** 5
        x6 += (valores_x[i]) ** 6
        y += (valores_y[i])
        xy += (valores_x[i]) * (valores_y[i])
        x2y += ((valores_x[i]) ** 2) * (valores_y[i])
        x3y += ((valores_x[i]) ** 3) * (valores_y[i])

        senx += math.sin(valores_x[i])
        cosx += math.cos(valores_x[i])
        tgx += math.tan(valores_x[i])
        lnx += math.log(valores_x[i])

        senx2 += math.sin(valores_x[i]) ** 2
        cosx2 += math.cos(valores_x[i]) ** 2
        tgx2 += math.tan(valores_x[i]) ** 2
        lnx2 += math.log(valores_x[i]) ** 2

    # Almacenar elementos en matriz
    matrizLineal = [
        [n, x, y],
        [x, x2, xy]
    ]
    matrizCuadratica = [
        [n, x, x2, y],
        [x, x2, x3, xy],
        [x2, x3, x4, x2y]
    ]
    matrizCubica = [
        [n, x, x2, x3, y],
        [x, x2, x3, x4, xy],
        [x2, x3, x4, x5, x2y],
        [x3, x4, x5, x6, x3y]
    ]

    matrizLinealSen = [
        [n, x, senx, y],
        [x, x2, x*senx, xy],
        [senx, x*senx, senx2, y*senx]
    ]
    matrizLinealCos = [
        [n, x, cosx, y],
        [x, x2, x*cosx, xy],
        [cosx, x*cosx, cosx2, y*cosx]
    ]
    matrizLinealTg = [
        [n, x, tgx, y],
        [x, x2, x*tgx, xy],
        [tgx, x*tgx, tgx2, y*tgx]
    ]
    matrizLinealLn = [
        [n, x, lnx, y],
        [x, x2, x*lnx, xy],
        [lnx, x*lnx, lnx2, y*lnx]
    ]

    matrizCuadraticaSen = [
        [n, x, x2, senx, y],
        [x, x2, x3, x*senx, xy],
        [x2, x3, x4, x2*senx, x2y],
        [senx, x*senx, x2*senx, senx2, y*senx]
    ]
    matrizCuadraticaCos = [
        [n, x, x2, cosx, y],
        [x, x2, x3, x*cosx, xy],
        [x2, x3, x4, x2*cosx, x2y],
        [cosx, x*cosx, x2*cosx, cosx2, y*cosx]
    ]
    matrizCuadraticaTg = [
        [n, x, x2, tgx, y],
        [x, x2, x3, x*tgx, xy],
        [x2, x3, x4, x2*tgx, x2y],
        [tgx, x*tgx, x2*tgx, tgx2, y*tgx]
    ]
    matrizCuadraticaLn = [
        [n, x, x2, lnx, y],
        [x, x2, x3, x*lnx, xy],
        [x2, x3, x4, x2*lnx, x2y],
        [lnx, x*lnx, x2*lnx, lnx2, y*lnx]
    ]

    ListaDeMatrices = [matrizLineal, matrizCuadratica, matrizCubica, 
                       matrizLinealSen, matrizLinealCos, matrizLinealTg, matrizLinealLn, 
                       matrizCuadraticaSen, matrizCuadraticaCos, matrizCuadraticaTg, matrizCuadraticaLn]
    
    return ListaDeMatrices

def printMatrix(matriz):
    filas = len(matriz)
    print()
    print()
    print("MATRIZ PRINCIPAL")
    for i in range(filas):
        for j in range(filas+1):
            print(f"[{matriz[i][j]}]", end=" ")
        print()
    print()

def getPredictions(valores_x, valores_y):

    # Obtener elementos de la matriz principal
    matrices = getElements(valores_x, valores_y)
    coeficientes = []
    # Ciclo para llamar a la función y acumular las listas retornadas
    for i in range(11):  
        coeficientes.append(montante(matrices[i])) # Llamar a monante y obtener coeficientes (ademas, los agrega a una lista)
        print("COEFICIENTES"+str(coeficientes[i]))

    # Inicializar listas vacías
    listas_gx = [[],[],[],[],[],[],[],[],[],[],[]]
    # Obtener g(x) en base a cada ecuacion (Ajuste de valores)
    for i in range(len(valores_x)):

        x = valores_x[i]
        
        listas_gx[0].append((coeficientes[0][0] + coeficientes[0][1]*x))
        listas_gx[1].append((coeficientes[1][0] + coeficientes[1][1]*x + coeficientes[1][2]*(x**2)))
        listas_gx[2].append((coeficientes[2][0] + coeficientes[2][1]*x + coeficientes[2][2]*(x**2) + coeficientes[2][3]*(x**3)))

        listas_gx[3].append((coeficientes[3][0] + coeficientes[3][1]*x + coeficientes[3][2]*(math.sin(x))))
        listas_gx[4].append((coeficientes[4][0] + coeficientes[4][1]*x + coeficientes[4][2]*(math.cos(x))))
        listas_gx[5].append((coeficientes[5][0] + coeficientes[5][1]*x + coeficientes[5][2]*(math.tan(x))))
        listas_gx[6].append((coeficientes[6][0] + coeficientes[6][1]*x + coeficientes[6][2]*(math.log(x))))

        listas_gx[7].append((coeficientes[7][0] + coeficientes[7][1]*x + coeficientes[7][2]*(x**2) + coeficientes[7][3]*(math.sin(x))))
        listas_gx[8].append((coeficientes[8][0] + coeficientes[8][1]*x + coeficientes[8][2]*(x**2) + coeficientes[8][3]*(math.cos(x))))
        listas_gx[9].append((coeficientes[9][0] + coeficientes[9][1]*x + coeficientes[9][2]*(x**2) + coeficientes[9][3]*(math.tan(x))))
        listas_gx[10].append((coeficientes[10][0] + coeficientes[10][1]*x + coeficientes[10][2]*(x**2) + coeficientes[10][3]*(math.log(x))))

    return listas_gx, coeficientes


