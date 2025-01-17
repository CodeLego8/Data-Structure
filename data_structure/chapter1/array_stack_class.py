class ArrayStackC:

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
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
            pass    


    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
            return self.array[self.top]
        else:
            pass

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            pass
    
    def size(self):
        return self.top + 1
    

s = ArrayStack(100)
msg = input("Input message: ")
for e in msg:
    s.push(e)

# print(s.top)

while not s.isEmpty():
    print(s.pop(), end ='')

# while not s.isEmpty():
#     print(s.peek(), end = '')    무한루프 오류류



# for i in range(len(s.array)):    오류 발생 수정필료,  pop() 쓰지 않고 array 요소 전부 출력력
#     i = 0
#     print(s.peek(s.top - i))
#     i += 1  

# def checkBrackets(statement):      # 괄호 짝 검사 함수

#     stack = ArrayStack(100)

#     for ch in statement:
#         if ch in ('{', '[','(' ):
#             stack.push(ch)
#         elif ch in ('}',']',')'):
#             if stack.isEmpty():
#                 return False
#             else:
#                 left = stack.pop()
#                 if (ch == "}" and left !="{") or \
#                 (ch == "]"and left !="[") or \
#                 (ch == ")" and left !="("):
#                     return False
#     return stack.isEmpty()
   
                    
                


