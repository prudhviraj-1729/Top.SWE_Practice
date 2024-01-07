# https://leetcode.com/problems/is-graph-bipartite/

def isBipartite(graph):
        
    color = ["no_color" for i in range(len(graph))]

    def dfs(parent):
        if color[parent] == "no_color":
            color[parent] = "red"
        for child in graph[parent]:
            if color[child] == "no_color":
                if color[parent] == "red":
                    color[child] = "blue"
                elif color[parent] == "blue":
                    color[child] = "red"
                if dfs(child) == False:
                    return False
            elif color[child] == color[parent]:
                return False
        return True

    for node in range(len(graph)):
        if color[node] == "no_color":
            if dfs(node) == False:
                return False
    return True