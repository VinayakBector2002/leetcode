class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        subset = []
        def backtrack():
            if len(subset) == n:
                result.append(subset[:])
                return
            # else 
            for number in nums:
                if number not in subset:
                    subset.append(number)
                    backtrack()
                    subset.pop()
            
        backtrack()
        return result
