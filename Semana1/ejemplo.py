





# Esto es un comentario de una linea
'''
hola 
este es 
un 
comentario 
multilinea
'''

#Variables

string_corto = "Esto es un string corto"

string_largo = '''
Hola esto es
un string
largo.
'''
#print(string_largo)

a = 5 #enteros
b = 3 #enteros

c = 1.0 #flotante
d = 2.0 #flotante

e = "Dobles"
f = 'Simples'

g = True #Booleanos
h = False

#Operaciones

suma = a + b
resta = a - b
multiplicacion = a * b
division = a/b

#print(suma)
#print(resta)
#print(multiplicacion)
#print(f"Suma: {suma} , Resta {resta} ") 

print('Ingrese su nombre: ')
#nombre = input() #Input sirve para obtener datos del usuario

#int(edad)
#str()
#bool()

#edad = int(input("Ingrese su edad"))

# print('Hola', nombre, 'su edad es', edad)


#Condicionales
# IF 
a = 5

#if a == 1:
    #print("A es igual a 1")
#else:
    #print ("A no es igual a 1")
    

#Operadores lógicos
# and or not -- JAVA &&, ||, !

a = 5
b = 2


if a == 1 and b == 5:
    print("Se cumplen las dos condiciones")    
elif a == 2 or b == 4:
    print("Se cumple una de las condiciones")
elif not a == 1:
    print("A no es igual ha 1")
else: 
    print("No se cumple ninguna condicion")
    
# Operadores de comparacion
# ==, !=, <, >, <=, >=

if a > 5:
    print ("A es mayor que 5")

if a < 7:
    print ("A es menor a 7")
    

#Ciclos

#For
# for (int i =0; i < 10; i++)
for i in range(0, 10):
    print(i)   

print("--------------")
for i in range(0, 10, 3):
    print (i)

print("----while----")
#while 
contador = 0
#while contador < 10:
     #print(contador)
     #contador += 1
     

def func_dummy(nombre_alumno):
    print(nombre_alumno)    
    
def suma(num1, num2):
    return num1 + num2

print("dummy")
func_dummy("Daniel")

print(suma(5,10))

lista = ["manzana", "pera", "uva", 1 , 2, True]

for elemento in lista:
    print(elemento)

print(lista[0])


for i in range(0, len(lista)):
    print(lista[i])
    







