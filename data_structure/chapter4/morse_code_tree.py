class BTNode:
    def __init__(self, e, left=None, right=None):
        self.data = e
        self.left = left
        self.right = right

table = [
    ('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),   ('E', '.'),
    ('F', '..-.'),  ('G', '--.'),   ('H', '....'),  ('I', '..'),    ('J', '.---'),
    ('K', '-.-'),   ('L', '.-..'),  ('M', '--'),    ('N', '-.'),    ('O', '---'),
    ('P', '.--.'),  ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
    ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),  ('Y', '-.--'),
    ('Z', '--..')
]


def encode(ch):           # ord는 파이썬 내장함수로 아스키 값을 반환
    idx = ord(ch)-ord('A')    # index를 A는 0, B는 1, C는 2 이렇게 바꿔줌줌
    return table[idx][1]      

def decodeSimple(morse):
    for tp in table:
        if morse == tp[1]:   # 입력된 모스 부호 morse가 현재 튜플 tp의 두 번째 요소(tp[1])와 같으면 True를 반환합니다.
            return tp[0]
        
def MakeMoresTree():   # 모스코드 디코딩을 위한 결정 트리 만들기기
    root = BTNode(None, None, None)
    for tp in table:
        code = tp[1]
        node = root
        for c in code:
            if c == '.':
                if node.left == None:
                    node.left = BTNode(None, None, None)
                node = node.left   # 노드를 왼쪽으로 이동
            elif c == '-':
                if node.right == None:
                    node.right = BTNode(None, None, None)
                node = node.right  # 노드를 오른쪽으로 이동
        node.data = tp[0]                                          
    return root

def decode(root, code):  #결정트리를 이용한 디코딩딩
    node = root
    for c in code:
        if c == '.':
            node = node.left
        elif c =='-':
            node = node.right
    return node.data

morseCodeTree = MakeMoresTree()
str = input("입력 문장:")
mlist = []
for ch in str:
    code = encode(ch)
    mlist.append(code)

print("Mores Code: ", mlist)
print("De")