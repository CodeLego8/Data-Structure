import random

class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.front = 0
        self.rear = 0
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity 
    
    def isEmpty(self):
        return self.front == self.rear
    
    def enequeue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            print("Queue is full!")
            
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            print("Queue is empty!")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            print("Queue is empty!")
            return None

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    def display(self, text):
        print(text, end=' = [')
        for i in range(self.size()):
            print(self.array[(self.front + 1 + i) % self.capacity], end=' ')
        print("]")

# 테스트
q = ArrayQueue(10)

q.display("First Entity:")

while not q.isFull():
    q.enequeue(random.randint(0, 100))

q.display("After Entity:")

