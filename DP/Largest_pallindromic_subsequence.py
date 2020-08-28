# https://leetcode.com/problems/longest-palindromic-subsequence/submissions/
# the idea is use two pointers and memoisation.
# dp[i][j] represents the largest pallindromic subsequence in the substing starting 
# from the index i to j both inclusive.

# Top-Down approach : time O(N^2) memory same

dp={} # global variable 
def lps(i,j):
    if i>j:
        return 0
    if i==j:
        return 1
    if dp.get((i,j)):
        return dp[(i,j)]
    
    if s[i]==s[j]:
        dp[(i,j)]=2+lps(i+1,j-1)
    else:
        dp[(i,j)]=max(lps(i+1,j),lps(i,j-1))
    
    return dp[(i,j)]
return lps(0,len(s)-1)

# in Bottom is just clever way of implementing LCS
# LCS of s and reverse(s) is required answer



def longestPalindromeSubseq(self, s: str) -> int:
        m=n=len(s)
        rev_s=s[::-1]
        dp=[[0 for j in range(n+1)]for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==rev_s[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

# to find min number of deletion required to make a string pallindromic 
# find longest pallindromic subsequence and substract it by the length of string