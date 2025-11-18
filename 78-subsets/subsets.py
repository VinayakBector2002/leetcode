class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        results = []
        subset = []

        def helper(i: int):
            if i == n:
                results.append(subset.copy())
                return
            
            # choice
            subset.append(nums[i])
            helper(i + 1)
            subset.pop()
            helper(i + 1)
        
        helper(0)
        return results