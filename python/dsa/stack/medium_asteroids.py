asteroids = [2,4,-4,-1]

def collision(asteroids):
    
    stack = []
    for a in asteroids:
        
        while stack and stack[-1] > 0 and a < 0:
            diff = a + stack[-1]
            
            if diff > 0:
                a = 0
            elif diff < 0:
                stack.pop()
            else:
                a = 0
                stack.pop()

            
        if a:
            stack.append(a)
    
    return stack       
        
        
        
        
        
        
    return stack

print(collision(asteroids))