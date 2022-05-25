class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        HashMap = {}
        sorted_nums = nums.copy()
        sorted_nums.sort()
        output = []
        a = range(len(nums))
        for i in a:
            if ((i != 0) and (sorted_nums[i] == sorted_nums[i-1])):
                continue
            else:
                HashMap[sorted_nums[i]] = i
        
        for i in range(len(nums)):
            output.insert(i,HashMap.get(nums[i]))
        
        return output
        
        
        
            
        