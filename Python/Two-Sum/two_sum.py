from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use a dictionary for fast lookups
        num_to_index = {}
        
        # Enumerate through nums for index and value
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                # Return immediately upon finding the result
                return [num_to_index[complement], i]
            # Add current number and index to the dictionary
            num_to_index[num] = i

        # No need for additional return due to guaranteed solution
