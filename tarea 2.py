def calcular_temperatura_promedio(datos_ciudades):
    """
    Calcula la temperatura promedio por ciudad dado un diccionario con los datos de varias semanas.

    Parámetros:
    datos_ciudades (dict): Un diccionario donde las claves son los nombres de las ciudades y los valores son listas de temperaturas semanales.

    Retorna:
    dict: Un diccionario con el promedio de temperatura por cada ciudad.
    """
    promedios = {}

    for ciudad, temperaturas in datos_ciudades.items():
        # Verificar que haya al menos una temperatura registrada
        if temperaturas:
            promedio = sum(temperaturas) / len(temperaturas)
            promedios[ciudad] = promedio
        else:
            promedios[ciudad] = None  # Si no hay datos, dejarlo como None o 0

    return promedios


# Datos de ejemplo: 3 ciudades del Ecuador con temperaturas durante 4 semanas
datos = {
    'Quito': [18.5, 19.0, 17.5, 18.2],
    'Guayaquil': [28.5, 29.0, 30.5, 29.8],
    'Cuenca': [16.0, 16.5, 15.8, 16.2]
}

# Llamar a la función y obtener el promedio por ciudad
promedios_temperatura = calcular_temperatura_promedio(datos)

# Mostrar los resultados
for ciudad, promedio in promedios_temperatura.items():
    print(f"El promedio de temperatura en {ciudad} es {promedio:.2f}°C.")
