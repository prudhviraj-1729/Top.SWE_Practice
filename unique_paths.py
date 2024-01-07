# https://leetcode.com/problems/unique-paths/

def uniquePaths(m, n):
    
    grid = [[1 for j in range(n)] for i in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[-1][-1]