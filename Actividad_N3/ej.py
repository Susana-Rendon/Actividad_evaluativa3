calificaciones = []

# Pedir 5 calificaciones al usuario
for i in range(5):
    calificacion = float(input("Ingrese su calificación: "))  # Usamos 'calificacion' en lugar de sobrescribir 'i'
    calificaciones.append(calificacion)

# Ordenar las calificaciones después de que todas han sido ingresadas
calificaciones_ordenadas = sorted(calificaciones)

# Calcular la mediana (el tercer valor en la lista ordenada)
mediana = calificaciones_ordenadas[2]

# Imprimir resultados
print(f"Las calificaciones ingresadas son: {calificaciones_ordenadas}")
print(f"La mediana de las calificaciones es: {mediana}")