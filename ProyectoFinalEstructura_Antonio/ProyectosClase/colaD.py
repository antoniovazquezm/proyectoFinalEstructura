#ANOTNIO VAZQUEZ MONTALBAN
#Cola Dinámica
class ColaD():
    def __init__(self):
        self.items= []
    
    #Encolar
    def enqueue(self, x):
        self.items.append(x)

    #Desencolar
    def dequeue(self):
        
        return len(self.items) == 0
        # if self.is_empty():
        #     print("Error: Cola Vacía!")
        #     return None
        # else:
        #     return self.items.pop(0)
    
    def is_empty(self):
        if self.items:
            return False if self.items else True #If ternario
        
    def front(self):
        return self.items[0]
    
    def last(self):
        return self.items[-1]
    
    def show(self): #imprimimos por método porque es dinámica
        for i in self.items:
            print(i, end=",")
        print()

    def size(self):
        return len (self.items)
            
# cola = ColaD()
# cola.enqueue(1)
# cola.enqueue(2)
# cola.enqueue(3)
# print("Tamaño de la cola:", cola.size())  # debería imprimir 3
# cola.show()  # debería imprimir 1,2,3
# print("Primer elemento de la cola:", cola.front())  # debería imprimir 1
# print("Último elemento de la cola:", cola.last())  # debería imprimir 3
# cola.dequeue()
# print("Tamaño de la cola después de desencolar:", cola.size())  # debería imprimir 2
# cola.show()  # debería imprimir 2,3




        # if self.items
        #     return False
        # else:
        #     return True