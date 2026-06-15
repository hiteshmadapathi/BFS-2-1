# Time Complexity --> O(m*n)
# Space Complexity --> O(m*n)

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh += 1
        
        if len(q)==0 and fresh==0:
            return 0

        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        time = 0
        while len(q)>0:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                for dir in dirs:
                    nr = curr[0] + dir[0]
                    nc = curr[1] + dir[1]
                    if nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc]==1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            time += 1
        
        if fresh>0:
            return -1
        return time-1
