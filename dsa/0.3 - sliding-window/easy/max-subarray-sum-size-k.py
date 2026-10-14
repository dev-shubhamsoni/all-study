"""
Given an array of integers nums and an integer k, find the maximum sum of 
any contiguous subarray of size k.

Constraints:

1 <= nums.length <= 100,000
-10,000 <= nums[i] <= 10,000
1 <= k <= nums.length
Example 1: Input:

nums = [2, 1, 5, 1, 3, 2]
k = 3
Output: 9

"""
# Learn Array Slicing - not related to the problem
# we can do sum offirst elements using [:how many elements]

# nums = [2, 1, 5, 1, 3, 2]
nums = [4,2,1,-9,8,4,3]
k = 3

def maxSubArrayOfSizeK(nums, k):
    
    # this give a space so for tis to not happen we need to use a for loop to sum  
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    
    for i in range(0, len(nums) - k):
        
        curr_sum -= nums[i]
        curr_sum += nums[i + k]
        
        max_sum = max(curr_sum, max_sum)
    
    return max_sum



print(maxSubArrayOfSizeK(nums, k))














