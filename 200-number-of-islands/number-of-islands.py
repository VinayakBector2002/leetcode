from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1], [1,0], [0,-1], [-1, 0]]
        visited = set()
        rows, cols = len(grid), len(grid[0])
        count = 0 

        def dfs(i,j):
            # (i,j) not in visited all the time 
            visited.add((i,j))

            q = deque([(i,j)])
            while q:
                x,y = q.popleft()
                for dx,dy in directions:
                    X, Y = x+dx, y+dy
                    if X in range(rows) and Y in range(cols) and (X,Y) not in visited:
                        if grid[X][Y] == "1":
                            q.append([X,Y])
                        visited.add((X,Y))
                    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count += 1
        return count