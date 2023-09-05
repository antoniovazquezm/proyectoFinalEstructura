class ColaE():
    def __init__(self, size):
        self.items = []
        self.size = size
        self.cont = 0

    def enqueue(self, x):
        if not self.is_full():
            self.items.append(x)
            self.cont += 1
        else:
            print("Oh no! Tu cola está llena!")

    def dequeue(self):
        while not self.is_empty():
            self.cont -= 1
            return self.items.pop(0)
        
    def is_empty(self):
        if self.items:
            return False
        else: 
            return True
    
    def is_full(self):
        if self.cont >= self.size:
            return True
        else:
            return False
    
    def top(self):
        return self.items[0]
    
    def last(self):
        return self.items[-1]
    
    def mostrar(self):
        for i in self.items:
            print(i, end = " ")
        print()
    
    def size(self):
        return self.cont
    
# colaE = ColaE(4)
# colaE.enqueue(1)
# colaE.enqueue(2)
# colaE.enqueue(3)
# colaE.enqueue(4)
# colaE.mostrar()
# colaE.dequeue()
# colaE.mostrar()