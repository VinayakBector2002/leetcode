class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        strPtr = 0
        endPtr = len(numbers) - 1
        while True:
            # we can write this because 
            # guarantee to find the soln
            ttl = numbers(strPtr) + numbers(endPtr)
            if ttl > target:
                # current sum is greater than target
                endPtr -= 1
                continue
            elif ttl < target:
                # current sum is smaller than target
                strPtr += 1
                continue
            elif ttl == target:
                # 1-index array
                return [strPtr + 1, endPtr + 1]
                continue
            else:
                return
