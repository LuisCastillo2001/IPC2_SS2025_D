class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class NodoLibro:
    def __init__(self, libro=None, siguiente=None):
        self.libro = libro
        self.siguiente = siguiente

class ListaLibros:
    def __init__(self):
        self.primero = None

    def append(self, nuevo_libro):
        nuevo_nodo = NodoLibro(libro=nuevo_libro)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            aux = self.primero
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo_nodo

    def mostrar_libros(self):
        if self.primero is None:
            print("No hay libros en esta lista.")
            return
        nodo_aux = self.primero
        print("  - Libros:")
        while nodo_aux is not None:
            print(f"    * Título: {nodo_aux.libro.titulo}")
            print(f"      Autor: {nodo_aux.libro.autor}")
            nodo_aux = nodo_aux.siguiente

    def eliminar(self, titulo):
        if self.primero is None:
            print("La lista está vacía, no se puede eliminar.")
            return
        if self.primero.libro.titulo == titulo:
            self.primero = self.primero.siguiente
            print(f"Libro '{titulo}' eliminado.")
            return
        anterior = None
        actual = self.primero
        while actual is not None and actual.libro.titulo != titulo:
            anterior = actual
            actual = actual.siguiente
        if actual is None:
            print(f"Libro '{titulo}' no encontrado.")
        else:
            anterior.siguiente = actual.siguiente
            print(f"Libro '{titulo}' eliminado.")
