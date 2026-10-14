"""
Given an input integer array nums (not necessarily sorted), write a function to find all unique triplets 
[nums[i], nums[j], nums[k]] such that i, j, and k are distinct indices, and the sum of nums[i], nums[j], 
and nums[k] equals zero. Ensure that the resulting list does not contain any duplicate triplets.

Input:

nums = [-1,0,1,2,-1,-1]
Output:

[[-1,-1,2],[-1,0,1]]
Explanation: Both nums[0], nums[1], nums[2] and nums[1], nums[2], nums[4] both include [-1, 0, 1] and 
sum to 0. nums[0], nums[3], nums[4] ([-1,-1,2]) also sum to 0.

Since we are looking for unique triplets, we can ignore the duplicate [-1, 0, 1] triplet and return
[[-1, -1, 2], [-1, 0, 1]].

The order of the triplets and the order of the elements within the triplets do not matter.

"""


# python .sort method sorts array and returns none, so sort it and dont put in a variable
# always use total istead of sum for variable as sum is python buildit function as well
# Sum Condtion - < 0 and > 0
# how to remove duplicates logic

nums = [-1,0,1,2,-1,-4]


def threeSum(nums):
    

    nums.sort()
    outputArr = []
    
    
    for i, val in enumerate(nums):
        
        j = i + 1
        k = len(nums) - 1
        
        while j < k:
            
            sum = nums[i] + nums[j] + nums[k]
            
            if sum == 0:
                outputArr.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                
                while(j < k and nums[j] == nums[j - 1]):
                    j += 1
                    
                while(j < k and nums[k] and nums[k] == nums[k + 1]):
                    k -= 1
                
                continue
            
            
            if nums[i] < sum:
                j += 1
            
            if nums[i] > sum:
                k -= 1
                

    
    return outputArr



print(threeSum(nums))
