from data_structure.first.array_stack_class import ArrayStackC


class CheckBracketsStack(ArrayStackC):

    def __init__(self, statement):
        self.statement = statement
        self.stack = ArrayStackC(100)

    def checkBracket(self):
        for ch in statement:
            if ch in ('{', '[','(' ):
                self.stack.push(ch)
            elif ch in ('}',']',')'):
                if self.stack.isEmpty():
                    return False
                else:
                    left = self.stack.pop()
                    if (ch == "}" and left !="{") or \
                       (ch == "]"and left !="[") or \
                       (ch == ")" and left !="("):
                        return False
        return self.stack.isEmpty()
   
                    
statement = input("괄호를 포함한 문자열 입력:")                

c = CheckBracketsStack(statement)

result = c.checkBracket()

print(result)


