def es_palindromo_ELKIN_ALEXIS_MORENO_ROJAS(cadena):
    if cadena.lower() == cadena.lower()[::-1]:
        print(f"La palabra '{cadena}' es un palíndromo.")
    else:
        print(f"La palabra '{cadena}' no es un palíndromo.")

es_palindromo_ELKIN_ALEXIS_MORENO_ROJAS("Ana")

