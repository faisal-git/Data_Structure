# time : O(V+E)
# can be applied on DAG
def topological(v,visited,order,g):
    visited[v]=True
    for adj,w in g[v]:
        if not visited[adj]:
            topological(adj,visited,order,g)
    order.append(v)

# take inputs as adjacency list: in g as { source:[[des,weight],[....]]}
# let there are n nodes 0 to n-1
visited=[False]*n
dis =[float('inf')]*n
dis[0]=0 # 0 is source 
stack=[]
for v in range(n):
    if not visited[v]:
        topological(v,visited,stack,g)

for node in stack[::-1]:
    for adj,w in g[node]:
        if dis[adj]>dis[node]+w:
            dis[adj]=dis[node]+w
print(*dis) # shortest distance from source here is 0 to all other nodes