"""
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false


"""

# Arrived at brute force solution
# this problem as a mathcing sol group anagrams, the logic is same with sliding window modification

s1 = "abc"
s2 = "lecabee"

# def permutationInString(s1,s2):
    
    
#     k = len(s1)
    
#     s1Map = {}

    
#     for val in s1:
#         s1Map[val] = s1Map.get(val, 0) + 1
        
    
#     for i in range(0, len(s2) - k + 1):
        
#         currMap = {}
#         j = i
        
#         while j < i + k:
#             currMap[s2[j]] = currMap.get(s2[j], 0) + 1
#             j += 1
        
#         if s1Map == currMap:
#             return True          
#     return False
        
    
    
def permutationInString(s1, s2):
    
    if len(s1) > len(s2):
        return False

    k = len(s1)
    s1Count = [0] * 26
    winCount = [0] * 26

    for i in range(k):
        s1Count[ord(s1[i]) - ord('a')] += 1
        winCount[ord(s2[i]) - ord('a')] += 1

    if s1Count == winCount:
        return True

    for r in range(k, len(s2)):
        winCount[ord(s2[r]) - ord('a')] += 1        # add new right char
        winCount[ord(s2[r - k]) - ord('a')] -= 1    # remove old left char
        if s1Count == winCount:
            return True

    return False



print(permutationInString(s1,s2))