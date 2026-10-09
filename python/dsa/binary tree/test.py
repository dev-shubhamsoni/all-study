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


def dfsIteration(root):
    
    if root == None:
        return []
    
    stack = [root]
    output = []
    
    while len(stack) > 0:
        
        
        current = stack.pop()
        output.append(current.val)
        
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return output

print(dfsIteration(a))


def dfsRecursion(root):
    
    if root == None:
        return []
    
    leftValues = dfsRecursion(root.left)
    rightValues = dfsRecursion(root.right)
    
    return [root.val, *leftValues, *rightValues]
    

print(dfsRecursion(a))

def bfsIteration(root):
    
    if root == None:
        return []
    
    queue = [root]
    output = []
    
    while len(queue) > 0:
        
        curr = queue.pop(0)
        output.append(curr.val)
        
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    
    
    
    return output

print(bfsIteration(a))