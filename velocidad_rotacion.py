import math

def velocidad_rotacion(latitud, longitud):

    lat_rad = math.radians(latitud)
    radio_tierra = 6371.0
    periodo_rotacion = 24.0

    velocidad_r = (2 * math.pi * radio_tierra * math.cos(lat_rad)) / periodo_rotacion
    
    return velocidad_r

# Primeras coordenadas
lat1, long1 = 18.60646, -90.73780
velocidad1 = velocidad_rotacion(lat1, long1)
print(f"La velocidad de rotación en las coordenadas ({lat1}, {long1}) es de: {velocidad1} km/h")

# Segundas coordenadas
lat2, long2 = -38.373825292521154, -69.67405073588125
velocidad2 = velocidad_rotacion(lat2, long2)
print(f"La velocidad de rotación en las coordenadas ({lat2}, {long2}) es de: {velocidad2} km/h")