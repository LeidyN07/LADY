# Función para ordenar una fila en una matriz
def ordenar_fila(matriz, fila):
    print("Matriz original:")
    for f in matriz:
        print(f)

    # Ordenar la fila específica con la función sorted()
    matriz[fila] = sorted(matriz[fila])

    print("\nMatriz después de ordenar la fila", fila, ":")
    for f in matriz:
        print(f)


# Definir una matriz 3x3 de ejemplo
matriz = [
    [3, 1, 4],
    [9, 2, 5],
    [8, 7, 6]
]

# Ordenar la fila 1 (segunda fila) en orden ascendente
ordenar_fila(matriz, 1)
