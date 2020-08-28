#https://practice.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions/0
# simple logic is that find  LCS 
# answer will be simply len(str1)+len(str2)-2*LCS
# is so becuase LCS gives us the max. lenght of common letters found in both string 
# so we need no all extra letters if is not found both strings


for _ in range(int(input())):
    m,n=map(int,input().split())
    str1,str2=input().split()
    dp=[[0]*(n+1) for __ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-2]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    sub_seq=dp[-1][-1]
    print((m-sub_seq)+(n-sub_seq))