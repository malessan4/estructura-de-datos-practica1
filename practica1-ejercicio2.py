def division_entera(num1, num2):
    resultado = num1 // num2
    return resultado
cuenta1 = division_entera(5,2)
print(cuenta1)
    
"""
Nos da como resultado 2, ya que como estamos trabajando con division entera se descarta
la parte decimal
"""

def multiplicacion(num1, num2):
    resultado = num1 * num2
    return resultado
cuenta2 = multiplicacion(7.2,9.8)
print(cuenta2)
"""
Nos da como resultado 70.56, porque 7.2 * 9.8 es una multiplicacion y da 70.56
"""

def resta(num1, num2):
    resultado = num1 - num2
    return resultado
cuenta3 = resta(7,3.1)
print(cuenta3)
"""
Nos da como resultado 3.9, porque 7 - 3.1 es una resta y da 3.9
"""

def suma(num1, num2):
    resultado = num1 + num2
    return resultado
cuenta4 = suma (10.45,7)
print(cuenta4)
"""
Nos da como resultado 17.45, porque 10.45 + 7 es una suma y da 17.45
"""

def suma_string (num1, num2):
    resultado = num1 + num2
    return resultado
cuenta5 = suma_string("republica", " argentina")
print(cuenta5)
"""
Nos da como resultado "republica argentina", porque es la concatenacion de dos strings
"""

def multi_string (num1, num2):
    resultado = num1 * num2
    return resultado
cuenta6 = multi_string("argentina ", 3)
print(cuenta6)
"""
Nos da como resultado "argentina argentina argentina", porque es la multiplicacion por 3 de un strings
"""
