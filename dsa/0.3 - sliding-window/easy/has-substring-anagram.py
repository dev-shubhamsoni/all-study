

"Problem we need to find if an anagram exist int he stirng"

# Learned how to put values in set by defualt and by methods

s = 'greyhounds'
anagram = 'hoy'


def hasSUbstringAnagram(s, anagram):
    
    k = len(anagram)
    
    window_set = set(s[:k])
    anagram_set = set(anagram)
    
    if window_set == anagram_set:
        return True
    
    
    for i in range(0, len(s) - k):
        window_set.remove(s[i])
        window_set.add(s[i + k])
        
        if window_set == anagram_set:
            return True


    return False



print(hasSUbstringAnagram(s, anagram))