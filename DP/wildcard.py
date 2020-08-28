# to get an idea that why this problem exhibits overlapping subproblems 
#consider an examaple p='a*a*' s='aaaa' 
# lets i and j keeps track of ith and jth element of s and p respectively
# recurrence start with (i=4,j=4)
# lets * at j=4 matches two chars i=4 and 3 and recurrence goes to i=2 and j=3 and 
# then s[i]==p[j] then recurrence goes to i=1 and j=2 and now * at j=2 matches 0 chars
# then recurrnce reaches state where i=1 and j=1 for the first time 
# just reverse the behaviour of * at j=4 and j=2 we will again reach the state i=j=1
# hence it have overlapping subproblem
# now consider what are the decision we need to make certaion decision to arrive at optimal
# if p[j]=='?' then we shift i=i-1 and j=j-1
# if p[j]=='* then two option to be consider
# 1. '*' matches 0 character : in this case we move the pointer in P one step
# 2.'*' matches 1 or more characters : in this case we move the pointer in S one step
# else do compare the s[i] and p[j] and call on subproblem i-1,j-1 if s[i]==p[j]
# dp[i][j] represents the ans to the subproblems where i and j elements are considered from s and p respectively

# Top Down approach
 def isMatch( s: str, p: str) -> bool:
        memo={}
        def recur(text,pattern,i,j):
            if j>=len(pattern):
                return True if i>=len(text) else False
            elif (i,j) in memo:
                return memo[(i,j)]
            else:
                
                if pattern[j]=='*':
                    skip=recur(text,pattern,i,j+1)
                    absorb=i<len(text) and recur(text,pattern,i+1,j)
                    memo[(i,j)]=skip or absorb
                else:
                    curr=i<len(text)and pattern[j] in (text[i],'?')
                    memo[(i,j)]=curr and recur(text,pattern,i+1,j+1)
                    
                return memo[(i,j)]
        return recur(s,p,0,0)
# Bottom-up approach
def isMatch(s: str, p: str) -> bool:
        m,n=len(s),len(p)
        dp=[[False]*(n+1) for i in range(m+1)]
        dp[0][0]=True
        for j in range(n):
            if p[j]=='*':
                dp[0][j+1]=dp[0][j]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1]=='*':
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                elif p[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=dp[i-1][j-1] and p[j-1]==s[i-1]
        return dp[-1][-1]

