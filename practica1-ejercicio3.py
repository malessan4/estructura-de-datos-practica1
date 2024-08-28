def calcular_perimetro_triangulo ():
    lado1 = float(input("Ingrese la longitud lado1 del triangulo: "))
    lado2 = float(input("Ingrese la longitud lado2 del triangulo: "))
    lado3 = float(input("Ingrese la longitud lado del triangulo: "))
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        perimetro = lado1+lado2+lado3
        return print(f"El perímetro del triángulo es: {perimetro}.")

    else:
        return "Lados con longitud invalida para formar un triangulo"
    
triangulo1 = calcular_perimetro_triangulo()