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

target = "e"

def findTargetBfsIterative(root, target):
    if root == None:
        return False
    
    queue = [root]

    
    while len(queue) > 0:
        current = queue.pop(0)
        
        if current.val == target:
            return True
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        
    return False


def findTargetDfsRecursion(root, target):
    
    if root == None:
        return False
    if root.val == target:
        return True   
    return  findTargetDfsRecursion(root.left, target) or findTargetDfsRecursion(root.right, target)


    
    
print(findTargetDfsRecursion(a, target))

