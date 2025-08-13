from libros import Libro, ListaLibros

class Estanteria:
    def __init__(self, numero, codigo, libros=None):
        self.numero = numero
        self.codigo = codigo
        self.libros = libros 

class NodoEstanteria:
    def __init__(self, estanteria=None, siguiente=None, anterior=None):
        self.estanteria = estanteria
        self.siguiente = siguiente
        self.anterior = anterior

class ListaEstanterias:
    def __init__(self):
        self.primero = None

    def append(self, nueva_estanteria):
        nuevo_nodo = NodoEstanteria(estanteria=nueva_estanteria)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            aux = self.primero
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo_nodo
            nuevo_nodo.anterior = aux

    def mostrar_estanterias(self):
        if self.primero is None:
            print("No hay estanterías en esta lista.")
            return
        actual = self.primero
        print("=== Lista de Estanterías ===")
        while actual is not None:
            print(f"\nEstantería Número: {actual.estanteria.numero}")
            print(f"Código: {actual.estanteria.codigo}")
            print("Libros en esta estantería:")
            actual.estanteria.libros.mostrar_libros()
            print("-" * 30)  # Separador entre estanterías
            actual = actual.siguiente
        print("=== Fin de la Lista de Estanterías ===")
        
    def eliminar(self, numero):
        if self.primero is None:
            print("La lista está vacía, no se puede eliminar.")
            return
        if self.primero.estanteria.numero == numero:
            self.primero = self.primero.siguiente
            if self.primero is not None:
                self.primero.anterior = None
            print(f"Estantería '{numero}' eliminada.")
            return
        actual = self.primero
        while actual is not None and actual.estanteria.numero != numero:
            actual = actual.siguiente
        if actual is None:
            print(f"Estantería '{numero}' no encontrada.")
        else:
            if actual.siguiente is not None:
                actual.siguiente.anterior = actual.anterior
            if actual.anterior is not None:
                actual.anterior.siguiente = actual.siguiente
            print(f"Estantería '{numero}' eliminada.")



