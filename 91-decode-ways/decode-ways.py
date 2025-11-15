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
        print(dp)
        return dp[0]
