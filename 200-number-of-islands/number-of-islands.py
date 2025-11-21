class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        
        def dfs(x,y):
            visited.add((x,y))

            for dx, dy in directions:
                X,Y= x+dx, y+dy
                if X in range(rows) and Y in range(cols) and grid[X][Y] == "1" and (X,Y) not in visited: 
                    dfs(X,Y)
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count += 1
        
        return count