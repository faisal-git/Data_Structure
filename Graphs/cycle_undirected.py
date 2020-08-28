# cycle provides alterante path  for a pair of nodes
# track back edges.
# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
# BFS can also be used 
# using DFS
def dfs(v,visited,parent,g):
    visited[v]=True
    for node in g[v]:
        if not visited[node]:
            if dfs(node,visited,v,g):
                return 1
        elif parent!=node:
            return 1
    return 0
            
def isCyclic(g,n):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph
    :return:  boolean (whether a cycle exits or not)
    '''
    # code here
    visited=[False]*n
    for v in range(n):
        if not visited[v]:
            if dfs(v,visited,-1,g):
                return 1
    return 0


# union-find algorithm for cycle detection in undirected graphs.
# https://www.geeksforgeeks.org/union-find/