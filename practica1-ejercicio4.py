def calcular_area_triangulo ():
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    area = (base * altura)/2
    return print(f"El area del triangulo es: {area}")

triangulo1 = calcular_area_triangulo()