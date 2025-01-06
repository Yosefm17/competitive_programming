from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        # Single pass to calculate operations in one traversal
        left_count, left_operations = 0, 0
        right_count, right_operations = 0, 0

        for i in range(n):
            # Update answer with operations from the left side
            answer[i] += left_operations
            if boxes[i] == '1':
                left_count += 1
            left_operations += left_count

        for i in range(n - 1, -1, -1):
            # Update answer with operations from the right side
            answer[i] += right_operations
            if boxes[i] == '1':
                right_count += 1
            right_operations += right_count

        return answer
