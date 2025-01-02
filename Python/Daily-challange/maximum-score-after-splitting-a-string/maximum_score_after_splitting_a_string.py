class Solution:
    def maxScore(self, s: str) -> int:
        # Count the total number of ones in the string
        total_ones = s.count('1')
        
        max_score = 0
        left_zeros = 0
        right_ones = total_ones
        
        # Iterate up to len(s) - 1 to ensure both substrings are non-empty
        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1
            # Calculate the score for the current split
            max_score = max(max_score, left_zeros + right_ones)
        
        return max_score