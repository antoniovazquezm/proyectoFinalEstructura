from ProyectosClase.nodo import Nodo

class ListaLigada:
    def __init__(self, size):
        self.cabeza = None
        self.size = size
        # Initialize the linked list with size number of nodes
        for i in range(size):
            nodo = Nodo(None)
            self.insertar_final(nodo)


    def insertar_final(self, nodo):
        # comprobar si la lista ligada está vacía
        if self.cabeza: 
            ultimo_nodo = self.cabeza
            while ultimo_nodo.siguiente != None:
                ultimo_nodo = ultimo_nodo.siguiente
            ultimo_nodo.siguiente = nodo
        else:
            self.cabeza = nodo
        self.size += 1
    
    def insertar_inicio(self, nodo):
        nodo.siguiente = self.cabeza
        self.cabeza = nodo
        self.size += 1
    
    def insertar_posicion(self, nodo, posicion):
        if self.cabeza:
            if posicion == 0:
                self.insertar_inicio(nodo)
            elif posicion == self.size - 1:
                self.insertar_final(nodo)
            elif posicion >= self.size: # o también: posicion > self.size - 1
                print(f"No existe el índice {posicion} en la lista ligada")
            else:
                i = 0
                actual = self.cabeza
                while i < posicion and actual.siguiente != None:
                    actual = actual.siguiente
                    i += 1
                nodo.siguiente = actual.siguiente
                actual.siguiente = nodo
                self.size += 1
        else:
            print("No es posible añadir un nodo a una lista ligada sin datos.")  

    def mostrar(self):
        nodo_temp = self.cabeza
        while nodo_temp != None:
            print(f"{nodo_temp.dato}", end = " -> ")
            nodo_temp = nodo_temp.siguiente
        print("Null")   

    def eliminar_inicio(self):
        if not self.cabeza:
            print("La lista ligada está vacía.")
        else:
            self.cabeza = self.cabeza.siguiente
            self.size -= 1

    def eliminar_final(self):
        if not self.cabeza:
            print("La lista ligada está vacía.")
        elif not self.cabeza.siguiente:
            self.cabeza = None
            self.size -= 1
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente:
                actual = actual.siguiente
            actual.siguiente = None
        self.size -= 1

    def eliminar(self, posicion):
        if not self.cabeza:
            print("La lista ligada está vacía.")
        elif posicion > self.size - 1:
            print(f"El índice {posicion} que desea eliminar es inexistente.")
        elif posicion == 0:
            self.eliminar_inicio()
        elif posicion == self.size:
            self.eliminar_final()
        else: 
            ultimo_nodo = self.cabeza
            for i in range(posicion - 1):
                ultimo_nodo = ultimo_nodo.siguiente
            ultimo_nodo.siguiente = ultimo_nodo.siguiente.siguiente
        self.size -= 1

    def obtener(self, posicion):
        if not self.cabeza:
            print("La lista ligada está vacía.")
        elif posicion >= self.size:
            print(f"El índice {posicion} que desea obtener es inexistente.")
        elif posicion == 0:
            print(f"El valor del índice {posicion} es: {self.cabeza.dato}")
        else:
            ultimo_nodo = self.cabeza
            for i in range(posicion):
                ultimo_nodo = ultimo_nodo.siguiente
            print(f"El valor del índice {posicion} es: {ultimo_nodo.dato}")



    

# ll = ListaLigada()

# nodo = Nodo(3)
# ll.insertar_final(nodo)
# nodo = Nodo(5)
# ll.insertar_final(nodo)
# nodo = Nodo(7)
# ll.insertar_inicio(nodo)
# nodo = Nodo(1)
# ll.insertar_posicion(nodo, 0)

# ll.mostrar()
# ll.obtener(7)
# ll.obtener(3)
# ll.eliminar(3)
# ll.mostrar()
# ll.eliminar_inicio()
# ll.mostrar()
# ll.eliminar_final()
# ll.mostrar()
# ll.obtener(2)