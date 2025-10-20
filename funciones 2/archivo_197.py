def palabras_empiezan_a_ELKIN_ALEXIS_MORENO_ROJAS():
    palabras = ["ana", "luna", "arbol", "manzana", "ave"]
    contador = sum(1 for p in palabras if p.lower().startswith("a"))
    print("Cantidad de palabras que empiezan con 'a':", contador)

palabras_empiezan_a_ELKIN_ALEXIS_MORENO_ROJAS()

