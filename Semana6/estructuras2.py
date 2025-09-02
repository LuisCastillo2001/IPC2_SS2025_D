class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Implementación de una pila
class Pila:
    def __init__(self):
        self.top = None #cima inicio
    
    def apilar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.top
        self.top = nuevo_nodo
        print()
    
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
            print(actual.dato, end= " ")
            actual = actual.siguiente
        print()

# Fifo
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
        #20 -> 30
        
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return valor
        #frente = 30
    
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
            print(actual.dato, end = " ")
            actual = actual.siguiente
        print()
    
    
        

                

#Crear una pila
stack = Pila()
print("------------Pila-------------")
#Lifo
stack.apilar(10)
stack.apilar(20)
stack.apilar(30)
stack.apilar(40)
stack.mostrar()
#stack.desapilar()
stack.mostrar()


#Implementación de una cola

print("------------Cola-------------")
queue = Cola()

#Fifo
queue.encolar(10)
queue.encolar(20)
queue.encolar(30)
queue.encolar(40)
queue.mostrar()
queue.desencolar()
queue.mostrar()

try:
    from graphviz import Digraph
    
    def graficar_pila(pila, nombre_archivo):
        dot = Digraph(comment="Pila")
        dot.attr(rankdir='TB')
        dot.attr('node', shape='box', width='1', height = '0.5', style='filled', fillcolor='lightblue')
        
        actual = stack.top
        idx = 0
        nodo_anterior = None
        
        while actual is not None:
            nombre_nodo = f"n{idx}"
            etiqueta = str(actual.dato)
            if idx == 0:
                etiqueta += "\n(top)"
            dot.node(nombre_nodo, etiqueta)
            if nodo_anterior is not None:
                dot.edge(nodo_anterior, nombre_nodo)
            nodo_anterior = nombre_nodo
            actual = actual.siguiente
            idx += 1
        
        dot.render(nombre_archivo, view=False, format = "svg")
        
    graficar_pila(stack, "pila,graphviz")
    print("Se ha guardado el grafo de la pila")
except ImportError:
    print("Hubo un error al generar el grafo")            
        