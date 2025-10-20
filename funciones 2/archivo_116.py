def edades_mayores_25_ELKIN_ALEXIS_MORENO_ROJAS():
    personas = {"Ana": 25, "Luis": 30, "Marta": 22, "Carlos": 28}
    mayores = {nombre: edad for nombre, edad in personas.items() if edad > 25}
    print("Personas con edad mayor a 25:", mayores)

edades_mayores_25_ELKIN_ALEXIS_MORENO_ROJAS()

