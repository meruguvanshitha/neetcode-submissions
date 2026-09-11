from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # If start or end is blocked, no path is possible
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
            
        # Queue stores: (row, col, current_path_length)
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1  # Mark the start cell as visited
        
        # 8 possible directions (horizontal, vertical, and diagonals)
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        
        while queue:
            r, c, length = queue.popleft()
            
            # If we reached the bottom-right corner
            if r == n - 1 and c == n - 1:
                return length
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and if the cell is unvisited (0)
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1  # Mark as visited
                    queue.append((nr, nc, length + 1))
                    
        return -1