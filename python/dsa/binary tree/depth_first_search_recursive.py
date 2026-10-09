class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def depthFirst(root):
    if root == None:
        return []
    
    leftValues = depthFirst(root.left)
    rightValues = depthFirst(root.right)
    
    return [root.val, *leftValues, *rightValues]

print(depthFirst(a))

