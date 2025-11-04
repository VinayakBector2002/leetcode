from collections import deque 

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        queue = deque()
        visited = set()
        
        queue.append((start, 0))

        while queue:
            for i in range(len(queue)):
                curr, step = queue.popleft()
                if curr in visited:
                    continue
                    
                visited.add(curr)
                
                if curr == goal:
                    return step
                
                for k in nums:
                    add, sub, bit = curr + k, curr - k, curr ^ k
                    if goal in (add, sub, bit):
                        return step + 1
                    if add not in visited and 0 <= add <= 1000:
                        queue.append((add, step + 1))
                    if sub not in visited and 0 <= sub <= 1000:
                        queue.append((sub, step + 1))
                    if bit not in visited and 0 <= bit <= 1000:
                        queue.append((bit, step + 1))
        
        return -1