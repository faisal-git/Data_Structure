#https://www.interviewbit.com/problems/repeating-subsequence/
n=len(A)
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
               
                elif A[i-1]==A[j-1] and i!=j:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return 1 if dp[-1][-1]>1 else 0
# https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence/0