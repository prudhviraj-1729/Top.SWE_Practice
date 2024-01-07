# https://leetcode.com/problems/count-sub-islands/

def countSubIslands(grid1, grid2):
    count = 0
    if not grid2 or not grid1:
        return count
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited2 = set()

    def dfs(x, y):
        nonlocal flag
        visited2.add(x * len(grid2[0]) + y)
        if grid1[x][y] != 1:
            flag = False
        for dx, dy in directions:
            newX = x + dx
            newY = y + dy
            if newX >= 0 and newX < len(grid2) and newY >= 0 and newY < len(grid2[0]) and grid2[newX][newY] == 1 and newX * len(grid2[0])+newY not in visited2:
                dfs(newX, newY)

    for i in range(len(grid2)):
        for j in range(len(grid2[0])):
            if i * len(grid2[0]) + j not in visited2 and grid2[i][j] == 1 and grid1[i][j] == 1:
                flag = True
                dfs(i, j)
                if flag:
                    count += 1
    return count