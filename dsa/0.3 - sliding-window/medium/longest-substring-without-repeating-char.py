"""

Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.


Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.


Example 2:

Input: s = "xxxx"

Output: 1

"""

s = "xxxxyxyz"

def longestSubString(s):
 
 
    # charSet = set()
    # res = 0
    
    # l = 0
    
    # for r in range(0, len(s)):
        
    #     while s[r] in charSet:
    #         charSet.remove(s[l])
    #         l += 1

    #     charSet.add(s[r])
    #     t = r - l + 1
    #     res = max(res, r - l + 1)
        
    # return res
    
    res = 0
    
    charMap = {}
    l = 0
    
    for r in range(0, len(s)):
        
        while charMap.get(s[r], 0) >= 1:
            
            charMap[s[l]] = charMap.get(s[l]) - 1
            l += 1
        
        charMap[s[r]] = charMap.get(s[r], 0) + 1
        res = max(res, r - l + 1)
        
    return res
            
    
    
    


print(longestSubString(s))