from collections import deque, defaultdict
from copy import deepcopy

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = deque()
        q.append([0])
        target =  len(graph) - 1
        paths = []
        
        def dfs():
            while q:
                currentPath = q.pop()
                for nbr in graph[currentPath[-1]]:    
                    copyPath = deepcopy(currentPath)
                    copyPath.append(nbr)

                    if nbr == target:
                        paths.append(copyPath)
                    else:
                        q.append(copyPath)
        dfs()
        return paths