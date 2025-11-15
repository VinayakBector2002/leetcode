class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n < 3:
            return min(cost)
        
        @cache
        def helper(index: int) -> int:
            if index >= n:
                return 0
            
            if index in (n - 1, n - 2):
                return cost[index]
            
            return cost[index] + min(helper(index + 1), helper(index + 2))
        
        return min(helper(0), helper(1))