def promedio_pares_ELKIN_ALEXIS_MORENO_ROJAS(lista):
    pares = [num for num in lista if num % 2 == 0]
    if pares:
        promedio = sum(pares) / len(pares)
        print(f"El promedio de los números pares es: {promedio}")
    else:
        print("No hay números pares en la lista.")

promedio_pares_ELKIN_ALEXIS_MORENO_ROJAS([1, 2, 3, 4, 5, 6])

