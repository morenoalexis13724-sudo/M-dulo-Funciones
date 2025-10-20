def filtrar_diccionarios_ELKIN_ALEXIS_MORENO_ROJAS():
    personas = [
        {"nombre": "Ana", "edad": 25},
        {"nombre": "Luis", "edad": 30},
        {"nombre": "Marta", "edad": 22}
    ]
    mayores_25 = [p for p in personas if p["edad"] > 25]
    print("Personas mayores de 25 años:", mayores_25)

filtrar_diccionarios_ELKIN_ALEXIS_MORENO_ROJAS()

