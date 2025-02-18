class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []  # Stack to keep track of numbers in descending order
        result = ""
        num = 1  # Start with the smallest number '1'
        
        for ch in pattern:
            stack.append(str(num))
            num += 1
            
            if ch == 'I':
                while stack:
                    result += stack.pop()
        
        stack.append(str(num))  # Append the last number
        while stack:
            result += stack.pop()
        
        return result
