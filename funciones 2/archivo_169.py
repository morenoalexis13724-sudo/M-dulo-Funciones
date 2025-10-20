def contar_digitos_cadena_ELKIN_ALEXIS_MORENO_ROJAS():
    texto = "Python 3.10 tiene 2 versiones"
    cantidad = sum(1 for c in texto if c.isdigit())
    print("Cantidad de dígitos en la cadena:", cantidad)

contar_digitos_cadena_ELKIN_ALEXIS_MORENO_ROJAS()

