"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add 
up to a given target number target and index1 < index2. Note that index1 and index2 
cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]

"""
# - A 1‑indexed array is an array whose first element is accessed with index 1 instead of 0, 
# so an array of n elements is indexed from 1 to n.
# forgot about the method but gotit right later, key - use sum

numbers = [-5,-3,0,2,4,6,8]
target = 5

def twoSum(nums, target):
    
    
    left = 0
    right = len(nums) - 1
    
    while left < len(nums) - 1 and right > 0:
        
        leftVal = nums[left]
        rightVal = nums[right]
        sum = leftVal + rightVal
        
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1


print(twoSum(numbers, target))