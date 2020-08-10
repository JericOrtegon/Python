def run():
    nombre_1 = input("Hola, bienvenido a nuestro programa de comparación de edades, en esta oportunidad vas a ser el primero en ingresa tu nombre: ")
    edad_1 = int(input(nombre_1 + " por favor ingresa tu edad: "))
    nombre_2 = input("Hola, bienvenido a nuestro programa de comparación de edades, en esta oportunidad vas a ser el segundo en ingresa tu nombre: ")
    edad_2 = int(input(nombre_2 + " por favor ingresa tu edad: "))

    if edad_1 > edad_2:
        print(nombre_1 + " eres mayor que " + nombre_2)
    elif edad_1 < edad_2:
        print(nombre_1 + " eres menor que " + nombre_2)
    else:
        print(nombre_1 + " tienes la misma edad que " + nombre_2)    


if __name__ == "__main__":
    run()