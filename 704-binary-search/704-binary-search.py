class Solution:
    def search(self, nums: List[int], target: int) -> int:
        last = len(nums)
        start = 0
        end = len(nums)-1
        while ((start <= end)):
            mid = round(end-start/2)
            if (nums[mid] == target):
                # Number was found
                return mid
            elif (nums[mid] < target):
                # Target on right list 
                start = mid + 1
                continue
            else :
                end = mid - 1
                continue
        return -1