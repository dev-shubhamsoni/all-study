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
    stack = [root]
    result = []
    
    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)
        
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return result

print(depthFirst(a))