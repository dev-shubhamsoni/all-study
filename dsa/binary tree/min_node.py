class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
a = Node(2)
b = Node(5)
c = Node(6)
d = Node(1)
e = Node(4)
f = Node(9)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def minNode(root):
    
    if root == None:
        return float('inf') 
    
    leftMin = minNode(root.left)
    rightMin = minNode(root.right)
    
    
    return min(root.val, leftMin, rightMin)


print(minNode(a))