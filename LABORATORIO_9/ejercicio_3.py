import random
import string


def generar_contrasena(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiales=True):
    try:
        if longitud <= 0:
            raise ValueError("La longitud debe ser mayor que cero.")

        caracteres = ''
        if incluir_mayusculas:
            caracteres += string.ascii_uppercase
        if incluir_minusculas:
            caracteres += string.ascii_lowercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_especiales:
            caracteres += string.punctuation

        if not caracteres:
            raise ValueError("Debes incluir al menos un tipo de carácter.")

        def generador_caracter(): return random.choice(caracteres)
        contrasena = ''.join(generador_caracter() for _ in range(longitud))
        return contrasena
    except ValueError as error:
        return str(error)


print(generar_contrasena(12, True, True, True, True))
print(generar_contrasena(8, False, True, True, False))
print(generar_contrasena(10, True, False, False, True))
