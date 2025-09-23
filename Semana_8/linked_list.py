# linked_list.py
class Node:
    def __init__(self, data, completada=False):
        self.data = data
        self.completada = completada
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def toggle(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                current.completada = not current.completada
                return True
            current = current.next
            count += 1
        return False

    def delete(self, index):
        """
        Elimina el nodo en la posición `index`.
        Retorna True si se eliminó, False si el índice es inválido.
        """
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        prev = None
        current = self.head
        count = 0
        while current and count < index:
            prev = current
            current = current.next
            count += 1
        if current is None:
            return False
        prev.next = current.next
        return True

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
