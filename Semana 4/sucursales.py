from estanteria import ListaEstanterias

# lista circular de sucursales de bibliotecas

class Sucursal:
    def __init__(self, nombre, direccion, estanterias=None):
        self.nombre = nombre
        self.direccion = direccion
        self.estanterias = estanterias

class NodoSucursal:
    def __init__(self, sucursal=None, siguiente=None):
        self.sucursal = sucursal
        self.siguiente = siguiente

class ListaSucursales:
    def __init__(self):
        self.primero = None

    def append(self, nueva_sucursal):
        nuevo_nodo = NodoSucursal(sucursal=nueva_sucursal)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            aux = self.primero
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo_nodo

    def mostrar_sucursales(self):
        if self.primero is None:
            print("No hay sucursales en esta lista.")
            return
        actual = self.primero
        while actual is not None:
            if actual.sucursal is None:
                print("Nodo sin sucursal asociada.")
            else:
                print(f"Sucursal: {actual.sucursal.nombre}, Dirección: {actual.sucursal.direccion}")
                print("Estanterías en la sucursal:")
                actual.sucursal.estanterias.mostrar_estanterias()
            actual = actual.siguiente
            if actual == self.primero:
                break

    def eliminar(self, nombre):
        if self.primero is None:
            print("La lista está vacía, no se puede eliminar.")
            return
        if self.primero.sucursal.nombre == nombre:
            self.primero = self.primero.siguiente
            print(f"Sucursal '{nombre}' eliminada.")
            return
        anterior = None
        actual = self.primero
        while actual is not None and actual.sucursal.nombre != nombre:
            anterior = actual
            actual = actual.siguiente
        if actual is None:
            print(f"Sucursal '{nombre}' no encontrada.")
        else:
            anterior.siguiente = actual.siguiente
            print(f"Sucursal '{nombre}' eliminada.")
