class Stack:
    def __init__(self):
        self.items = []
        
    def append(self, item):
        self.items.append(item)
        
    def pop(self):
        
        if self.items:
           return self.items.pop()
       
    def peek(self):
        return self.items[-1]
    


arr = [73,74,75,71,69,72,76,73]


def temp(arr):
    
    output = [0] * len(arr)
    
    stack = Stack()
    print(stack.items)
    
    for i, value in enumerate(arr):
        
        while stack.items and value > stack.items[-1][1]:
            stackIndex, stackValue = stack.pop()
            output[stackIndex] = (i - stackIndex)
           
        stack.append([i, value])
           


    
    
    return output
    
    

print(temp(arr))