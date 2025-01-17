s = list()

msg = input("문자열 입력")

for e in msg:
    s.append(e)

while len(s) != 0 :
    result = s.pop()
    print(result, end ='')