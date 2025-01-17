from chapter2.array_queue import ArrayQueue 

class CircularDeque(ArrayQueue):
    def __init__(self, capacity = 10): # 생성자는 상속되지 않으므로 다시 구현현
        super().__init__(capacity) #super() 자식 클래스에서 부모 클래스를 부르는 함수
    
    def addRear(self,item): # 큐에서 함수 이름은 다르지만 기능 동일
        self.enequeue(item)

    def deleteFront(self):
        return self.dequeue()
    
    def getFront(self):
        return self.peek()
    
    # 큐 말고 덱에서만 구현 함수
    def addFront(self,item):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front - 1) % self.capacity
        else:
            pass

    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear]
            self.rear = (self.rear - 1) % self.capacity
            return item
        else:
            pass

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else:    
            pass
    # isFull(), isEmpty(), size(), display() 는 동일하게 사용가능


dq = CircularDeque()

for i in range(9):
    if i%2==0:
        dq.addRear(i)
    else:
        dq.addFront(i)

dq.display("Odd insert Front, Even insert Rear")

for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()

dq.display("Delete front two times, Delete rear third times")

for i in range(9,14):
    dq.addFront(i)

dq.display("Insert front 9 to 13")

