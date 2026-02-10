from bisect import bisect_left
'''

Input: List[str] Given an integer array nums
Output: Int return the number 
Task: Of triplets chosen from the array that can make 
    triangles if we take them as side lengths of a triangle.

'''

class Solution:

    # On^2 log n
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                currPeri = nums[i] + nums[j]
                intersection = bisect_left(nums, currPeri,lo=j + 1)
                count += intersection - j - 1
        return count