menu = """
Bievenido al elevador de potencias,
Aquí podras saber de manera sencilla,
el resultado de cualquier número que quieras elevar
a cualquier potencia que desees, 

Buena suerte
"""
numero = int(input("Por favor ingrese el número que quiere elevar: "))
potencia = int(input("Por favor ingrese el número al que quiere elevar el 2: "))
resultado = numero ** potencia
resultado = str(resultado)
print("El resultado es " + resultado)