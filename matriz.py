#BUSQUEDA
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def buscar_valor(matriz,valor ):
    for fila in range(3):
        for columna in range(3):
            if matriz[fila][columna] == valor:
                return (fila, columna)
    return None
valor_a_buscar = int(input("Ingrese un número a buscar: "))

resultado = buscar_valor(matriz, valor_a_buscar)

if resultado:
    print(f"Encontrado en la posición: {resultado}")
else:
    print("No encontrado en la matriz")
