class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # init
        nums.sort()
        n = len(nums)
        answer = set()
        result = []
        
        # helper
        def backtrack(index: int):
            if index == n:
                # it's time to add + return : )
                answer.add(tuple(result[:]))
                return
            
            result.append(nums[index])
            backtrack(index + 1)
            result.pop()
            backtrack(index + 1)
        
        backtrack(0)
        return list(answer)

        