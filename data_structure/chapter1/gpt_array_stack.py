class GptArrayStack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]
        else:
            print("Stack is empty!")
            return None  # 빈 스택일 경우 명시적으로 None 반환

    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        else:
            print("Stack is full!")  # 가득 찬 스택 처리

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print("Stack is empty!")  # 빈 스택 경고 메시지
            return None

    def size(self):
        return self.top + 1


# 스택 사용
s = GptArrayStack(100)
msg = input("Input message: ")
for e in msg:
    s.push(e)

# 역순으로 출력
print("Reversed message using peek and pop: ", end='')
while not s.isEmpty():
    print(s.peek(), end='')  # 최상단 값을 확인하여 출력
    s.pop()  # 값을 출력한 뒤 제거
