class Solution:
    def rob1(self, nums: List[int]) -> int:

        n = len(nums)

        @cache
        def helper(index: int) -> int:
            if index >= n:
                return 0
            if index == n - 1:
                return nums[-1]
            if index == n - 2:
                return max(nums[-1], nums[-2])
            
            return max(nums[index] + helper(index + 2), helper(index + 1))
        
        return helper(0)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]

        return max(self.rob1(nums[1::]), self.rob1(nums[:-1:]))    