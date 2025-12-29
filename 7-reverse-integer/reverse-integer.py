class Solution:
    def reverse(self, x: int) -> int:
        stack = list(str(x))
        result = []
        
        # pop all the trailng zeros
        while stack and stack[-1] == '0':
            stack.pop()

        if len(stack) == 0:
            return 0
        
        while stack and stack[-1] != "-":
            result.append(stack.pop())
        
        result = "".join(result)
        result = int(f"-{result}") if stack else int(result)
        
        return result if result in range(-2**31, 2**31) else 0