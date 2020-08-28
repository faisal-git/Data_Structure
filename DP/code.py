def mcm(p): 
    n=len(p)
    dp=[[0]*n for _ in range(n)]

    for i in range(n-2,0,-1):
        for j in range(i+1,n,1):
            dp[i][j]=float('inf')
            for k in range(i,j):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+p[i-1]*p[k]*p[j])
    return (dp[1][n-1])
                
print(mcm([30, 35, 15, 5, 10, 20, 25]))