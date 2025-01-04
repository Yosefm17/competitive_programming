class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Set to store unique palindromic subsequences
        unique_palindromes = set()
        
        # Iterate over all lowercase letters as potential centers
        for c in set(s):
            # Find the first and last occurrence of the character
            first = s.find(c)
            last = s.rfind(c)
            
            # If there's enough room for a palindromic subsequence
            if last - first > 1:
                # Add all characters between first and last to form palindromes
                for mid_char in set(s[first + 1:last]):
                    unique_palindromes.add((c, mid_char, c))
        
        # Return the count of unique palindromic subsequences
        return len(unique_palindromes)
