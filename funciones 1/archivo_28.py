def contar_vocales_ELKIN_ALEXIS_MORENO_ROJAS(cadena):
    vocales = 'aeiouAEIOU'
    cantidad = sum(1 for letra in cadena if letra in vocales)
    print(f"La cadena '{cadena}' tiene {cantidad} vocales.")

contar_vocales_ELKIN_ALEXIS_MORENO_ROJAS("Programación")

