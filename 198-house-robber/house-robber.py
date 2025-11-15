'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums (input) int
return the maximum amount of total money (output) int

for any 2 adj houses we need to make a choice about which one to rob
[1,2,3,1]
1 3 -> take : [3, 1] ** 
        take 3
        take 1
  3 -> not: [2,3,1]
        take 2 and take 1 Base
        not:
            [3, 1] ** 
            3
for 2 branches we take the max of them + current place
base cases one element left


1 <= nums.length <= 100 small
0 <= nums[i] <= 400     small
'''

 
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def helper(index: int) -> int:
            if index >= n:
                return 0
            
            if index == n - 1:
                return nums[index]
            
            if index == n - 2:
                return max(nums[n - 2],nums[n - 1])
            

            value =  max(helper(index + 1), nums[index] + helper(index + 2))
            return value
        
        return helper(0)
        