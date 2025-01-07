from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Initialize an empty list to store substrings
        result = []
        
        # Iterate through each word in the list
        for i in range(len(words)):
            for j in range(len(words)):
                # Check if a word is a substring of another word and avoid comparing the word with itself
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break  # Avoid adding duplicates
        
        return result