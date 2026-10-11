# Push, pop & Peek all 3 are Big O(1)

# Where to use
# 1 - Undo type of functionality, where we have to go back & check.


class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        
        if self.items:
           return self.items.pop()
        
        return None
    
    def peek(self):
        return self.items[-1]
        
        
stack = Stack()
stack.push(20)
stack.push(40)
print(f"peek item is: {stack.peek()}")
print(stack.items)
stack.pop()
print(stack.items)