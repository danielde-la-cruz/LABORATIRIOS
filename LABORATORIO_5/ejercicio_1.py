
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# A
edades_ordenadas = sorted(edades)
edad_minima = edades_ordenadas[0]
edad_maxima = edades_ordenadas[-1]

# B
edades_ordenadas.append(edad_minima)
edades_ordenadas.append(edad_maxima)

# C
n = len(edades_ordenadas)
if n % 2 == 1:
    edad_mediana = edades_ordenadas[n // 2]
else:
    medio1 = edades_ordenadas[n // 2 - 1]
    medio2 = edades_ordenadas[n // 2]
    edad_mediana = (medio1 + medio2) / 2

# D
edad_promedio = sum(edades_ordenadas) / len(edades_ordenadas)

# E
rango_edades = edad_maxima - edad_minima

# F
diferencia_minimo = abs(edad_minima - edad_promedio)
diferencia_maximo = abs(edad_maxima - edad_promedio)

print("Edades ordenadas:", edades_ordenadas)
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)
print("Edad mediana:", edad_mediana)
print("Edad promedio:", edad_promedio)
print("Rango de edades:", rango_edades)
print("Diferencia entre mínimo y promedio:", diferencia_minimo)
print("Diferencia entre máximo y promedio:", diferencia_maximo)
