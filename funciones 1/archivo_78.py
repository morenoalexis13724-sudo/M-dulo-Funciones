def contar_vocales_ELKIN_ALEXIS_MORENO_ROJAS():
    palabra = "programacion"
    contador = 0
    for letra in palabra:
        if letra in "aeiou":
            contador += 1
    print("La palabra tiene", contador, "vocales.")

contar_vocales_ELKIN_ALEXIS_MORENO_ROJAS()

