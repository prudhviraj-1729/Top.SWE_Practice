# https://leetcode.com/problems/number-of-islands/

from collections import deque

def numIslands(grid):
        
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def dfs(x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == "-1" or grid[x][y] == "0":
            return
        grid[x][y] = "-1"                       # Says that it is visited
        for i, j in directions:
            dfs(x + i, y + j)

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        grid[x][y] = "-1"                       #Says that it is visited

        while queue:
            p, q = queue.popleft()
            for i, j in directions:
                if p + i >= 0 and p + i < len(grid) and q + j >= 0 and q + j < len(grid[0]) and grid[p + i][q + j] == "1":
                    grid[p + i][q + j] = "-1"
                    queue.append((p + i, q + j))
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(i, j)               # DFS Call
                # bfs(i, j)               # BFS Call
                count += 1
    return count