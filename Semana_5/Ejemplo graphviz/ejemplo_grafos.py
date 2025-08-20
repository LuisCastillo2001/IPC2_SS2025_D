import os

# Clase para cada nodo de alumno
class AlumnoNodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

# Lista doblemente enlazada
class ListaAlumnos:
    def __init__(self):
        self.head = None

    # Agregar nodo al final
    def agregar(self, nombre, apellido, carnet):
        nuevo = AlumnoNodo(nombre, apellido, carnet)
        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual
        print(f"Alumno {nombre} {apellido} agregado.")

    # Buscar nodo por carnet
    def buscar(self, carnet):
        actual = self.head
        while actual:
            if actual.carnet == carnet:
                print(f"Alumno encontrado: {actual.nombre} {actual.apellido} ({actual.carnet})")
                return actual
            actual = actual.siguiente
        print("Alumno no encontrado.")
        return None

    # Eliminar nodo por carnet
    def eliminar(self, carnet):
        if self.head is None:
            print("La lista está vacía, no se puede eliminar.")
            return

        actual = self.head
        anterior = None

        while actual is not None:
            if actual.carnet == carnet:
                if anterior:  # No es el primer nodo
                    anterior.siguiente = actual.siguiente
                else:  # Es el primer nodo
                    self.head = actual.siguiente
                print(f"Alumno {actual.nombre} {actual.apellido} eliminado.")
                return
            anterior = actual
            actual = actual.siguiente

        print(f"Alumno con carnet '{carnet}' no encontrado.")


    # Graficar lista usando Graphviz
    def graficar(self, archivo="lista_alumnos"):
        dot = "digraph G {\n"
        dot += "rankdir=LR;\n"  # De izquierda a derecha
        dot += "node [shape=record];\n"  # Nodo tipo record (con campos)
        actual = self.head
        while actual:
            dot += f'n{actual.carnet} [label="{{{actual.nombre} {actual.apellido}|{actual.carnet}}}"];\n'
            if actual.siguiente:
                dot += f'n{actual.carnet} -> n{actual.siguiente.carnet} [dir=both];\n'
            actual = actual.siguiente
        dot += "}\n"

        with open(archivo + ".dot", "w") as f:
            f.write(dot)

        # Generar imagen
        os.system(f"dot -Tpng {archivo}.dot -o {archivo}.png")
        print(f"Lista graficada en {archivo}.png")

# Menu interactivo
def menu():
    lista = ListaAlumnos()
    while True:
        print("\n--- MENU LISTA DOBLE ---")
        print("1. Agregar alumno")
        print("2. Buscar alumno por carnet")
        print("3. Eliminar alumno por carnet")
        print("4. Graficar lista")
        print("5. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.agregar(nombre, apellido, carnet)
        elif opcion == "2":
            carnet = input("Carnet a buscar: ")
            lista.buscar(carnet)
        elif opcion == "3":
            carnet = input("Carnet a eliminar: ")
            lista.eliminar(carnet)
        elif opcion == "4":
            lista.graficar()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
