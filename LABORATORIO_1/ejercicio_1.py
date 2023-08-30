import math

numero = int(input("Ingrese un número: "))

if numero < 2:
    print("No es primo")
else:
    es_primo = True
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("Es primo")
    else:
        print("No es primo")
