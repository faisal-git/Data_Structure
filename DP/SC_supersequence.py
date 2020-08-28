# https://leetcode.com/problems/shortest-common-supersequence/
# simply try to inlude only one occurances of each letter which is a part of LCS of A and b 
# and adding all other letters of A and B otherwise
# dp[i][j] superseq. for i elements in A and j elements in B.
#dp[i][j]=dp[i-1][j-1]+ A[i] if A[i]==B[j] 
# dp[i][j]=min(dp[i-1][j]+A[i],dp[i][j-1]+B[j])
def super_seq(A,B,m,n,cache):
        if not m and not n:
            return ""
        if m==0:
            return B[:n]
        if n==0:
            return A[:m]
        if cache.get((m,n)):
            return cache[(m,n)]
        if A[m-1]==B[n-1]:
            cache[(m,n)]=super_seq(A,B,m-1,n-1,cache)+A[m-1]
        else:
            string1=super_seq(A,B,m-1,n,cache)+A[m-1]
            string2=super_seq(A,B,m,n-1,cache)+B[n-1]
            cache[(m,n)]=string1 if len(string1)<=len(string2) else string2
        return cache[(m,n)]
#----------------------------------------------------------
# Bottom-up approach
# the idea is to first calculate LCS and based on the condition try to compute asn backward
# ans="" initialise
# if text1[i]==text2 then decrease i and j and inlude either text1[i] or text2[j]
# if dp[i][j-1]>dp[i-1][j] ( means subsequecne(i,j-1)>subsequece(i-1,j))
# hence inlude text2[j] in answer as ,ans=text2[j]+ans
# else: ans=text1[i]+ans
m,n=len(text1),len(text2)
dp=[[0 for j in range(n+1)]for i in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if text1[i-1]==text2[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

i,j=m,n
ans=""
while i and j:
    if text1[i-1]==text2[j-1]:
        ans=text1[i-1]+ans
        i-=1
        j-=1
    elif dp[i-1][j]>dp[i][j-1]:
        ans=text1[i-1]+ans
        i-=1
    else:
        
        ans=text2[j-1]+ans
        j-=1
    
if i:
    return text1[:i]+ans
elif j:
    return text2[:j]+ans

return ans




