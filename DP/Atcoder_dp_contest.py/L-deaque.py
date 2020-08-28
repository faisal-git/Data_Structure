# dp[i][j] represents max value X-Y where X stand for the value of that guy whose has his turn at this dp state
# dp[i][j]=max(taking ith value - max value can formed from i+1,j,taking jth value-max value formed form i,j)
# Time and space complexity is O(N^2)
# space comlextiy can be brought to O(N) since for dp[i][j] we only on row dp[i+1] to be present in memory 
#


import sys
sys.setrecursionlimit(10**9)

def recursive(i,j):
  if i>j:
    return 0
  elif dp.get((i,j)):
    return dp[(i,j)]
  dp[(i,j)]=max(nums[i]-recursive(i+1,j),nums[j]-recursive(i,j-1))
  return dp[(i,j)]

dp={}
n=int(input())
nums=list(map(int,input().split()))
#print(dp)
#print(recursive(0,n-1))
dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(n-1,-1,-1):
    for j in range(i,n,1):
        dp[i][j]=max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1])
print(dp[0][n-1])

