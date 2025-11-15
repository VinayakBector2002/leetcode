'''
Input: Given a string s containing only digits  int
Output: return the number of ways to decode it int

Summary 
    - Encoding A -> 1, B -> 2 ...
    - There are many different ways you can decode the message
        - Given digit can be paired with the one after it to resolve


0: 
    1 -> A
        1: 
            1  -> A
            11 -> K
    11 -> K 
        2:
            1  -> A
            10 -> K

If the entire string cannot be decoded in any valid way, return 0.


2 2 6
  2 1
6 -> 1
26 -> 2 | 6 | -> 1
    -> |26| -> 1
2
'''

class Solution:
    def __init__(self):
        self.listOfNums = [str(i) for i in range(1, 27)]

    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n)
        # Last index
        dp[n - 1] = 1 if s[-1] in self.listOfNums else 0

        for i in range(n - 2, -1, -1):    
            # singular
            if dp[i + 1] and s[i] in self.listOfNums:
                dp[i] += dp[i + 1]
            
            if i + 2 <= n - 1:
                if dp[i + 2] and s[i: i +2] in self.listOfNums:
                    dp[i] += dp[i + 2]
            elif s[i:i+2] in self.listOfNums:
                dp[i] += 1
            # dp[i] = count
        print(dp)
        return dp[0]
