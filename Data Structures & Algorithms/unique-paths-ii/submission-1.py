class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        row = [0] * n
        row[0] = 1  # Base case: start at 1 path

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    row[j] = 0  # Blocked cell has 0 paths
                elif j > 0:
                    row[j] += row[j - 1]  # Add paths coming from the left

        return row[-1]