def dividir_elementos_ELKIN_ALEXIS_MORENO_ROJAS(lista1, lista2):
    resultado = []
    for a, b in zip(lista1, lista2):
        if b != 0:
            resultado.append(a / b)
        else:
            resultado.append("Error: división entre cero")
    print(f"División de listas elemento a elemento: {resultado}")

dividir_elementos_ELKIN_ALEXIS_MORENO_ROJAS([10, 20, 30], [2, 5, 0])

