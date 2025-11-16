class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        fromLeft = [1]
        for number in nums:
            fromLeft.append(fromLeft[-1]*number)
        fromLeft.append(1)

        fromRight = [1]
        for number in nums[::-1]:
            fromRight.append(fromRight[-1]*number)
        fromRight.append(1)        
        fromRight = fromRight[::-1]

        answer = []
        for i in range(1, n + 1):
            answer.append(fromLeft[i - 1] * fromRight[i + 1])
        return answer
    