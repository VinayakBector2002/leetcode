class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict ={}
        for index, element in enumerate(nums):
            find = target - element 
            if (find in dict):
                return [dict[find], index]
            else:
                dict[element] = index
        