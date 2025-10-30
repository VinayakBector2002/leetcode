class Solution:
    # Top Down
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        n = len(days)
        dp[n] = 0

        def dfs(index):
            if index in dp:
                return dp[index]

            dp[index] = sys.maxsize
            k = index
            for cost, duration in zip(costs, [1,7,30]):
                while k < len(days) and days[k] - days[index] < duration :
                    k += 1
                dp[index] = min(dp[index], dfs(k) + cost)
            return dp[index]
        
        return dfs(0)
            
    # Bottom Up
    # def mincostTickets1(self, days: List[int], costs: List[int]) -> int:
    #     n = len(days)
    #     dp = [0] * (n + 1)
    #     for i in range(1, n + 1):
    #         dp[i] = dp[i - 1] + costs[0]

    #         j = i - 1
    #         while j > 0 and days[i - 1] - days[j - 1] < 7:
    #             j -= 1
    #         dp[i] = min(dp[i], dp[j] + costs[1])
            
    #         k = i - 1
    #         while k > 0 and days[i - 1] - days[k - 1] < 30:
    #             k -= 1
    #         dp[i] = min(dp[i], dp[k] + costs[2])
    #     return dp[n]
            