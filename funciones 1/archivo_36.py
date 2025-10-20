def es_primo_ELKIN_ALEXIS_MORENO_ROJAS(numero):
    if numero < 2:
        print(f"{numero} no es primo.")
        return
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print(f"{numero} no es primo.")
            return
    print(f"{numero} es primo.")

es_primo_ELKIN_ALEXIS_MORENO_ROJAS(13)

