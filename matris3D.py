# Definir las temperaturas manualmente para 2 ciudades, 2 semanas y 3 días por semana
temperaturas = [
    [  # Ciudad 1
        [20, 22, 21],  # Semana 1 (Lunes, Martes, Miércoles)
        [23, 25, 22]  # Semana 2
    ],
    [  # Ciudad 2
        [18, 19, 20],  # Semana 1
        [21, 22, 23]  # Semana 2
    ]
]

# Iterar sobre las ciudades
for ciudad in range(len(temperaturas)):
    print(f"\nCiudad {ciudad + 1}:")

    # Iterar sobre las semanas
    for semana in range(len(temperaturas[ciudad])):
        promedio = sum(temperaturas[ciudad][semana]) / len(temperaturas[ciudad][semana])
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
