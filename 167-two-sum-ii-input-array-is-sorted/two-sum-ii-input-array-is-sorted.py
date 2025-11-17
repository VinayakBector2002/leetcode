class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n == 1:
            return numbers[0] == k
        
        l,r = 0, n - 1

        while (l < r):
            current = numbers[l] + numbers[r]
            if current < target:
                l += 1
            elif current > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        
        return -1