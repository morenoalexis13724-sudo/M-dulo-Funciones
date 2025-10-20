def restar_elementos_ELKIN_ALEXIS_MORENO_ROJAS(lista1, lista2):
    resultado = [a - b for a, b in zip(lista1, lista2)]
    print(f"Resta de listas elemento a elemento: {resultado}")

restar_elementos_ELKIN_ALEXIS_MORENO_ROJAS([10, 20, 30], [1, 2, 3])

