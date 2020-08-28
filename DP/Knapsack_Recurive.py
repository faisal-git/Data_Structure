import sys
sys.setrecursionlimit(10**9)

def knapsack(W,n):
  if n==0 or W==0 :
    return 0
  elif cache.get((W,n)):
    return cache[(W,n)]
  
  else:
    if wt[n-1]<=W:
      cache[(W,n)]=max(knapsack(W,n-1),p[n-1]+knapsack(W-wt[n-1],n-1))
      return cache[(W,n)]
    else:
      cache[(W,n)]=knapsack(W,n-1)
      return cache[(W,n)]


    

  
n,w=map(int,input().split())
wt,p=[],[]
cache={}
for _ in range(n):
  temp_wt,temp_pr=map(int,input().split())
  wt.append(temp_wt)
  p.append(temp_pr)
print(knapsack(w,n))

