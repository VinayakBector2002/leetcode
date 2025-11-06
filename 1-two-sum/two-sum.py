class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        for i in range(len(nums)):
            curr = nums[i]
            if curr in sumMap:
                return [sumMap[curr], i]
            sumMap[target - curr] = i
        