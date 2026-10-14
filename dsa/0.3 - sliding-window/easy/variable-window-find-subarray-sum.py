# Logic - Since there are no negatives if subarray sum increases target we move left
# pointer and and it is less than we move right one

# issues - 
# Wrong loop with condition - used a range and itgot finished before whole array
# code issues - substracting the current element istead previous element needed to be substracted

# Another variation is longest length of window target sum
# we just need to track the longest length from the start

nums = [3,1,4,9,2,1,7,5]
target = 10

def subArraySumVariableWindow(nums, target):
    
    
    
    start = 0
    end = 0
    
    current_sum = nums[0]
    
    while end < len(nums) - 1:
    
        
        if current_sum == target:
            return [start, end]
        
        
        if current_sum < target:
            end += 1
            current_sum += nums[end]
        elif current_sum > target:
            start += 1
            current_sum -= nums[start - 1]



print(subArraySumVariableWindow(nums, target))