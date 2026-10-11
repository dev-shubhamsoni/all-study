
"""
Given two strings s and t, return true if the two strings are anagrams of each other, 
otherwise return false.

Two strings are anagrams if they contain the same characters, with each character appearing 
the same number of times, regardless of order.


Example 1:

Input: s = "racecar", t = "carrace"

Output: true

Example 2:

Input: s = "jar", t = "jam"

Output: false

"""

# Issues, not able to resolve this problem
# .get method can return 0 if value doesnt exists
# forgot to add check for length at the start
# currently there are all lowercase, but if mixed, lowercase all first
# not checking code for wrong things instead using chat gpt

s = "racecar"
t = "carrace"


def isAnagram( s, t):
    
    if len(s) != len(t):
        return False
    
    checkS = {}
    checkT = {}
    
    for i in range(len(s)):
        
        checkS[s[i]] = 1 + checkS.get(s[i], 0)
        checkT[t[i]] = 1 + checkT.get(t[i], 0)

    
    return checkS == checkT



print(isAnagram(s,t))