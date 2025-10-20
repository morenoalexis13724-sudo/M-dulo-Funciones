def contar_letras_cadena_ELKIN_ALEXIS_MORENO_ROJAS():
    texto = "Python es divertido"
    conteo = {letra: texto.count(letra) for letra in set(texto) if letra.isalpha()}
    print("Conteo de letras:", conteo)

contar_letras_cadena_ELKIN_ALEXIS_MORENO_ROJAS()

