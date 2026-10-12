"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and 
ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false

"""

# - learned About Ord again and how to use it to check if the char 
# is alphanumeric or not
# solved using two pointers.

s = "Was it a car or a cat I saw?"



def validPalindrome(str):
    
    left = 0
    right = len(str) - 1
    
    while(left < right):
        
        if not alphaNum(str[left]):
            left += 1
            continue
            
        if not alphaNum(str[right]):
            right -= 1
            continue
            
        if str[left].lower() == str[right].lower():
            left += 1
            right -= 1
        else:
            return False 
    
   
    return True

    #another Solution
    
    # l, r = 0, len(s) - 1

    #     while l < r:
    #         while l < r and not self.alphaNum(s[l]):
    #             l += 1
    #         while r > l and not self.alphaNum(s[r]):
    #             r -= 1
    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l, r = l + 1, r - 1
    #     return True

def alphaNum(c):
    
    return (ord('A') <= ord(c) <= ord('Z') or
       ord("a") <= ord(c) <= ord('z') or
       ord('0') <= ord(c) <= ord('9'))
        
    
    return        
    


print(validPalindrome(s))
    
