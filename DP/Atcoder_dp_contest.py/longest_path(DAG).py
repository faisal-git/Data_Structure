# https://atcoder.jp/contests/dp/submissions/16059034

import collections
import sys 
sys.setrecursionlimit(10**9)
def dfs(v):
    if cache.get(v):
        return cache[v]
    path=0
    for adj in g[v]:
        path=max(path,1+dfs(adj))
    cache[v]=path
    return path


n,m=map(int,input().split())
g=collections.defaultdict(list)
cache={}
path=0
for _ in range(m):
    u,v=map(int,input().split())
    g[u].append(v)
for v in range(1,n+1):
    path=max(path,dfs(v))
print(path)

