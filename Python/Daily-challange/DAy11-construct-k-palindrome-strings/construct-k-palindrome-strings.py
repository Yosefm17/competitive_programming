from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of the string, it's impossible to construct k palindromes
        if k > len(s):
            return False
        
        # Count the frequency of each character
        char_count = Counter(s)
        
        # Count the number of characters with an odd frequency
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # We can construct at least 'odd_count' palindromes,
        # so it's possible if odd_count <= k
        return odd_count <= k
