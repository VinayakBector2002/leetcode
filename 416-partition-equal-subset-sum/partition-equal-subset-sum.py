
'''
Given an integer array nums

return true 

if you can partition the array into 
    two subsets such that 
        the sum of the elements in both subsets is equal or false otherwise.

Understanding -> Divide the list into 2 parts st the sum is equal 
    Reccursion Tree 
    for a given index i and partitions p1 and p2
    put i in partition 1 (p1 + nums[i], p2)
    otherwise (p1, p2  + nums[i])

    [0,0,0] -> [1, 1, 0]
                -> [1, 6, 0]  *
                -> [1, 1, 5]  **               
            -> [1, 0, 1]
                -> [1, 0, 6]  * 
                -> [1, 5, 1]  **
    
    duplicates, by sorting the partition
    Base cases 
        - index at the end then no +1
        - partitions are equal 

[1,5,11,5] ->  [1, 5, 5], [11] -> True

Constraints:
    1 <= nums.length <= 200 small
    1 <= nums[i] <= 100 small
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return False
        
        @cache
        def numsWaysPartition(index: int, partitions: tuple):
            if partitions[0] == partitions[1] and index == n:
                return True
            if index >= n:
                return False
            curr = nums[index]
            p1,p2 = partitions
            paritions1 = tuple(sorted((p1 + curr, p2)))
            paritions2 = tuple(sorted((p1, p2 + curr)))
            return numsWaysPartition(index + 1, paritions1) or numsWaysPartition(index + 1, paritions2)
        
        return numsWaysPartition(0, (0,0))
