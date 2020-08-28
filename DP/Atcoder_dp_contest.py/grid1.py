# https://atcoder.jp/contests/dp/submissions/16059263

import sys
sys.setrecursionlimit(10**9)

def recursive(i,j):
    if i<0 or j<0 or i>=row or j>=col or  grid[i][j]=='#':
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    if i==row-1 and j==col-1:
        return 1
    mod=10**9+7
    dp[i][j]=recursive(i+1,j)%mod +recursive(i,j+1)%mod
    return dp[i][j]%mod


row,col=map(int,input().split())
dp=[[-1]*col for _ in range(row)]
grid=[]
for _ in range(row):
    grid.append(input())
print(recursive(0,0))
