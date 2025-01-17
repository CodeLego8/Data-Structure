class DNodde:
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
