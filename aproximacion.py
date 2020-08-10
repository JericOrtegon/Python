def run():
    print("""
    Hola, este es un programa que te ayuda a 
    encontrar la raiz cuadrada de cualquier número 
    que tu desees ingresar. 
    Nos gusta saber que nos visitas.
    Buena suerte""")

    objetivo = int(input("Escoge un número: "))
    epsilon = 0.01
    paso = epsilon ** 2
    respuesta = 0.0

    while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta ** 2 - objetivo) >= epsilon:
        print(f"No se encontró la raiz cuadrada  {objetivo}")
    else:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")




if __name__ == "__main__":
    run()