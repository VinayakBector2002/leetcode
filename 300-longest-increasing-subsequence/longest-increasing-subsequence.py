'''
Given an integer array nums, (input)

return the length (int)

the longest strictly!!! increasing subsequence (no change of order but can remove element)
summary : chose a predec which is smaller than me but has largest predecs
[10,9,2,5,3,7,101,18]

10 -> [101] -> 101 -> []
9 -> [101] -> 101 -> []
  -> [18]
2 -> [5] -> [7] -> [101]
  -> [3]
  -> [7]
  -> [101]
  -> [18]  
5 -> [7] -> 7 -> [101]
  -> [101] -> 101 -> []
  -> [18]
3 -> [7]
7 -> [101]
  -> [18]

18 -> []
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] # base, index: number of ways to get there
        for i in range(1, len(nums)):
            curr_max = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    curr_max = max(curr_max, LIS[j] + 1)
            LIS.append(curr_max)
        return max(LIS)
            
        