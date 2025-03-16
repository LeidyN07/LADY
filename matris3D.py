def calcular_promedio_temperaturas(datos_temperaturas):
    """
    Calcula el promedio de temperaturas por ciudad y semana.
    
    Parámetros:
    datos_temperaturas (list): Lista de temperaturas de cada ciudad por semana.
    
    Retorna:
    dict: Promedio de temperatura por ciudad.
    """
    
    promedios = {}  # Diccionario para almacenar los promedios
    
    for ciudad_idx, ciudad_temperaturas in enumerate(datos_temperaturas):
        ciudad_nombre = f"Ciudad {ciudad_idx + 1}"
        promedio_ciudad = 0
        num_semanas = len(ciudad_temperaturas)
        
        for semana_temperaturas in ciudad_temperaturas:
            promedio_ciudad += sum(semana_temperaturas) / len(semana_temperaturas)
        
        promedio_ciudad /= num_semanas
        promedios[ciudad_nombre] = promedio_ciudad
    
    return promedios


# Ejemplo de datos de temperaturas para 3 ciudades y 4 semanas
temperaturas = [
    [  # Ciudad 1
        [20, 22, 21],  # Semana 1
        [23, 25, 22],  # Semana 2
        [21, 23, 20],  # Semana 3
        [19, 20, 21]   # Semana 4
    ],
    [  # Ciudad 2
        [18, 19, 20],  # Semana 1
        [21, 22, 23],  # Semana 2
        [19, 20, 18],  # Semana 3
        [20, 21, 22]   # Semana 4
    ],
    [  # Ciudad 3
        [15, 16, 14],  # Semana 1
        [17, 18, 16],  # Semana 2
        [14, 15, 16],  # Semana 3
        [16, 17, 15]   # Semana 4
    ]
]

# Llamada a la función
resultados = calcular_promedio_temperaturas(temperaturas)

# Imprimir los resultados
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio:.2f}°C")
