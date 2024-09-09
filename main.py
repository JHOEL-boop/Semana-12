# Definimos los datos: ciudades, días de la semana y semanas
ciudades = ['Ciudad1', 'Ciudad2', 'Ciudad3']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 2  # Ejemplo con 2 semanas

# Creamos una matriz 3D de temperaturas (ciudades x días x semanas)
# Cada ciudad tiene una lista de días, y cada día tiene temperaturas por semana.
temperaturas = [
    [  # Ciudad1
        [15, 16],  # Lunes (Semana 1: 15, Semana 2: 16)
        [17, 18],  # Martes
        [19, 20],  # Miércoles
        [21, 22],  # Jueves
        [23, 24],  # Viernes
        [25, 26],  # Sábado
        [27, 28],  # Domingo
    ],
    [  # Ciudad2
        [10, 11],  # Lunes
        [12, 13],  # Martes
        [14, 15],  # Miércoles
        [16, 17],  # Jueves
        [18, 19],  # Viernes
        [20, 21],  # Sábado
        [22, 23],  # Domingo
    ],
    [  # Ciudad3
        [8, 9],  # Lunes
        [10, 11],  # Martes
        [12, 13],  # Miércoles
        [14, 15],  # Jueves
        [16, 17],  # Viernes
        [18, 19],  # Sábado
        [20, 21],  # Domingo
    ]
]

# Calcular el promedio de temperaturas para cada ciudad por cada semana
for i, ciudad in enumerate(ciudades):
    for semana in range(semanas):
        suma_temperaturas = 0
        for dia in range(len(dias_semana)):
            suma_temperaturas += temperaturas[i][dia][semana]
        promedio = suma_temperaturas / len(dias_semana)
        print(f'Promedio de temperatura en {ciudad} en la Semana {semana + 1}: {promedio:.2f}°C')
