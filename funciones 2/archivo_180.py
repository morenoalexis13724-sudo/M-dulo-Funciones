def palabras_mas_4_letras_ELKIN_ALEXIS_MORENO_ROJAS():
    texto = "Python es divertido y muy útil"
    palabras = texto.split()
    contador = sum(1 for p in palabras if len(p) > 4)
    print("Cantidad de palabras con más de 4 letras:", contador)

palabras_mas_4_letras_ELKIN_ALEXIS_MORENO_ROJAS()

