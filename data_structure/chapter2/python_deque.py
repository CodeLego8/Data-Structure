import collections

dq = collections.deque() # 용량 무한대 / 전단 대신 좌단 사용
#dq = collections.deque(maxlen=10) , 이런식으로 용량 제한 가능, 매개변수 maxlen만 가능함함

print("Deq is not empty" if dq else "Daq is empty") # 삼항 연산자
for i in range(9):
    if i%2==0:
        dq.append(i) # 후단 삽입
    else:
        dq.appendleft(i) # 전단삽입
print("Odd insert Front, Even insert Rear", dq)

for i in range(2):
    dq.popleft()
for i in range(3):
    dq.pop()
print("Delete Front 2 times, Delete Rear 3 times", dq)

for i in range(9,14):
    dq.appendleft(i)

print("Insert Front 9 ~13", dq)

print("Deq is not empty" if dq else "Daq is empty")
 