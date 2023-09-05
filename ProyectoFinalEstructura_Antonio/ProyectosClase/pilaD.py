#ANTONIO VAZQUEZ MONTALBAN
#PILAS
class Pila():
    def __init__(self):
        self.items = [] #Constructor que crea una pila vacía

    def push(self, x): #Insdrtar un dato al final de la lista
        self.items.append(x)
    
    def pop(self): #Extrarer el último dato de la pila y arrojarlo 
        return self.items.pop()
    
    def isEmpty(self):
        if self.items:
            return False
        else:
            return True
    
    def isFull(self):
        pass

    def top(self):
        return self.items[-1]
    
    def show(self):
        for i in self.items : 
            print(i, end=" ") 
        print()


        
        
    



