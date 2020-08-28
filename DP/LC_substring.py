#https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# other approach : https://leetcode.com/problems/maximum-length-of-repeated-subarray/discuss/109059/O(mn)-time-O(1)-space-solution
# it is different form LCS since for a given i,j if A[i]==B[i] then dp[i][j]=max(1+dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) where as in 
# LCS if A[i]==B[i] then dp[i][j]=1+dp[i][j]
# consider example A="aaab" and B="aabb"
# i=4 and j=4 in case LCS ,ans will be 1+LCS('aaa','aab')=LCS(3,3)
#where as in substring ,ans will be LCS('aab','aab')=LCS(4,3) because 1+LCS(3,3) returns 0 since
# A[3]!=B[3]
# suffix tree can improve the time complexity
def LC_substring(A,B)
  m,n=len(A),len(B)
        dp=[0]*(n+1)
        ans=0
        for i in range(m):
            for j in range(n,0,-1):
                if A[i]==B[j-1]:
                    dp[j]=dp[j-1]+1
                    ans=max(ans,dp[j])
                else:
                    dp[j]=0
        return ans
        