# Datos de prueba (3 ciudades, 4 semanas de datos)

datos_temperatura = {
    "Guayaquil": [30, 32, 31, 29, 28, 27, 30, 32, 31, 29, 28, 27, 30, 32, 31, 29, 28, 27, 30, 32, 31, 29, 28, 27, 30, 32,
                 31, 29],
    "Quito": [22, 24, 23, 25, 26, 21, 22, 24, 23, 25, 26, 21, 22, 24, 23, 25, 26, 21, 22, 24, 23, 25, 26, 21, 22, 24,
                 23, 25],
    "Cuenca": [15, 17, 16, 18, 14, 19, 15, 17, 16, 18, 14, 19, 15, 17, 16, 18, 14, 19, 15, 17, 16, 18, 14, 19, 15, 17,
                 16, 18]
}
# Desarrollo del promedio de cada ciudad

def calcular_temperatura_promedio(datos_temperatura):

    promedios = {}

    for ciudad, temperaturas in datos_temperatura.items():
        total_temperaturas = sum(temperaturas)
        cantidad_dias = len(temperaturas)
        promedio = total_temperaturas / cantidad_dias
        promedios[ciudad] = round(promedio, 2)

    return promedios

# Prueba de la función
promedios = calcular_temperatura_promedio(datos_temperatura)
print("Temperatura promedio por ciudad:", promedios)

