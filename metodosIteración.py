from sympy import symbols, lambdify, sympify #type: ignore
from os import system, name as os_name

parar_bucle_principal = True

def obtener_funcion (expresion, variables):
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

def obtener_error_porcentual (valor_actual, valor_anterior):
    '''
    Esta función recibe dos parámetros: valor_actual, valor_anterior.
    
    Parámetros:\n
    \tvalor_actual (float): El valor actual.\n
    \tvalor_anterior (float): El valor anterior.

    Retorna:\n
    \tfloat: Retorna el error porcentual.

    Ejemplo:\n
    >>> error_porcentual(3, 2)
    >>> 33.3

    >>> error_porcentual(10, 5)
    >>> 50.0

    '''
    return obtener_funcion('abs((x - y) / x) * 100', ['x', 'y'])(valor_actual, valor_anterior)

def biseccion():
    # Definir las variables para utilizar
    valores = []

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

    maxima_iteracion = 1000
    for _ in range(maxima_iteracion):
        a = intervalo[0]
        b = intervalo[1]

        # Evaluar la función en los valores de a, b
        resultado_de_a = funcion(a)
        resultado_de_b = funcion(b)

        expresion_punto_medio = '(a + b) / 2'
        resultado_de_punto_medio = obtener_funcion(expresion_punto_medio, ['a', 'b'])(a, b)
        punto_medio_evaluado_en_funcion = funcion(resultado_de_punto_medio)
        valores.append({ "valor": str(resultado_de_punto_medio), "error_porcentual": '' })
    
        if resultado_de_a * punto_medio_evaluado_en_funcion < 0:
            intervalo[1] = resultado_de_punto_medio
        elif resultado_de_a * punto_medio_evaluado_en_funcion > 0:
            intervalo[0] = resultado_de_punto_medio
        elif resultado_de_a * punto_medio_evaluado_en_funcion == 0:
            print('\n\033[;1m#\033[0m', '\033[;1mPunto medio\033[0m'.center(50, ' '), '\033[;1mError Porcentual\033[0m'.center(50, ' '))
            for i in range(len(valores)):
                print(f'{i+1}: {valores[i]["valor"].center(40, " ")} {valores[i]["error_porcentual"].center(40, " ")}')

            print(f'f(a) = {resultado_de_a}')
            print(f'f(b) = {resultado_de_b}')
            print('Intervalo: ', intervalo)
            print(f'\033[32;1mEl resultado es: {resultado_de_punto_medio}\033[0m')
            return
  

        if len(valores) > 1:
            valor_anterior = float(valores[-2]['valor'])
            error_porcentual = obtener_error_porcentual(resultado_de_punto_medio, valor_anterior)
            valores[-1]['error_porcentual'] = str(error_porcentual)

            if (error_porcentual == 0):
                print('\n\033[;1m#\033[0m', '\033[;1mPunto medio\033[0m'.center(50, ' '), '\033[;1mError Porcentual\033[0m'.center(50, ' '))
                for i in range(len(valores)):
                    print(f'{i+1}: {valores[i]["valor"].center(40, " ")} {valores[i]["error_porcentual"].center(40, " ")}')

                print(f'Punto medio actual: {resultado_de_punto_medio} y punto medio anterior: {valor_anterior}')
                print(f'f(a) = {resultado_de_a}')
                print(f'f(b) = {resultado_de_b}')
                print('Intervalo: ', intervalo)
                print(f'\033[32;1mEl resultado es: {resultado_de_punto_medio}\033[0m')
                print('Error porcentual: ', error_porcentual)
                return
    print('No se encontró la raíz en el número máximo de iteraciones.')

def falsa_posicion():
    valores = []

    print('Método de la falsa posición')
    print('Ejemplo de variables: "a" o "a,b,c" si son mas variables\n')

    variable = input('Ingrese la variable: ')
    expresion = input('Ingrese la función: ')
    print('\n')

    funcion = obtener_funcion(expresion, variable)

    a = float(input('Ingrese el valor del intervalo "a": '))
    b = float(input('Ingrese el valor del intervalo "b": '))
    print('\n')

    intervalo = [a, b]

    # Inicializar variables
    maxima_iteracion = 1000

    for i in range(maxima_iteracion):
        a = intervalo[0]
        b = intervalo[1]

        x_i = obtener_funcion('((a * f_b) - (b * f_a)) / (f_b - f_a)', ['a', 'b', 'f_a', 'f_b'])(a, b, funcion(a), funcion(b))
        valores.append({ "valor": str(x_i), "error_porcentual": '' })

        if (len(valores) > 1):
            valor_anterior = float(valores[-2]['valor'])
            error_calculado = obtener_error_porcentual(x_i, valor_anterior)
            valores[-1]['error_porcentual'] = str(error_calculado)


            if error_calculado == 0:
                print('\n\033[;1m#\033[0m', '\033[;1mx\033[0m'.center(50, ' '), '\033[;1mError Porcentual\033[0m'.center(50, ' '))
                for i in range(len(valores)):
                    print(f'{i+1}: {valores[i]["valor"].center(40, " ")} {valores[i]["error_porcentual"].center(40, " ")}')
                print(f'\033[32;1mLa raíz encontrada es: {x_i}\033[0m')
                return
            
        if funcion(a) * funcion(x_i) < 0:
            intervalo[1] = x_i
        elif funcion(a) * funcion(x_i) > 0:
            intervalo[0] = x_i
        else:
            print('\n\033[;1m#\033[0m', '\033[;1mx\033[0m'.center(50, ' '), '\033[;1mError Porcentual\033[0m'.center(50, ' '))
            for i in range(len(valores)):
                print(f'{i+1}: {valores[i]["valor"].center(40, " ")} {valores[i]["error_porcentual"].center(40, " ")}')
            print(f'\033[32;1mLa raíz encontrada es: {x_i}\033[0m')
            return
    print('No se encontró la raíz en el número máximo de iteraciones.')

def newton ():
    """
    Método de Newton que permite al usuario ingresar la función y el punto inicial.
    """

    valores = []

    print('Método de Newton')
    print('Ejemplo de variables: "a" o "a,b,c" si son mas variables\n')

    # Pedir los datos al usuario
    variable = input('Ingrese la variable: ')
    expresion = input("Ingrese la función (ejemplo: x**3 - 4*x + 1): ")

    # Obtener funciones
    funcion = obtener_funcion(expresion, variable) 
    funcion_derivada = obtener_funcion(f'diff({expresion}, {variable})', variable)

    # Pedir el valor inicial al usuario
    x0 = float(input("Ingrese el valor inicial x0: "))
    x_n = x0
    # Configuración del método de Newton
    tol = 0
    max_iter = 1000

    # Iteraciones del método de Newton
    for _ in range(max_iter):
        funcion_evaluada = funcion(x_n)
        funcion_derivada_evaluada = funcion_derivada(x_n)

        if abs(funcion_derivada_evaluada) < 1e-10:  # Evita división por cero
            raise ValueError("La derivada es muy pequeña. Intenta otro x0.")

        x_n1 = x_n - funcion_evaluada / funcion_derivada_evaluada # Fórmula de Newton
        tolerancia = abs(x_n1 - x_n)
        valores.append({ "valor": str(x_n1), "Tolerancia": str(tolerancia) })

        if tolerancia == tol:  # Criterio de convergencia
            print('\n\033[;1m#\033[0m', '\033[;1mValor\033[0m'.center(50, ' '), '\033[;1mTolerancia\033[0m'.center(50, ' '))
            for i in range(len(valores)):
                print(f'{i+1}: {valores[i]["valor"].center(40, " ")} {valores[i]["Tolerancia"].center(40, " ")}')
            print(f'\033[32;1mLa raíz encontrada es: {x_n1}\033[0m')
            return

        x_n = x_n1  # Actualizar x_n

    print("No se encontró la raíz en el número máximo de iteraciones.")

def secante():
    valores = []

    print('Método de la secante')

    variable = input('Ingrese la variable: ')
    expresion = input('Ingrese la función: ')
    print('\n')

    funcion = obtener_funcion(expresion, variable)

    x0 = float(input('Ingrese el valor inicial x0: '))
    x1 = float(input('Ingrese el valor inicial x1: '))
    print('\n')

    valor_inicial = [x0, x1]

    tolerancia = 0
    maxima_iteracion = 1000

    for _ in range(maxima_iteracion):
        x0 = valor_inicial[0]
        x1 = valor_inicial[1]

        funcion_evaluada_x0 = funcion(x0)
        funcion_evaluada_x1 = funcion(x1)

        if funcion_evaluada_x1 - funcion_evaluada_x0 == 0:
            raise ValueError('La función no es válida para el método de la secante.')

        x2 = obtener_funcion('x1 - (fx1 * (x1 - x0) / (fx1 - fx0))', ['x0', 'x1', 'fx0', 'fx1'])(x0, x1, funcion_evaluada_x0, funcion_evaluada_x1)
        valor_inicial = [x1, x2]
        resultado_toleracia = obtener_funcion('abs(x - y)', ['x', 'y'])(x1, x2)
        valores.append({ "valor": str(x2), "tolerancia": str(resultado_toleracia) })

        if resultado_toleracia <= tolerancia:
            print('\n\033[;1m#\033[0m', '\033[;1mx\033[;0m'.center(50, ' '), '\033[;1mTolerancia\033[0m'.center(50, ' '))
            for i in range(len(valores)):
                print(f'{i+1}: {valores[i]["valor"].center(40, " ")} {valores[i]["tolerancia"].center(40, " ")}')
            print(f'\033[32;1mLa raíz encontrada es: {x2}\033[0m')
            return

while parar_bucle_principal:
    try:
        print('\nMétodos de iteración')
        print('''
Métodos disponibles:
    biseccion -> 1,
    newton -> 2
    secante -> 3
    falsa posición -> 4
        ''')
        metodo = int(input('Ingrese el método que desea utilizar: '))
        system('cls' if os_name == 'nt' else 'clear')

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
        elif metodo == 3:
            secante()
        elif metodo == 4:
            falsa_posicion()
        else:
            print('Método no encontrado')
    except ValueError as error:
        print('\nError', error, '\n')
