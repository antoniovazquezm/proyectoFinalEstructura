class CircularQueue:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
    
    def enqueue(self, item):
        if ((self.rear + 1) % self.capacity == self.front):
            print("Queue is full\n")
        elif (self.front == -1 and self.rear == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
    
    def dequeue(self):
        if (self.front == -1 and self.rear == -1):
            print("Queue is empty\n")
        elif (self.front == self.rear):
            item = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return item
    
    def display(self):
        if(self.front == -1 and self.rear == -1):
            print("Queue is empty\n")
        elif(self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end = " ")
            print()
        else:
            for i in range(self.front, self.capacity):
                print(self.queue[i], end = " ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end = " ")
            print()


# cola = CircularQueue(3)
# cola.enqueue(1)
# cola.enqueue(2)
# cola.enqueue(3)
# cola.display()
# print(cola.dequeue())
# cola.enqueue(4)
# cola.display()
