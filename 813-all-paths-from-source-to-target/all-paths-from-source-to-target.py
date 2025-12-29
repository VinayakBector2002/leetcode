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
