def promedio_impares_ELKIN_ALEXIS_MORENO_ROJAS(lista):
    impares = [num for num in lista if num % 2 != 0]
    if impares:
        promedio = sum(impares) / len(impares)
        print(f"El promedio de los números impares es: {promedio}")
    else:
        print("No hay números impares en la lista.")

promedio_impares_ELKIN_ALEXIS_MORENO_ROJAS([1, 2, 3, 4, 5, 6])

