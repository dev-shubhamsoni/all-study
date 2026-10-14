"""

Given an array of integers representing card values, write a function to calculate the 
maximum score you can achieve by picking exactly k cards.

You must pick cards in order from either end. You can take some cards from the beginning, 
then switch to taking cards from the end, but you cannot skip cards or pick from the middle.

For example, with k = 3:

Take the first 3 cards: valid
Take the last 3 cards: valid
Take the first card, then the last 2 cards: valid
Take the first 2 cards, then the last card: valid
Take card at index 0, skip some, then take card at index 5: not valid (skipping cards)
Constraints: 1 <= k <= cards.length

Example 1: Input:

cards = [2,11,4,5,3,9,2]
k = 3

"""
cards = [1,2,3,4,5,6,1]
k = 3

def maxScore(cards, k):
    
    
    curr_score = sum(cards[:k])
    max_score = curr_score
   
   
    for i in range(0, len(cards) - k):
        
        curr_score -= cards[i]
        curr_score += cards[i + k]
        
        max_score = max(max_score, curr_score)
    
    
    
    return max_score
    



print(maxScore(cards, k))
