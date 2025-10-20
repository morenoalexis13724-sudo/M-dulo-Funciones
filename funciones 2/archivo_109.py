def contar_negativos_ELKIN_ALEXIS_MORENO_ROJAS():
    numeros = [4, -3, 7, -1, -5, 2]
    contador = sum(1 for n in numeros if n < 0)
    print("Hay", contador, "números negativos en la lista.")

contar_negativos_ELKIN_ALEXIS_MORENO_ROJAS()

