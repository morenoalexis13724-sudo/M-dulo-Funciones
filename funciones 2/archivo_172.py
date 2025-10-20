def eliminar_caracteres_ESPECIALES_ELKIN_ALEXIS_MORENO_ROJAS():
    texto = "Python! @es #divertido$"
    limpio = "".join(c for c in texto if c.isalnum() or c.isspace())
    print("Texto limpio:", limpio)

eliminar_caracteres_ESPECIALES_ELKIN_ALEXIS_MORENO_ROJAS()

