class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}
        n = len(questions)

        def dfs(index):
            if index >= n:
                return 0
            if index in dp:
                return dp[index]
            points, brainpower = questions[index]
            dp[index] = max(dfs(index + 1), points + dfs(index + 1 + brainpower))
            return dp[index]
        
        return dfs(0)