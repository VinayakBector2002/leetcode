class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        n = len(days)

        def backtrack(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]

            memo[i] = sys.maxsize

            k = i 
            for cost, duration in zip(costs, [1, 7, 30]):
                while k < n and days[k] - days[i] < duration:
                    k += 1
                memo[i] = min(memo[i], backtrack(k) + cost)
            return memo[i]
        
        return backtrack(0)            
