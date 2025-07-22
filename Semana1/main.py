# Funciones:
# Función Suma:
def func_dummy():
    print("hola")

def suma_func(num1, num2):
    return num1 + num2

def resta_func(num1, num2):
    return num1 - num2

def division_func(num1, num2):
    return num1 / num2

def multiplicacion_func(num1, num2):
    return num1 * num2

def menu():
    print('¿Qué operación quieres hacer?')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')
    print('5. Salir')
    opcion = input()
    return opcion


if  __name__ == '__main__':
    print('Hola, estoy en el main')

    # Este es un comentario de 1 línea.

    '''
    Hola
    este
    es
    un
    comentario
    multilínea.
    '''
    
    # Variables:

    string_largo = '''
    soy
    un
    string
    largo
    '''

    print(string_largo)

    a = -1 # entero
    b = 3 # entero

    c = 1.0 # flotante
    d = 2.0 # flotante

    e = "Dobles"
    f = 'simple'

    # Booleans:
    g = True # Boolean
    h = False # Boolean

    # Operaciones
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a/b

    # impresiones:
    print(suma)
    print(resta)
    print(multiplicacion)
    print(division)

    print('Ingrese su nombre: ')
    nombre = input()

    edad = input("Ingrese su edad: ")

    print('Hola ' + nombre + ' su edad es:', int(edad))

    # Condicionales:
    # IF:
    if a == 1:
        print('Si, "a" si posee el valor de 1.')
    else:
        print("No, 'a' no posee el valor de 1.")

    # Operadores lógicos:
    # Python: and, or, not ------------------ Java: &&, ||, !

    if a == 1 and b == 2:
        print("Se cumple con las condiciones")
    elif a == 2 or int(edad)== 23:
        print("Se cumple alguna de las condiciones")
    elif not a == 1:
        print("Se cumple con que 'a' NO es 1")
    else:
        print("Ninguna de las condiciones se cumple")

    # Operadores de comparación:
    # ==, !=, <, >, <=, >=
    # igual que, no es igual, menor qué, mayor qué, menor igual qué, mayor igual qué:

    if int(edad) >= 18:
        print("MAYOR DE EDAD")
    else:
        print("MENOR DE EDAD")
    
    #Ciclos:
    # FOR:
    for i in range(1, 11):
        print(i, "HOLA")

    for i in range(0, 10, 2):
        print(i)

    '''
    for(int i=0; i<10; i+=2){
    
    }

    '''

    #WHILE:
    print("CONTADOR CON WHILE: ")
    contador = 0
    while contador < 10:
        print(contador)
        contador+=1
    
    # FUNCIONES
    print('SUMA', suma_func(1,22))
    print('RESTA', resta_func(7,1))
    print('MULTIPLICACIÓN', multiplicacion_func(4,4))
    print('DIVISIÓN', division_func(6,2))

    func_dummy()

    # Saltos de Línea:
    print()
    print('\n')

    # Listas:
    lista_ejemplo = [1,2,3]
    lista_ejemplo2 = []
    lista_ejemplo2 = [1, "a", True]

    for elemento in lista_ejemplo:
        print(elemento)

    for i in range(0, len(lista_ejemplo)):
        print(lista_ejemplo[i])

    opcion_seleccionada = menu()
    while opcion_seleccionada != '5':
        num1 = int(input('Ingrese el primer número: '))
        num2 = int(input('Ingrese el segundo número: '))

        if opcion_seleccionada == '1':
            print(" La suma es: "+ str(suma_func(num1, num2)))
        elif opcion_seleccionada == '2':
            print(" La resta es: "+ str(resta_func(num1, num2)))
        elif opcion_seleccionada == '3':
            print(" La multiplicación es: "+ str(multiplicacion_func(num1, num2))) 
        elif opcion_seleccionada == '4':
            print(" La división es: "+ str(division_func(num1, num2))) 
        else:
            print("Opción no válida.")

        opcion_seleccionada = menu()
    print("Adiós, gracias por usar la calculadora")
