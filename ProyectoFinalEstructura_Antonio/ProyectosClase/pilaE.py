class PilaE():
    def __init__(self, size):
        self.items = []
        self.size = size
        self.count = 0

    def push(self, x):
        if not self.isFull():
            self.items.append(x)
            self.count += 1

    def pop(self):
        if not self.isEmpty():
            self.count -= 1
            return self.items.pop()
        else:
            return False

    def isFull (self):
        if len(self.items) >= self.size:
            return True  #print("Tu pila está llena!")
        else:
            return False

    def isEmpty(self):
        if self.items:
            return False #print("Tu pila esta llena!")
        else:
            return True

    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return False

    def show(self):
        for i in self.items : 
            print(i, end=",")
        print()

# pila = PilaE(3)
# pila.push(1)
# pila.push(2)
# pila.push(3)
# pila.show()