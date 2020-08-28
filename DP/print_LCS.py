# just an extension of LCS

# Top down approach
def dp(l1,l2,s,t,cache):
        
        if not l1 or not l2:
            return ""
        elif cache.get((l1,l2)):
            return cache[(l1,l2)]
        else:
            
            if s[l1-1]==t[l2-1]:
                cache[(l1,l2)]=dp(l1-1,l2-1,s,t,cache)+s[l1-1]
                return cache[(l1,l2)]
            
            else:
                sub1,sub2=dp(l1-1,l2,s,t,cache),dp(l1,l2-1,s,t,cache)
                cache[(l1,l2)]=sub1 if len(sub1)>=len(sub2) else sub2
                return cache[(l1,l2)]




A,B=input().split()
m,n=len(A),len(B)
print(dp(m,n,A,B,{}))


# below is bottom-up approach.
"""dp=[[""]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if A[i-1]==B[j-1]:
            dp[i][j]=dp[i-1][j-1]+B[j-1]
        else:
            if len(dp[i-1][j])>len(dp[i][j-1]):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i][j-1]
print(dp[-1][-1])"""