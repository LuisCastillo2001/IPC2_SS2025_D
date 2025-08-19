import os
from graficos import exportar_graphviz_matriz, exportar_graphviz_tabla, generar_imagen_dot


# Carpeta donde está el script actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Nodo para un sensor
class SensorNodo:
    def __init__(self, id_sensor, valor=0):
        self.id_sensor = id_sensor
        self.valor = valor
        self.siguiente = None
        self.anterior = None

# Lista de sensores
class SensorLista:
    def __init__(self):
        self.head = None

    def agregar_sensor(self, id_sensor, valor):
        nuevo = SensorNodo(id_sensor, valor)
        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual

    def mostrar(self):
        actual = self.head
        while actual:
            print(str(actual.valor).ljust(8), end="")
            actual = actual.siguiente

# Nodo para una estación
class EstacionNodo:
    def __init__(self, id_estacion):
        self.id_estacion = id_estacion
        self.sensores = SensorLista()   
        self.siguiente = None
        self.anterior = None

# Lista de estaciones
class EstacionLista:
    def __init__(self):
        self.head = None

    def agregar_estacion(self, id_estacion):
        nueva = EstacionNodo(id_estacion)
        if self.head is None:
            self.head = nueva
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva
            nueva.anterior = actual
        return nueva

    def mostrar(self):
        # Encabezado basado en la primera estación
        if self.head and self.head.sensores.head:
            print("      ", end="")
            actual_sensor = self.head.sensores.head
            while actual_sensor:
                print(f"s{actual_sensor.id_sensor}".ljust(8), end="")
                actual_sensor = actual_sensor.siguiente
            print()

        # Filas con estaciones
        actual_est = self.head
        while actual_est:
            print(f"n{actual_est.id_estacion}".ljust(6), end="")
            actual_est.sensores.mostrar()
            print()
            actual_est = actual_est.siguiente

estaciones = EstacionLista()

# Estación 1
n1 = estaciones.agregar_estacion(1)
n1.sensores.agregar_sensor(1, 200)
n1.sensores.agregar_sensor(2, 300)
n1.sensores.agregar_sensor(3, 0)


# Estación 2
n2 = estaciones.agregar_estacion(2)
n2.sensores.agregar_sensor(1, 0)
n2.sensores.agregar_sensor(2, 0)
n2.sensores.agregar_sensor(3, 6000)

# Estación 3
n3 = estaciones.agregar_estacion(3)
n3.sensores.agregar_sensor(1, 500)
n3.sensores.agregar_sensor(2, 8000)
n3.sensores.agregar_sensor(3, 0)

# Estación 4
n4 = estaciones.agregar_estacion(4)
n4.sensores.agregar_sensor(1, 1500)
n4.sensores.agregar_sensor(2, 0)
n4.sensores.agregar_sensor(3, 1500)

# Estación 5
n5 = estaciones.agregar_estacion(5)
n5.sensores.agregar_sensor(1, 0)
n5.sensores.agregar_sensor(2, 0)
n5.sensores.agregar_sensor(3, 0)

# Estacion 6
n6 = estaciones.agregar_estacion(6)
n6.sensores.agregar_sensor(1, 0)
n6.sensores.agregar_sensor(2, 3000)
n6.sensores.agregar_sensor(3, 0)

#Estacion 7
n7 = estaciones.agregar_estacion(7)
n7.sensores.agregar_sensor(1, 1100)
n7.sensores.agregar_sensor(2, 9500)
n7.sensores.agregar_sensor(3, 0)

# Mostrar la matriz
estaciones.mostrar()

# Preguntar al usuario qué tipo de gráfico quiere
print("\n¿Qué tipo de gráfico desea generar?")
print("1. Tipo nodos (con conexiones)")
print("2. Tipo tabla (colorizada)")
opcion = input("Ingrese su opción (1 o 2): ")

if opcion == "1":
    ruta_dot = os.path.join(BASE_DIR, "matriz_nodos.dot")
    ruta_png = os.path.join(BASE_DIR, "matriz_nodos.png")
    exportar_graphviz_matriz(estaciones, ruta_dot)
    generar_imagen_dot(ruta_dot, ruta_png)
    print(f"Gráfico tipo nodos generado en: {ruta_png}")

elif opcion == "2":
    ruta_dot = os.path.join(BASE_DIR, "matriz_tabla.dot")
    ruta_png = os.path.join(BASE_DIR, "matriz_tabla.png")
    exportar_graphviz_tabla(estaciones, ruta_dot)
    generar_imagen_dot(ruta_dot, ruta_png)
    print(f"Gráfico tipo tabla generado en: {ruta_png}")
