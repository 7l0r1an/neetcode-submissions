class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        contor = 0
        randuri = len(grid)
        coloane = len(grid[0])
        
        def fill(i,j):
            if i < 0 or j < 0 or i >= randuri or j >= coloane or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            fill(i+1, j)
            fill(i-1, j)
            fill(i, j+1)
            fill(i, j-1) 
        for i in range(randuri):
            for j in range(coloane):
                if grid[i][j] == "1":
                    contor += 1
                    fill(i,j)
        return contor