def suma(a, b):
    print(f"SUMANDO {a} + {b}")
    return a + b

def resta(a, b):
    print(f"RESTANDO {a} - {b}")
    return a - b

def multiplicacion(a, b):
    print(f"MULTIPLICANDO {a} - {b}")
    return a * b

def  division(a, b):
    print(f"DIVIDIENDO {a} / {b}")
    return a / b

num1 = suma(10, 5)
print(num1)

print(resta(5, 10))

num2 = multiplicacion(num1, 5)
print(num2)
print(5 + division(10, 2))
