# https://leetcode.com/problems/path-with-maximum-probability/

from collections import defaultdict
from collections import heapq

def maxProbability(n, edges, succProb, start, end):
    # construct the graph
    graph = defaultdict(list)
    prob = defaultdict(dict)
    for i,(p,[a,b]) in enumerate(zip(succProb,edges)):
        graph[a].append(b)
        graph[b].append(a)
        prob[a][b] = prob[b][a] = p
    # apply dijkstra
    dis = {start:1}
    for i in range(n):
        dis[i] = 0
    visited = set([])
    # note that Python only supports min-heap
    # so some tricks here to get a max-heap
    pq = [(-1,start)]
    while pq:
        _p, node = heapq.heappop(pq)
        visited.add(node)
        for child in graph[node]:
            if child not in visited:
                if dis[child] < -1 * _p * prob[node][child]:
                    heapq.heappush(pq,(_p * prob[node][child],child))
                    dis[child] = -1 * _p * prob[node][child]

    return dis[end]