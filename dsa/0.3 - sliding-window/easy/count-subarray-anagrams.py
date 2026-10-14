



s = 'gattactat'
anagram = 'att'


def countSubArrayAnagram(s, anagram):

    k = len(anagram)
    
    curr_window_map = {} 
    anagram_map = {} 
    count = 0
    
    for i in range(0, k):
        
        curr_window_map[s[i]] = curr_window_map.get(s[i], 0) + 1
        
    for i in range(0, k):
        anagram_map[anagram[i]] = anagram_map.get(anagram[i], 0) + 1
        
    if curr_window_map == anagram_map:
        count += 1
    
    
    for i in range(0, len(s) - k):
        
        curr_window_map[s[i]] -= 1
        
        if curr_window_map.get(s[i]) == 0:
            del curr_window_map[s[i]]
        
        curr_window_map[s[i + k]] = curr_window_map.get(s[i + k], 0) + 1
        
        if curr_window_map == anagram_map:
            count += 1
            
    return count        
        
        
        
        
        



print(countSubArrayAnagram(s, anagram))








