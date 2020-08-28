#time: O(E+V)
# https://practice.geeksforgeeks.org/problems/shortest-path-from-1-to-n/0
# there are n nodes and there is an edge b/w i and j if either j=i+1 or j=3*i
import collections
for _ in range(int(input())):
    n=int(input())
    q=collections.deque()
    q.append(1)
    dis=[float('inf')]*(n+1)
    dis[1]=0
    while q: 
        for _ in range(len(q)):
            node=q.popleft()
            for adj in (node+1,3*node):
                if adj<=n and dis[adj]==float('inf'):
                    dis[adj]=1+dis[node]
                    q.append(adj)
    print(dis[n])