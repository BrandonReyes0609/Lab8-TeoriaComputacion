import time
import numpy as np
import matplotlib.pyplot as plt

def tiempo_promedio_suma(a, b, N=100000):
    inicio = time.perf_counter()
    for _ in range(N):
        _ = a + b
    fin = time.perf_counter()
    # Calcula el tiempo promedio por operación de suma
    tiempo_promedio = (fin - inicio) / N
    return tiempo_promedio

# Parte A: Repetir el experimento k veces para obtener la distribución de tiempos promedio
print("Parte A")
k = 100  # Número de repeticiones del experimento
resultados = []

for i in range(k):
    tiempo = tiempo_promedio_suma(12345, 67890)
    resultados.append(tiempo)  # Guardar cada tiempo promedio en la lista
    print(f"Iteración {i + 1}/{k}: Tiempo promedio = {tiempo}")

# Cálculo del tiempo promedio total y desviación estándar
tiempo_promedio_total = np.mean(resultados)
desviacion_estandar = np.std(resultados)

print("\nTiempo promedio total:"+str(tiempo_promedio_total)+" segundos")
print("Desviación estándar de los tiempos promedio:"+str(desviacion_estandar)+" segundos")

# Graficar la distribución de tiempos promedio
plt.hist(resultados, bins=10)
plt.xlabel("Tiempo Promedio (s)")
plt.ylabel("Frecuencia")
plt.title("Distribución de Tiempos Promedios para Suma")
plt.show()

# parte B

#------------------------------------------------------------
# Parte B: Probar con diferentes tamaños de números y comparar tiempos
print("\nParte B")
tamaños = [5, 10, 15]  # Tamaños en número de dígitos
resultados_b = []

for tamaño in tamaños:
    # Generar números de tamaño especificado (5, 10, 15 dígitos)
    a = int('9' * tamaño)  # Genera el número 99999... con el número de dígitos deseado
    b = int('1' * tamaño)  # Genera el número 11111... con el número de dígitos deseado
    
    # Calcular el tiempo promedio para la suma
    tiempo_promedio = tiempo_promedio_suma(a, b)
    resultados_b.append(tiempo_promedio)
    
    print("Tamaño: "+str(tamaño)+" dígitos - Tiempo promedio: "+str(tiempo_promedio)+"segundos")

# Visualización de resultados
plt.plot(tamaños, resultados_b, marker='o')
plt.xlabel("Número de Dígitos en a y b")
plt.ylabel("Tiempo Promedio (s)")
plt.title("Tiempo Promedio de Suma según Tamaño de Números")
plt.show()
#--------------------------------------------------------------
# parte C
# Parte C: Comparar tiempos de ejecución entre enteros y floats
print("\nParte C")
# Definir valores de a y b con 10 dígitos
a_int = int('1234567890')  # Entero de 10 dígitos
b_int = int('9876543210')

# Convertir a float
a_float = float(a_int)
b_float = float(b_int)

# Calcular el tiempo promedio para enteros
tiempo_promedio_int = tiempo_promedio_suma(a_int, b_int)
print("Tiempo promedio con enteros:"+str(tiempo_promedio_int)+" segundos")

# Calcular el tiempo promedio para floats
tiempo_promedio_float = tiempo_promedio_suma(a_float, b_float)
print("Tiempo promedio con floats:"+str(tiempo_promedio_float)+" segundos")

# Visualización de los resultados
tipos = ['Entero', 'Float']
tiempos = [tiempo_promedio_int, tiempo_promedio_float]

plt.bar(tipos, tiempos, color=['blue', 'orange'])
plt.xlabel("Tipo de Dato")
plt.ylabel("Tiempo Promedio (s)")
plt.title("Comparación de Tiempos Promedio para Entero y Float")
plt.show()

# parte D
# Parte (d): Comparación de tiempos con diferentes tamaños de números
print("Parte (d) - Comparación por tamaño de número")

# Definimos los números de 5, 10 y 15 dígitos
numeros = {
    "5 dígitos": (12345, 67890),
    "10 dígitos": (1234567890, 9876543210),
    "15 dígitos": (123456789012345, 987654321098765)
}

# Calculamos el tiempo promedio para cada tamaño
resultados_tamaños = {}

for label, (a, b) in numeros.items():
    tiempo_promedio = tiempo_promedio_suma(a, b)
    resultados_tamaños[label] = tiempo_promedio
    print("Tamaño " +str(label)+" - Tiempo promedio = "+str(tiempo_promedio)+" segundos")

# Graficamos los resultados para visualizar la comparación
etiquetas = list(resultados_tamaños.keys())
valores = list(resultados_tamaños.values())

plt.bar(etiquetas, valores, color=['blue', 'green', 'red'])
plt.xlabel("Tamaño del Número")
plt.ylabel("Tiempo Promedio (s)")
plt.title("Comparación de Tiempos Promedios por Tamaño del Número")
plt.show()
