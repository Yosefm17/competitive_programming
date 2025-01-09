#https://leetcode.com/problems/counting-words-with-a-given-prefix/
from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # Initialize a counter to keep track of the number of matches
        count = 0
        
        # Iterate through each word in the list
        for word in words:
            # Check if the current word starts with the given prefix
            if word.startswith(pref):
                # Increment the counter if the condition is satisfied
                count += 1
        
        return count
