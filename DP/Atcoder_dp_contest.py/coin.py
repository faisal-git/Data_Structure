# https://atcoder.jp/contests/dp/submissions/16061061

n=int(input())
p=list(map(float,input().split()))

dp=[[0]*(n+1) for _ in range(n+1)]
dp[0][0]=1
for t in range(1,n+1):
    dp[t][0]=dp[t-1][0]*(1-p[t-1])
    for h in range(1,t+1):
        dp[t][h]=dp[t-1][h-1]*p[t-1]+dp[t-1][h]*(1-p[t-1])
ans=0
for h in range(t//2+1,n+1):
    ans+=dp[n][h]
print(ans)