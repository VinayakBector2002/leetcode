class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for number in nums:
            if number in hashmap:
                return True
            #else
            hashmap[number] = 1
        return False