class Solution:
    def isPalindrome(self, x: int) -> bool:
        numList = list(str(x))
        return numList == numList[::-1]
        