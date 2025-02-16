from typing import List
from sympy import symbols, lambdify, sympify #type: ignore

parar_bucle_principal = True

print('''
    Funciones disponibles:
      π: pi,
      |x|: abs,
      e (euler): E,
      diff(expresion, variable): Derivar una expresión
''')

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

    while True:
        a = intervalo[0]
        b = intervalo[1]

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

while parar_bucle_principal:
    try:
        biseccion()
    except ValueError as error:
        print('\nError', error, '\n')
