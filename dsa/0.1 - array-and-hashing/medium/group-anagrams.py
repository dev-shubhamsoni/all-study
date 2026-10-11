"""
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]

"""

# ord function
# defaultdict
# list as key is not acceptable use tuple
# if we do freq[key] = val this will replace the value use .append to add to existing value

strs = ["act","pots","tops","cat","stop","hat"]

from collections import defaultdict

def groupAnagrams(strs):
    
    res = defaultdict(list)
    
    for str in strs:
        count = [0] * 26
         
        for c in str:
             
            count[ord(c) - ord('a')] += 1
        
        res[tuple(count)].append(str)
        
    return list(res.values())
            
            
            
    



print(groupAnagrams(strs))