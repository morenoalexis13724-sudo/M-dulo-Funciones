def contar_menor_30_ELKIN_ALEXIS_MORENO_ROJAS():
    personas = [
        {"nombre": "Ana", "edad": 25},
        {"nombre": "Luis", "edad": 30},
        {"nombre": "Marta", "edad": 22}
    ]
    contador = sum(1 for p in personas if p["edad"] < 30)
    print("Cantidad de personas con edad menor a 30:", contador)

contar_menor_30_ELKIN_ALEXIS_MORENO_ROJAS()

