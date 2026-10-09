# parent child - b and c are child a is parent and b is parent of d
# root - who doesnt have a aprent - a
# leaf - no child - b & c
# no nodes empty tree - still a bianry tree

#     a
#    / \
#   b   c
#  /
# d

# - A binary tree is a tree where every node most 2 children otherwise it will be just a tree
# - Have exactly one root
# - Exactly 1 path between root and any node
# - 0 nodes - empty tree - binary tree 


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

