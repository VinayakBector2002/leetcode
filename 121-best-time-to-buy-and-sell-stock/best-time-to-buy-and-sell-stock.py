class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        curr_min = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            curr = prices[i]
            if curr < curr_min:
                curr_min = curr
                continue
            max_profit = max(max_profit, curr - curr_min)
        
        return max_profit