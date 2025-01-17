
class Node:
    def __init__(self, element, link=None):  
        self.data = element
        self.link = link

    def append(self, node):
        if node is not None:
            node.link = self.link
            self.link = node

    def popNext(self):
        next = self.link
        if next is not None:
            self.link = next.link
        return next 


class LinkedList:

    classCount = 0
    
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    

    def isFull(self):
        return False  # 연결리스트는 절대 포화상태가 되지 않음
    
    def getNode(self, pos):
        if pos < 0:      # (일관성을 유지하기 쉽도록 Node(0)이 머리 노드를 의미하게 만듦듦),
                                      # 그러므로, -> pos가 0일 수가 없음음
            return None
        ptr = self.head   # 머리 노드를 가리키는 변수(head pointer)
        for i in range(pos):
            if ptr == None:       #  연결리스트 노드가 없는 경우, head가 None인 경우
                return None
            ptr = ptr.link  # 링크타고 다음 노드로 이동 
        return ptr
    
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:         # 해당 노드가 없는 경우 
            return None
        else:
            return node.data
    
    def insert(self, pos, e):
        node = DNode(e, None)
        before = self.getNode(pos-1)    # pos =<인 경우, getNode(-1)은 None 이 return

        if before == None:
            node.link = self.head
            self.head = node
            self.classCount += 1
        else:
            before.append(node)
            self.classCount += 1

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            before = self.head
            if self.head is not None:
                self.head = self.head.link
                self.classCount -= 1
            return before
        else: 
            self.classCount -= 1
            return before.popNext()

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.link
            count += 1
        return count

    def classCountSize(self):
        return self.classCount

    def display(self, msg='LinkedList: '):
        print(msg, end =' ')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='->')
            ptr = ptr.link
        print('None')

    def replace(self, pos, e):
        node = self.getNode(pos)
        if node != None:
            node.data = e    





# s = LinkedList()
# s.display("연결리스트 초기: ")
# s.insert(0,10)
# s.insert(0,20)
# s.insert(1,30)
# s.insert(s.size(),40)
# s.insert(2,50)
# # print(s.display("연결리스트 삽입"))


s = LinkedList()
s.display("연결리스트(초기): ")
s.insert(0,10)
s.insert(0,20)
s.insert(1,30)
s.insert(s.size(),40)
s.insert(2,50)
s.display("연결리스트(삽입 * 5): ")
s.replace(2,90)
s.display("연결리스트(교체 * 1): ")
s.delete(2)
s.delete(3)
s.delete(0)
s.display("연결리스트(삭제 * 3): ")
print(s.size())
print(s.classCountSize())