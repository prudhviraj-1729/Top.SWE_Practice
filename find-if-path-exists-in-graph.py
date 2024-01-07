# https://leetcode.com/problems/find-if-path-exists-in-graph/

from typing import List
from collections import deque

def validPath(n, edges, source, destination):
    def creategraph(edges):
        graph = {}
        for edge in edges:
            u, v = edge[0], edge[1]
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        return graph

    graph = creategraph(edges)
    vis = set([source])
    q = deque([source])

    while len(q)!=0:
        curr = q.popleft()
        if curr == destination:
            return True
        for n in graph[curr]:
            if n not in vis:
                q.append(n)
                vis.add(n)
    return False