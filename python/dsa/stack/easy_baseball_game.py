ops =  ["5","D","+","C"]


def baseball(arr):
    
    stack = []
    sum = 0
    for i in arr:
        
        if i == "+":
            add = stack[-1] + stack[-2]
            stack.append(add)
        elif i == "D":
            a = stack[-1]
            mul = a * 2
            stack.append(mul)
        elif i == "C":
            a = stack.pop()
        else:
            stack.append(int(i))
            
    for i in stack:
        sum += i
        
    return sum
    
    
print(baseball(ops))