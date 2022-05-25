class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sort = nums.copy()
        nums_sort.sort()
        nums_sort.reverse()
        Hash_map = {}
        output=list()
        length = len(nums_sort)
        for i in range(length):
            if nums_sort[i] in Hash_map:
                Hash_map[nums_sort[i]]+=1
            Hash_map[nums_sort[i]]=i
        for i in range(length):
            output.insert(i,(length - Hash_map[nums[i]] - 1))
        return output