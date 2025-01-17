import random

class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.front = 0
        self.rear = 0
    
    # def isFull2(self): 
    #     return self.rear == (self.front + 1) % self.capacity
     # 오류 발생함, 큐의 포화상태는 가득 찬것이 아닌 하나가 비워진것것
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity 
    
    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False
        
        # return self.front ==  self.rear

    def ringBuffer(self, item):
        self.rear  = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        if self.isEmpty():  # 큐가 비어있는 것이 아닌 꽉 찬 상태
            self.front = (self.front+1) % self.capacity
            


    def enequeue(self, item):
        if not self.isFull():
            self.rear  = (self.rear + 1) % self.capacity 
            self.array[self.rear] = item
        else:
            pass
            
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else: pass

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else: pass


    # def peek2(self):  # 큐는 선입선출 이므로 잘못 만든 함수
    #     if not self.isEmpty():
    #         return self.array[self.rear] % self.capacity
    #     else: pass


    def size(self):
        return(self.rear - self.front + self.capacity) % self.capacity
    
    def display(self, text):
        print(text, end='= [')
        for i in range(self.front + 1, self.front + 1 + self.size()):
            print(self.array[i % self.capacity], end=' ')
        print("]")


    # def display2(self, text):
    #     print(text, end='= [')
    #     for i in range(self.front+1,  abs(self.rear - self.front)):
    #         print(self.array[i % self.capacity], end='')
    #     print("]")


def levelOrder(root):  # 이진 트리 레벨 순회
    queue = ArrayQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)


q = ArrayQueue(10)

q.display("First Entity:")
while not q.isFull():
    q.enequeue(random.randint(0,100))
q.display("After Entity:")

q.display("Delete Order")
while not q.isEmpty():
    q.dequeue()
q.display("After Delete:")

