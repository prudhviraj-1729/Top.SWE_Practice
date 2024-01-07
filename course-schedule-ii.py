# https://leetcode.com/problems/course-schedule-ii/description/

from collections import defaultdict
from collections import deque

def findOrder(numCourses, prerequisites):
    in_degree = [0 for i in range(numCourses)]

    adj = defaultdict(list)

    for i, j in prerequisites:
        adj[j].append(i)

    for i in adj:
        for j in adj[i]:
            in_degree[j] += 1
    
    queue = deque()

    for node in range(numCourses):
        if in_degree[node] == 0:
            queue.append(node)
        
    res = []
    count = 0

    while queue:
        parent = queue.popleft()
        res.append(parent)
        for child in adj[parent]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

        count += 1
    
    if count == numCourses:
        return res
    return []