"""
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5

"""

# The logc wa shard to grasp
# We need to take the char cout and chaeck woth window length curr_window - max_freq <= k

s = "AABABBA"
k = 1

def longestRepeatingCharReplacement(s, k):
    
    char_freq = {}
    
    max_freq = 0
    l = 0
    r = 0
    best = 0
    curr_window = 0
    
    while r < len(s):
        
        char_freq[s[r]] = char_freq.get(s[r], 0) + 1
        
        for v in char_freq.values():
            max_freq = max(max_freq, v)
            
        curr_window = r - l + 1
        
        if curr_window - max_freq <= k:
            best = max(best, curr_window)
        else:
            char_freq[s[l]] = char_freq.get(s[l]) - 1
            l += 1
            
        r += 1
        
    return best    
    
    
    
    
    
    
    
    

print(longestRepeatingCharReplacement(s,k))