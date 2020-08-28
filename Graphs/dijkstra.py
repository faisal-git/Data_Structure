# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# https://leetcode.com/problems/network-delay-time/
# dijkstra algorithm is sssp in a graph with no negative weights
# Time and space complexity greatly depends on how it is implemented 
# it ranges from O(E*logV) because we look each egde atlest once and logV is fetching currently unexplored with least cost from priority queue/heap 
# but for a dense graph E =V^2 ,in this case O(V^2logV)
# when we implement with array instead of heap/priority q ,Time : O(V^2)
# more pricisely it is O(V^2 + E) since dijkstra algorithms tries to visit all nodes 
# dont gurantee correct result if there is negetive weights

import collections
import heapdict as hd

def dijkstra(q,dis,p,visited,graph):
    while q:
        #print(len(q.items()))
        v,c=q.popitem()
        #print('current',c,v)
        # early exit c if found
        if v==len(dis)-1: return 
        if v not in visited:
            for adj,w in graph[v]:
                if adj not in visited and dis[adj]>c+w:
                    dis[adj]=c+w
                    p[adj]=v
                    q[adj]=c+w
                
            visited.add(v)
    

n,e=map(int,input().split())
graph=collections.defaultdict(list)
dis=[float('inf')]*n
dis[0]=0
p=[-1]*n
visited=set()
for _ in range(e):
    u,v,w=map(int,input().split())
    graph[u-1].append((v-1,w))
    graph[v-1].append((u-1,w))
q=hd.heapdict()
q[0]=0
#print(graph)  
dijkstra(q,dis,p,visited,graph)
#print('parent',p)
#print('here',n,p[n-1])
if p[n-1]==-1:
    print(-1)
else:
    n-=1
    res=[]
    while n!=-1:
        res.append(n+1)
        n=p[n]
    print(*res[::-1])
        
