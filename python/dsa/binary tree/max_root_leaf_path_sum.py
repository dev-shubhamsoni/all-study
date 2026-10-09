class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#                 2  
#               /   \
#              5     6
#             /  \     \
#            1    4     9
#
#
#
#
#

def mrtlps(root):
    
    if root == None:
        return float('-inf')
    
    if root.left == None or root.right == None:
        return root.val
    
    leftNode = mrtlps(root.left)
    rightNode = mrtlps(root.right)
    
    return root.val + max(leftNode, rightNode)
    


print(mrtlps(a))