def ordenar_fila(matriz, fila):
    matriz[fila].sort()  # Ordena la fila en orden ascendente

# Matriz 3x3 con valores numéricos
matriz = [
    [9, 2, 7],
    [4, 8, 3],
    [6, 1, 5]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

fila_a_ordenar = 1  # Especifica qué fila ordenar (segunda fila, índice 1)
ordenar_fila(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
