class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = []
        for char in s:
            if char.isalnum():
                sanitized.append(char.lower())
        
        santizedString = "".join(sanitized)
        return santizedString == santizedString[::-1]