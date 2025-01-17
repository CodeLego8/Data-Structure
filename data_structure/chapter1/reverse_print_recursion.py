def printReverse(msg, len):
    if len > 0:
        print(msg[len - 1], end='')
        printReverse(msg, len-1)
    else:
        return
    
instr = input("입력하세요: ")


# instr = "자료구조"

printReverse(instr, len(instr))

