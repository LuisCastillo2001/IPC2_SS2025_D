# estructuras.py

# Nodo básico
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Implementación de Pila (LIFO)
class Pila:
    def __init__(self):
        self.top = None

    def apilar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.top
        self.top = nuevo_nodo

    def desapilar(self):
        if self.top is None:
            return None
        valor = self.top.dato
        self.top = self.top.siguiente
        return valor

    def esta_vacia(self):
        return self.top is None
    
    def cima(self):
        if self.top is None:
            return None
        return self.top.dato
    
    def tamanio(self):
        contador = 0
        actual = self.top
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    def mostrar(self):
        actual = self.top
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

# Implementación de Cola (FIFO)
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.final is None:
            self.final = nuevo_nodo
            self.frente = self.final
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def desencolar(self):
        if self.frente is None:
            return None
        valor = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return valor

    def esta_vacia(self):
        return self.frente is None
    
    def primero(self):
        if self.frente is None:
            return None
        return self.frente.dato

    def tamanio(self):
        contador = 0
        actual = self.frente
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    def mostrar(self):
        actual = self.frente
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

# Ejemplo de uso de pila y cola
if __name__ == "__main__":
    pila = Pila()
    cola = Cola()
    
    print("----------Pila-----------")
    pila.apilar(10)
    pila.apilar(20)
    pila.apilar(30)
    pila.apilar(40)
    pila.mostrar()  # Muestra: 40 30 20 10
    pila.desapilar()
    pila.mostrar()  # Muestra: 30 20 10


    #Operaciones de colas
    print("----------Cola-----------")
    cola.encolar(100)
    cola.encolar(200)
    cola.encolar(300)
    cola.encolar(400)
    cola.mostrar()  # Muestra: 100 200 300 400
    cola.desencolar()
    cola.mostrar()  # Muestra: 200 300 400

    # Ejemplo de visualización de la pila con graphviz
    try:
        from graphviz import Digraph

        def graficar_pila(pila, nombre_archivo="pila"):
            dot = Digraph(comment="Pila")
            dot.attr(rankdir='TB')  # Vertical: de arriba hacia abajo
            dot.attr('node', shape='box', width='1', height='0.5', style='filled', fillcolor='lightblue')
            
            actual = pila.top
            idx = 0
            nodo_anterior = None

            while actual is not None:
                nombre_nodo = f"n{idx}"
                etiqueta = str(actual.dato)
                if idx == 0:
                    etiqueta += "\n(top)"  # marcar el top
                dot.node(nombre_nodo, etiqueta)
                if nodo_anterior is not None:
                    dot.edge(nodo_anterior, nombre_nodo)  # conectar verticalmente
                nodo_anterior = nombre_nodo
                actual = actual.siguiente
                idx += 1


            dot.render(nombre_archivo, view=True, format="png")

        # Graficar la pila actual
        graficar_pila(pila, "pila_graphviz")
        print("Se ha generado el archivo pila_graphviz.png con la visualización de la pila.")
    except ImportError:
        print("Graphviz no está instalado. Instala con 'pip install graphviz' para ver la visualización.")
