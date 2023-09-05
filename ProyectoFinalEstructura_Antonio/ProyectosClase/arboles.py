class Nodos:
    def __init__(self, dato=None):
        self.izq = None
        self.der = None
        self.dato = dato

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertarNodo(self, dato):
        if self.raiz is None:
            self.raiz = Nodos(dato)
        else:
            self._insertar(dato, self.raiz)

    def _insertar(self, dato, nodo):
        if dato < nodo.dato:
            if nodo.izq is None:
                nodo.izq = Nodos(dato)
            else:
                self._insertar(dato, nodo.izq)
        else:
            if nodo.der is None:
                nodo.der = Nodos(dato)
            else:
                self._insertar(dato, nodo.der)

    def anchura(self):
        colaDatos = [self.raiz]
        while colaDatos:
            nodo = colaDatos.pop(0)
            print(f"{nodo.dato}", end = " -> ")
            if nodo.izq:
                colaDatos.append(nodo.izq)
            if nodo.der:
                colaDatos.append(nodo.der)

    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izq)
            print(f"{nodo.dato}", end = " -> ")
            self.inorden(nodo.der)

    def pre_orden(self, nodo):
        if nodo is not None:
            print(f"{nodo.dato}", end = " -> ")
            self.pre_orden(nodo.izq)
            self.pre_orden(nodo.der)

    def pos_orden(self, nodo):
        if nodo is not None:
            self.pos_orden(nodo.izq)
            self.pos_orden(nodo.der)
            print(f"{nodo.dato}", end = " -> ")

# arbol = Arbol()
# arbol.insertarNodo(1)
# arbol.insertarNodo(12)
# arbol.insertarNodo(9)
# arbol.insertarNodo(5)
# arbol.insertarNodo(6)
# arbol.insertarNodo(2)
# arbol.insertarNodo(10)
# print("ANCHURA")
# arbol.anchura()
# print("\n")
# print("INORDEN")
# arbol.inorden(arbol.raiz)
# print("\n")
# print("PREORDEN")
# arbol.pre_orden(arbol.raiz)
# print("\n")
# print("POSORDEN")
# arbol.pos_orden(arbol.raiz)
# print("\n")
