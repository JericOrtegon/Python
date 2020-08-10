pesosmx = input("¿Cuántos pesos Mexicanos tienes?: ")
pesosmx = float(pesosmx)
valor_dolar = 3150
dolares = pesosmx / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")
