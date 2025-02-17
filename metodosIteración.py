from typing import List
from sympy import symbols, lambdify, sympify #type: ignore
from os import system

parar_bucle_principal = True

def obtener_funcion (expresion: str, variables: str | List[str] ):
    '''
    Esta función recibe dos parámetros: expresión, variables.
    
    Parámetros:\n
    \texpresion (str): La expresión.\n
    \tvariables (str | List[str]): Variables.

    Retorna:\n
    \t(x) -> float: Retorna una función que recibe parámetros y retorna un número.

    Ejemplo:\n
    >>> funcion = obtener_funcion('x^2 + 3', 'x')
    >>> funcion(2)
    >>> 7

    >>> funcion = obtener_funcion('x + y', ['x', 'y'])
    >>> funcion(2, 3)
    >>> 5

    '''
    if isinstance(variables, List):
        simbolos = symbols(','.join(variables))
    else:
        simbolos = symbols(variables)
    evaluar_expresion = sympify(expresion)
    funcion = lambdify(simbolos, evaluar_expresion)
    return funcion

def biseccion():
    # Definir las variables para utilizar
    intervalo = [0, 1]
    variable = ''
    funcion = ''
    valores = []

    # x^4 + 3 * (x^3) - 2
    # 10*(E^(t/2)) * cos(2*t)-4
    # Solicitar los datos al usuario
    print('Método de la bisección')
    print('Ejemplo de variables: "a" o "a,b,c" si son mas variables\n')
    variable = input('Ingrese la variable: ')
    expresion = input('Ingrese la función: ')

    funcion = obtener_funcion(expresion, variable)

    # Solicitar los valores del intervalo
    a = float(input('Ingrese el valor del intervalo "a": '))
    b = float(input('Ingrese el valor del intervalo "b": '))
    intervalo = [a, b]

    iteraciones = 0
    while True:
        a = intervalo[0]
        b = intervalo[1]
        iteraciones += 1
        if iteraciones > 1000:
            print('No se encontró la raíz en el número máximo de iteraciones (1,000).')
            return

        # Evaluar la función en los valores de a, b
        resultado_de_a = funcion(a)
        resultado_de_b = funcion(b)

        expresion_punto_medio = '(a + b) / 2'
        resultado_de_punto_medio = obtener_funcion(expresion_punto_medio, ['a', 'b'])(a, b)
        punto_medio_evaluado_en_funcion = funcion(resultado_de_punto_medio)
        valores.append(resultado_de_punto_medio)
        # print('Intervalo: ', intervalo)
        # print('Resultado de a: ', resultado_de_a)
        # print('Resultado de b: ', resultado_de_b)
        # print('Resultado de Xm: ', resultado_de_punto_medio)
        # print('f(a) * f(Xm): ', resultado_de_a * punto_medio_evaluado_en_funcion)
    
        if resultado_de_a * punto_medio_evaluado_en_funcion < 0:
            intervalo[1] = resultado_de_punto_medio
        elif resultado_de_a * punto_medio_evaluado_en_funcion > 0:
            intervalo[0] = resultado_de_punto_medio
        elif resultado_de_a * punto_medio_evaluado_en_funcion == 0:
            print(f'\nf(a) = {resultado_de_a}')
            print(f'f(b) = {resultado_de_b}')
            print('Intervalo: ', intervalo)
            print('El resultado es: ', resultado_de_punto_medio)
            
            print('\n#        punto medio')
            for i in range(len(valores)):
                print(f'Punto medio {i+1}: {valores[i]}')
            return

        if len(valores) > 1:
            valor_anterior = valores[-2]
            expresion_error_porcentual = 'abs((punto_medio - valor_anterior) / punto_medio) * 100'
            
            error_porcentual_funcion = obtener_funcion(expresion_error_porcentual, ['punto_medio', 'valor_anterior'])
            error_porcentual = error_porcentual_funcion(resultado_de_punto_medio, valor_anterior)
            if (error_porcentual == 0):
                print(f'Punto medio actual: {resultado_de_punto_medio} y punto medio anterior: {valor_anterior}')
                print(f'f(a) = {resultado_de_a}')
                print(f'f(b) = {resultado_de_b}')
                print('Intervalo: ', intervalo)
                print('El resultado es: ', resultado_de_punto_medio)
                print('Error porcentual: ', error_porcentual)

                print('\n#        punto medio')
                for i in range(len(valores)):
                    print(f'{i+1}: {valores[i]}')
                return

def newton ():
    """
    Método de Newton que permite al usuario ingresar la función y el punto inicial.
    """
    funcion = ''
    funcion_derivada = ''

    print('Método de Newton')
    print('Ejemplo de variables: "a" o "a,b,c" si son mas variables\n')

    # x^4 + 3*(x^3) - 2

    # Pedir los datos al usuario
    variable = input('Ingrese la variable: ')
    expresion = input("Ingrese la función en términos de x (ejemplo: x**3 - 4*x + 1): ")

    # Obtener funciones
    funcion = obtener_funcion(expresion, variable) 
    funcion_derivada = obtener_funcion(f'diff({expresion}, {variable})', variable)

    # Calcular derivada automáticamente


    # Pedir el valor inicial al usuario
    x0 = float(input("Ingrese el valor inicial x0: "))
    x_n = x0
    # Configuración del método de Newton
    tol = 1e-6
    max_iter = 1000

    # Iteraciones del método de Newton
    for _ in range(max_iter):
        funcion_evaluada = funcion(x_n)
        funcion_derivada_evaluada = funcion_derivada(x_n)

        if abs(funcion_derivada_evaluada) < 1e-10:  # Evita división por cero
            raise ValueError("La derivada es muy pequeña. Intenta otro x0.")

        x_n1 = x_n - funcion_evaluada / funcion_derivada_evaluada # Fórmula de Newton

        if abs(x_n1 - x_n) < tol:  # Criterio de convergencia
            print(f"La raíz encontrada es: {x_n1}")
            return

        x_n = x_n1  # Actualizar x_n

    print("No se encontró la raíz en el número máximo de iteraciones.")

while parar_bucle_principal:
    try:
        print('\nMétodos de iteración')
        print('''
Métodos disponibles:
    biseccion -> 1,
    newton -> 2
        ''')
        metodo = int(input('Ingrese el método que desea utilizar: '))
        system('cls')

        print('''
Funciones disponibles:
    π: pi,
    |x|: abs,
    e (euler): E,
    diff(expresion, variable): Derivar una expresión,
    abs(expresion): Valor absoluto de una expresión
        ''')

        if metodo == 1:
            biseccion()
        elif metodo == 2:
            newton()
        else:
            print('Método no encontrado')
    except ValueError as error:
        print('\nError', error, '\n')
