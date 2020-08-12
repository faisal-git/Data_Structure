#https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# other approach : https://leetcode.com/problems/maximum-length-of-repeated-subarray/discuss/109059/O(mn)-time-O(1)-space-solution

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
        