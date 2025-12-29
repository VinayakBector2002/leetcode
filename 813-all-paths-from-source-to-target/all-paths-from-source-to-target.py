'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []

        def dfs(node, path):
            if node == target:
                res.append(path)
                return
            
            for nbr in graph[node]:
                dfs(nbr, path + [nbr])

        dfs(0, [0])
        return res

'''

from collections import deque, defaultdict

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
                    newPath = currentPath + [nbr] 
                    if nbr == target:
                        paths.append(newPath)
                    else:
                        q.append(newPath)
        dfs()
        return paths