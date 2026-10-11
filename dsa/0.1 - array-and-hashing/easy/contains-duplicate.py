
"""
Given an integer array nums, return true if any value appears more than once in the array, 
otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

"""


# problems faced - Unable to set and get dict items, view python dict

nums = [1, 2, 3, 3]

def hasDuplicate(nums):
    

    map = {}
    
    for i, v in enumerate(nums):
        
        
        if map.get(v) and map.get(v) > 1:
            return True
        
        map[v] = (map.get(v) or 1) + 1
    
    
    
    return False
    

print(hasDuplicate(nums))