def run():
    print("""
    Hola, este es un programa que te ayuda a 
    encontrar la raiz cuadrada de cualquier número 
    que tu desees ingresar. 
    Nos gusta saber que nos visitas.
    Buena suerte""")

    objetivo = int(input("Escoge un número: "))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta ** 2 - objetivo) >= epsilon:
        print(f"bajo {bajo}, alto = {alto}, respuesta = {respuesta}")
        if respuesta ** 2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f"La raiz cuadrada de {objetivo} es {respuesta}")



if __name__ == "__main__":
    run()