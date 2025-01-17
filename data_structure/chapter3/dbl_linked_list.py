class DNode:
    def __init__(self, e, prev=None, next=None):
        self.data = e
        self.next = next
        self.prev = prev
    
    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None:
                node.next.prev = node
            self.next = node

    def popNext(self):
        node = self.next
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev = self
        return node


class DblLinkedList(DNode):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    

    def isFull(self):
        return False 
    
    def getNode(self, pos):
        if pos < 0:    
            return None
        ptr = self.head  
        for i in range(pos):
            if ptr == None:      
                return None
            ptr = ptr.next 
        return ptr
    
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:        
            return None
        else:
            return node.data

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.next
            count += 1
        return count

    # def classCountSize(self):
    #     return self.classCount

    def display(self, msg='DblLinkedList: '):
        print(msg, end =' ')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='<=>')
            ptr = ptr.next
        print('None')

    def insert(self, pos, e):
        node = DNode(e)
        before = self.getNode(pos-1)  
        if before == None:
            node.next = self.head
            if node.next is not None: # 꼬리노드가 아니면
                node.next.prev = node
            self.head = node  #  포인터가 다시 머리노드를 가리키게 함함
        else:
            before.append(node)
           
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            before = self.head
            if self.head is not None:
                self.head = self.head.next
            if self.head is not None:      # 만약 리스트에 노드가 하나만 있거나,  self.head.next == None인 경우
                self.head.prev = None       #   self.head가 self.head.next로 설정되면 self.head == None 된다다
            return before                              #  이때, slef.jead.prev = None을 실행하면 self.head가 이미 None이므로,
                              # 파이썬은 None 객체에 prev 속성이 없다는 것을 인지하고, AttributeError를 발생생
        else: 
            return before.popNext()
        
    def replace(self, pos, e):
        node = self.getNode(pos)
        if node != None:
            node.data = e                           

s = DblLinkedList()
s.display("이중연결리스트(초기): ")
s.insert(0,10)
s.insert(0,20)
s.insert(1,30)
s.insert(s.size(),40)
s.insert(2,50)
s.display("이중연결리스트(삽입 * 5): ")
s.replace(2,90)
s.display("이중연결리스트(교체 * 1): ")
s.delete(2)
s.delete(3)
s.delete(0)
s.display("이중연결리스트(삭제 * 3): ")
