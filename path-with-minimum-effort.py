# https://leetcode.com/problems/path-with-minimum-effort/

from collections import defaultdict
from collections import heapq

def minimumEffortPath(grid):

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    n = len(grid)
    m = len(grid[0])
    source = [0, 0]
    destination = [n - 1, m - 1]
    
    distances = [[float("inf") for j in range(m)] for i in range(n)]
    distances[source[0]][source[1]] = 0
    
    priority_queue = [(0, tuple(source))]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == tuple(destination):
            return distances[n - 1][m - 1]
        
        for i, j in directions:
            p, q = current_node
            if p + i >= 0 and p + i < n and q + j >= 0 and q + j < m:
                max_abs_difference = max(abs(grid[p + i][q + j] - grid[p][q]), current_distance)
                if distances[p + i][q + j] > max_abs_difference:
                    distances[p + i][q + j] = max_abs_difference
                    heapq.heappush(priority_queue, (max_abs_difference, (p + i, q + j)))
    return -1