def suma(a, b):                         # Al principio de la funcion ponemos el nombre de la función y sus dos variables a y b
    print(f"SUMANDO {a} + {b}")         # Aquí por ejemplo vamos a "imprimir", SUMMANDO a + b que determinaremos más adelante
    return a + b                        # Por último indicamos que la función nos devuelva el resultado de a más b

def resta(a, b):                        # Aquí hacemos una nueva función pero con la diferencia que en vez de sumar vamos a restar
    print(f"RESTANDO {a} - {b}")        # En python, todo lo que va detrás de una # es ignorado, por lo que puedes poner notas dentro del código
    return a - b                        # por lo que puedes poner notas dentro del código

def multiplicacion(a, b):               # Vamos a crear dos funciones más, pero esta vez multiplican y dividen
    print(f"MULTIPLICANDO {a} - {b}")   # Para que una función no de error, tenemos que poner def su nombre, y entre paréntesis
    return a * b                        # las variables entre comas, seguido de dos puntos, todo lo que queremos que haga la
                                        # función tendrá que ir seguido de una tabulación
def  division(a, b):
    print(f"DIVIDIENDO {a} / {b}")
    return a / b

num1 = suma(10, 5)                      # Aquí vamos a llamar a la función suma y asignar lo que nos va ha devolver a la variable num1
print(num1)                             # Aquí vamos a imprimir la variable num1

print(resta(5, 10))                     # Aquí sin embargo, no vamos a asignar lo que nos devuelve la funcion a ninguna variable
                                        # sino que vamos a imprimirlo diractamente
num2 = multiplicacion(num1, 5)          # En este caso vamos a hacer lo mismo que con la suma pero en vez de utilizar dos números
print(num2)                             # Vamos a sumar 5 y el valor de la vaible num1

print(5 + division(10, 2))              # Por último, vamos a imprimir lo que nos de la funcion division con las variables 10 y 2
                                        # sumando 5 242
