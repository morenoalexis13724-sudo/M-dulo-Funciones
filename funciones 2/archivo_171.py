def contar_vocales_cadena_ELKIN_ALEXIS_MORENO_ROJAS():
    texto = "Python es divertido"
    vocales = "aeiouAEIOU"
    cantidad = sum(1 for c in texto if c in vocales)
    print("Cantidad de vocales:", cantidad)

contar_vocales_cadena_ELKIN_ALEXIS_MORENO_ROJAS()

