class FixedSizeList:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size  # 고정 크기 초기화
    
    def set(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            pass  # 크기 초과 시 예외 발생
    
    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            pass
    
    def __str__(self):     #__str__( )는 객체를 문자열로 바꿀 때 필요요
        return str(self.data)


# fixed_list = FixedSizeList(10)

# fixed_list.set(0, "A") 
# fixed_list.set(1, "B")
# print(fixed_list)  
# print(FixedSizeList(10))  



flexible_list = [None]*10

for i in range(8):
    flexible_list.append(10)

print(flexible_list)
t = flexible_list.pop()
print(t)
print(flexible_list)


flexible_list.reverse()
print(flexible_list)


print(flexible_list.count(None)) # 특정 요소의 개수를 찾아 반환
print(flexible_list)


