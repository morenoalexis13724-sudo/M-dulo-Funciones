def es_palindromo_ELKIN_ALEXIS_MORENO_ROJAS():
    texto = "ana"
    texto_limpio = texto.lower().replace(" ", "")
    if texto_limpio == texto_limpio[::-1]:
        print("La cadena es un palíndromo.")
    else:
        print("La cadena no es un palíndromo.")

es_palindromo_ELKIN_ALEXIS_MORENO_ROJAS()

