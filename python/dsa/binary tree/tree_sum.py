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


def treeSum(root):
    
    if root == None:
        return 0
    
    return root.val + treeSum(root.left) + treeSum(root.right);

print(treeSum(a))


def treeSumDfsIterative(root):
    
    if root == None:
        return 0
     
    
    stack = [root]
    sum = 0
    
    while len(stack) > 0:
        
        
        curr = stack.pop()
        sum += curr.val
        
        if curr.right:
            stack.append(curr.right)
        
        if curr.left:
            stack.append(curr.left)
            
    return sum

print(treeSumDfsIterative(a))
        
        
    
    
    
    