class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # creating a hashmap
        hashMap = {}

        for i in range(len(nums)):
            fndr = target - nums[i]
            if nums[i] in hashMap:
                return [hashMap[nums[i]], i]
            else :
                hashMap[fndr] = i

soln = Solution()
print(soln.twoSum([2,7,11,15], 9))