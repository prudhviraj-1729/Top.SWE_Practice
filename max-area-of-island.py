# https://leetcode.com/problems/max-area-of-island/

def maxAreaOfIsland(grid):
        
    m = len(grid)
    n = len(grid[0])
    
    parent = [i for i in range(m * n)]
    size = [1 for i in range(m * n)] 
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    def find(parent, i):
        if parent[i] != i:
            parent[i] = find(parent, parent[i])
        return parent[i]
    
    def union(parent, size, x, y):
        x_rep = find(parent, x)
        y_rep = find(parent, y)
        
        if x_rep == y_rep:
            return 
        if size[x_rep] < size[y_rep]:
            parent[x_rep] = y_rep
            size[y_rep] += size[x_rep]
        elif size[y_rep] < size[x_rep]:
            parent[y_rep] = x_rep
            size[x_rep] += size[y_rep]
        else:
            parent[y_rep] = x_rep
            size[x_rep] += size[y_rep]
            
    hasIsland = False
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                hasIsland = True
                for x, y in directions:
                    if i + x >= 0 and i + x < m and j + y >= 0 and j + y < n and grid[i + x][j + y] == 1:
                        union(parent, size, i * n + j, (i + x) * n + (j + y))

    if not hasIsland:
        return 0

    res = 0
    for i in range(m * n):
        res = max(res, size[i])
    return res 