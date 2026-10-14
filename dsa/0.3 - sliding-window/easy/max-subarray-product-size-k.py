

# nums = [2, 1, 5, 1, 3, 2]
nums = [ 1,4 ,1 ,6 ,-3 ,3 ,-5 ,2 ,26]
k = 4

def maxSubArrayProductOfSizeK(nums, k):
    
    current_product = 1
    
    for i in range(0, k):
        current_product *= nums[i]
    
    max_product = current_product
        

    for i in range(0, len(nums) - k):
        
        current_product /= nums[i]
        current_product *= nums[i + k]
        max_product = max(current_product, max_product)
        
    return int(max_product)


print(maxSubArrayProductOfSizeK(nums, k))














