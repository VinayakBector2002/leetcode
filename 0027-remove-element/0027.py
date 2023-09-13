class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        track = 0 
        k = 0
        # breakpoint()
        while track < len(nums):
            if nums[track] != val:
                k += 1
                track += 1
                continue
            if nums[track] == val:
                replace = track + 1
                while replace < len(nums):
                    if nums[replace] != val:
                        # breakpoint()
                        nums[track], nums[replace] = nums[replace], nums[track]
                        k += 1
                        break
                    replace += 1
                track += 1
                continue
        return k

soln = Solution()
print(soln.removeElement([0,1,2,2,3,0,4,2],2))