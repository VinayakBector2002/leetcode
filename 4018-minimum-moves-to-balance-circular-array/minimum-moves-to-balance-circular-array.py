class Solution:
    def minMoves(self, balance: List[int]) -> int:
        if sum(balance) < 0:
            return -1
        
        idx = None
        n = len(balance)

        for i in range(n):
            if balance[i] < 0:
                idx = i
        
        if idx is None:
            return 0
        
        result = 0
        val = balance[idx]
        step = 1
        left, right = (idx - 1) % n , (idx + 1) % n
        while (val < 0):
            if balance[left] > 0:
                take = min(balance[left], -val)
                val += take
                result += take * step
            
            if balance[right] > 0:
                take = min(balance[right], -val)
                val += take
                result += take * step
            left = (left - 1) % n
            right= (right + 1) % n
            step += 1
        
        return result
