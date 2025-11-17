class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        retVal = [[]]
        prev_answer = [[i] for i in nums]
        retVal.extend(prev_answer)
        print(retVal)
        n = len(nums)
        for i in range(n - 1):
            current = []
            for k in prev_answer:
                print(k)
                for item in nums:
                    if item > k[-1]:
                        current.append(k[::] + [item])  
            retVal.extend(current)
            prev_answer = current
        return retVal
