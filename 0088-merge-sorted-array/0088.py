class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        breakpoint()
        pointer = m + n - 1 # ptr to last element in nums1
        while (m > 0) and (n > 0):
            if (nums1[m - 1] > nums2[n - 1]):
                nums1[pointer] = nums1[m - 1]
                m -= 1
            else :
                nums1[pointer] = nums2[n - 1]
                n -= 1
            pointer -= 1

        while (n > 0):
            nums1[pointer - 1] = nums2[n - 1]
            pointer -= 1
            n -= 1 




soln = Solution()
nums1 = [2,0]
soln.merge(nums1, 1, [1], 1)
print(nums1)