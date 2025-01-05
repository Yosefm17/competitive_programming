from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Initialize the difference array
        n = len(s)
        diff = [0] * (n + 1)

        # Apply shifts to the difference array
        for start, end, direction in shifts:
            shift_value = 1 if direction == 1 else -1
            diff[start] += shift_value
            diff[end + 1] -= shift_value

        # Apply shifts directly to the result string
        result = []
        cumulative_shift = 0
        for i in range(n):
            cumulative_shift += diff[i]
            # Compute the shifted character
            shift_amount = cumulative_shift % 26  # Ensure the shift is within bounds
            new_char = chr((ord(s[i]) - ord('a') + shift_amount) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)
