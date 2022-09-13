class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        ans = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    
                    self.counti(r,c,grid)
                    ans+=1
        
        return ans
        
    def counti(self,r,c,grid):
        n = len(grid)
        m = len(grid[0])
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c] != '1':
            return
        grid[r][c] = '#'
        # counti(r+1,c+1)
        self.counti(r+1,c,grid)
        # counti(r+1,c-1)
        self.counti(r,c+1,grid)
        self.counti(r-1,c,grid)
        self.counti(r,c-1,grid)    