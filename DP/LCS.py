# https://leetcode.com/problems/longest-common-subsequence/
# dp[i][j] represents what is the length LCS if i elements and j elements taken from first and second string respectively
# recursive ralation :
# dp[i][j]= 1+ dp[i-1][j-1] if str1[i]==str2[j] else: max(dp[i-1][j],dp[i][j-1])
# time and space is O(m*n) where m and n the are the lengths strings given

# Top down approach
def dp(self,l1,l2,s,t,cache):
        
        if not l1 or not l2:
            return 0
        elif cache.get((l1,l2)):
            return cache[(l1,l2)]
        else:
            
            if s[l1-1]==t[l2-1]:
                cache[(l1,l2)]=self.dp(l1-1,l2-1,s,t,cache)+1
                return cache[(l1,l2)]
            
            else:
                
                cache[(l1,l2)]=max(self.dp(l1-1,l2,s,t,cache),self.dp(l1,l2-1,s,t,cache))
                return cache[(l1,l2)]

# Bottom up approach

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dp=[[0 for j in range(n+1)]for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]