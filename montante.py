def montante(matriz):

	# Variables
	filas = len(matriz)
	variables = []

	# Funcionamiento   
	print("Matriz Inicial\n" + str(matriz))

	pivAnt = 1.0  # Inicia el pivote anterior como un float
	for pivN in range(filas): # piv es pivote
		for r in range(filas): # r es row
			for c in range(filas+1): # c es col
				if c != pivN and r != pivN:
					matriz[r][c] = (matriz[pivN][pivN] * matriz[r][c] - matriz[r][pivN] * matriz[pivN][c]) / pivAnt #Formula Montante
			if r != pivN:
				matriz[r][pivN] = 0.0
		print("\n" + str(matriz))
		pivAnt = matriz[pivN][pivN]

	print()
	print("Matriz final\n\n" + str(matriz))
	print("FILAS:" + str(filas))
	for i in range(filas):
		nuevaVariable = matriz[i][filas] / matriz[i][i] # Dividir elemento de diagonal principal entre resultado
		variables.append(nuevaVariable) # Agregar a lista de variables

	return variables
