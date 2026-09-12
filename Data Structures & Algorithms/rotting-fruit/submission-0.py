from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes = 0

        # Step 1: Find all initial rotten fruit and count fresh fruit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # Direct return if there are no fresh fruits to rot
        if fresh_count == 0:
            return 0

        # Step 2: Multi-Source BFS
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue and fresh_count > 0:
            # Process all nodes at the current minute level
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check boundary and if the neighbor is a fresh fruit
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Mark as rotten
                        fresh_count -= 1
                        queue.append((nr, nc))

            minutes += 1

        # If fresh fruit remains, it was impossible to reach them
        return minutes if fresh_count == 0 else -1