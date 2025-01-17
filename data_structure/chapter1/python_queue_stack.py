import queue

s = queue.LifoQueue(maxsize=100)

msg = input("Input Str: ")

for e in msg:
    s.put(e)

while not s.empty():
    print(s.get(), end='')