# Importa las funciones del archivo1.py
from montante import montante
import matplotlib.pyplot as plt

def imprimirConjuntos(valores_x, valores_y, valores_gx):
    # Determina la longitud máxima
    max_length = len(valores_gx)

    print("x    y   g(x)")

    for i in range(max_length):
        # Usa '?' si los índices i están fuera del rango de las listas más cortas
        x_value = valores_x[i] if i < len(valores_x) else "?\t"
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

    # Almacenar elementos en matriz
    matriz = [
        [n, x, x2, x3, y],
        [x, x2, x3, x4, xy],
        [x2, x3, x4, x5, x2y],
        [x3, x4, x5, x6, x3y]
    ]

    return matriz

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

def main():
    # Crear arreglos con datos historicos
    valores_x = list(range(1999, 2024))
    valores_y = [
        321, 1759, 3082, 4773, 5996, 7608, 14316, 21201, 28523, 34196,
        39928, 44567, 48717, 54005, 59147, 67095, 73589, 80046, 94691,
        111203, 128511, 146886, 167047, 192106, 221067
    ]

    # Inicializar valores de x para prediccion
    valores_prediccion = list(range(2024, 2034))

    # Lista para almacenar g(x)
    valores_gx = []

    # Lista para almacenar retorno de variables (a0,...,an)
    variables = []

    # Obtener elementos de la matriz principal
    matriz = getElements(valores_x, valores_y)

    # Obtener Variables mediante montante
    variables = montante(matriz)
    print(variables)

    # Obtencion de variables
    a0 = variables[0]
    a1 = variables[1]
    a2 = variables[2]
    a3 = variables[3]

    # Obtener g(x) en base a la ecuacion cubica (Ajuste de valores)
    for i in range(len(valores_x)):
        x = valores_x[i]
        valores_gx.append((a0 + a1*x + a2*(x**2) + a3*(x**3)))

    # Obtener g(x) en base a la ecuacion cubica (Prediccion de valores) 
    for i in range(len(valores_prediccion)):
        x = valores_prediccion[i]
        valores_gx.append((a0 + a1*x + a2*(x**2) + a3*(x**3)))

    # Imprimir los conjuntos
    imprimirConjuntos(valores_x, valores_y, valores_gx)

    # Creacion Linea Azul (Funcion Original)
    plt.plot(valores_x, valores_y)

    # Creacion Linea Naranja (Funcion Ajustada)
    plt.plot(valores_x + valores_prediccion, valores_gx)

    # Mostrar el gráfico
    plt.show()

if __name__ == "__main__":
    main()