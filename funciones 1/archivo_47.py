def contar_numeros_impares_ELKIN_ALEXIS_MORENO_ROJAS(lista):
    cantidad = sum(1 for num in lista if num % 2 != 0)
    print(f"La lista tiene {cantidad} números impares.")

contar_numeros_impares_ELKIN_ALEXIS_MORENO_ROJAS([1, 2, 3, 4, 5, 6])

