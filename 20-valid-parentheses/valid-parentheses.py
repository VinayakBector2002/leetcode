class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char in '([{':
                stack.append(char)
                continue
            
            # else
            if stack and stack[-1] == hmap[char]:
                stack.pop()
            else:
                return False
        return not stack

        