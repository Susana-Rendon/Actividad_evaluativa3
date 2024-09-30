import statistics
calificaciones = []

# Pedir 5 calificaciones al usuario
for i in range(5):
    calificacion = float(input("Ingrese su calificación: "))
    calificaciones.append(calificacion)

calificaciones_ordenadas = sorted(calificaciones)

mediana = calificaciones_ordenadas[2]
desviacion_estandar = statistics.stdev(calificaciones_ordenadas)

print(f"Las calificaciones ingresadas son: {calificaciones_ordenadas}")
print(f"La mediana de las calificaciones es: {mediana}")
print(f"La desviacion estandar de las calificaciones es: {desviacion_estandar:.2f}")