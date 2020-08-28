### do consider to change how inputs are taken according to the question

# top down approach for Knapsack
# O(n*W) time and O(n*W) Space
# to improve performance a bit use cache as 2D matice instead of hasmap(tuple->value)
'''def knapsack(W,n):
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
    
wt,p=[],[]
cache={}

n,w=map(int,input().split())

for _ in range(n):
    temp_wt,temp_pr=map(int,input().split())
    wt.append(temp_wt)
    p.append(temp_pr)
print(knapsack(w,n))'''



#bottom up approach.


# what is dp relation 
# dp[i][j]: max profit for wieght constriants j and i  number of elements
# O(n*W) time and O(n*W) Space
'''n,W=map(int,input().split())
wt,p=[],[]
for _ in range(n):
    a,b=map(int,input().split())
    wt.append(a)
    p.append(b)
dp=[[0 for i in range(W+1)]for j in range(n+1)]
for x in range(1,n+1):
    for y in range(1,W+1):
        if wt[x-1]<=y:
            dp[x][y]=max(dp[x-1][y-wt[x-1]]+p[x-1],dp[x-1][y])
        else:
            dp[x][y]=dp[x-1][y]
print(dp[-1][-1])'''

# what is dp relation 
# dp[j]=max profit for knapsack weight j
# O(n*W) time and O(W) Space 

n,W=map(int,input().split())
wt,p=[],[]
for _ in range(n):
    a,b=map(int,input().split())
    wt.append(a)
    p.append(b)
dp=[0 for i in range(W+1)]
for x in range(1,n+1):
  
  for y in range(W,0,-1):
    if wt[x-1]<=y:
        
      dp[y]=max(dp[y-wt[x-1]]+p[x-1],dp[y])
    else:

      dp[y]=dp[y]
print(dp[-1])
