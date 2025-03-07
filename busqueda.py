matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor = int(input("Ingrese un número a buscar: "))

for fila in range(3):
    for columna in range(3):
        if matriz[fila][columna] == valor:
            print(f"Encontrado en la posición: ({fila}, {columna})")
            exit()

print("No encontrado en la matriz")
