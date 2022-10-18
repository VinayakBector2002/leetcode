class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        ans = 1
        while (i < len(nums)):
            if (nums[i]!= nums[i-1]):
                nums[ans] = nums[i]
                ans+=1
            i+=1
        return ans