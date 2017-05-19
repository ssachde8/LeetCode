class Solution(object):
    def search(self, i, j, grid, mark):
        return
    
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
        
    def dfs(self, grid, i, j):
        if(i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == '0'):
            return
        grid[i][j] = '0' #eliminate the need for a visited array by manipulating grid
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)
        
        
        