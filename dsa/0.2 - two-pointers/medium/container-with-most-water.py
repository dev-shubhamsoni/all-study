"""
height = min(leftIndex, rightIndex)
width = rightIndex - leftIndex
area =  width x height

"""
# FInding th elogic is key, which wall to move 
# min max function in python
# for varibale use snake case

heights = [3, 4, 1, 2, 2, 4, 1, 3, 2]

def mostWater(heights):

    leftWall = 0
    rightWall = len(heights) - 1
    maxArea = 0
    
    while leftWall < rightWall:
        

        height = min(heights[leftWall], heights[rightWall])
        width = rightWall - leftWall
        area = width * height
        
        if area > maxArea:
            maxArea = area
            
        if heights[rightWall] > heights[leftWall]:
            leftWall += 1
        else:
            rightWall -= 1
             
    return maxArea



print(mostWater(heights))