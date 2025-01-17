import queue

class BTNode:
    def __init__(self, e, left=None, right=None):
        self.data = e
        self.left = left
        self.right = right
    
def preorder(n):         # 전위 순회 VLR
    if n is not None:
        print(n.data, end = ' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n):         # 중위 순회 LVR
    if n is not None:
        inorder(n.left)
        print(n.data, end =' ')
        inorder(n.right)
    
def postorder(n):       # 후위 순회  LRV
    if n is not None:        
        postorder(n.left)
        postorder(n.right)
        print(n.data, end = ' ')

def levelorder(root):       
    q = queue.Queue(maxsize = 0)
    q.put(root)
    while not q.empty():
        n = q.get()
        if n is not None:
            print(n.data, end=' ')
            q.put(n.left)
            q.put(n.right)

def countNode(n):
    if n is None:
        return 0
    else:
        return countNode(n.left) + countNode(n.right) + 1

def calcHeight(n):
    if n is None:
        return 0
    hLeft = calcHeight(n.left)
    hRight = calcHeight(n.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1
    

d = BTNode('D', None, None)
e = BTNode('E', None, None)
b = BTNode('B', d , e)
f = BTNode('F', None, None)
c = BTNode('C', f , None)
root = BTNode('A', b , c)

print('\n In-Order :', end=' '); inorder(root)
print('\n Pre-Order :', end=' '); preorder(root)
print('\n Post-Order :', end=' '); postorder(root)
print('\n Level-Order :', end=' '); levelorder(root)

print("\n Count of Node:", countNode(root))
print("Height of Tree", calcHeight(root))