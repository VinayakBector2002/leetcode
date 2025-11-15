class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        

        @cache
        def numWays(index: int, partitions: tuple) -> bool:
            p1, p2 = partitions

            if index == n and p1 == p2:
                return True

            if index >= n:
                return False
            
            curr = nums[index]
            new_p1 = tuple(sorted((p1 + curr, p2)))
            new_p2 = tuple(sorted((p1, p2 + curr)))

            return numWays(index + 1, new_p1) or numWays(index + 1, new_p2)


        return numWays(0, (0,0))