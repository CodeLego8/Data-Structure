import queue # 큐 모듈
import random

q = queue.Queue(maxsize=10) # maxsize가 0이면 용량 무한대, 매개변수 maxsize 만 가능능

print("삽입 순서: ", end=' ')
while not q.full():
    v = random.randint(0,100)
    q.put(v)
    print(v, end=' ', )

print() # 줄 띄어쓰기

print("삭제 순서:", end = ' ')
while not q.empty() :
    print(q.get(), end =' ')

