#undirected graphs

def connected(node,visited,graph):
    visited[node]=True
    res=[node]
    if graph.get(node): # this can be skipped if graph is defaultdict(list) 
        for each in graph[node]:
            if not visited[each]:
                res+=connected(each,visited,graph)
    return res
# another approach
def connected(node,visited,temp,graph):
    visited[node]=True
    temp.append(node)
    if graph.get(node): # this can be skipped if graph is defaultdict(list) 
        for each in graph[node]:
            if not visited[each]:
                res+=connected(each,visited,temp,graph)
    return temp
