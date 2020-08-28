 #https://leetcode.com/problems/palindrome-partitioning-ii
 # recursive solution : Time O(n^2) and space O(N)
 def minCut(self, s: str) -> int:
        def dp(i,s,cache):
            if i==len(s):
                return 0
            if cache.get(i):
                return cache[i]
            if s[i:]==s[i:][::-1]:
                return 0
            cache[i]=len(s)
            for k in range(i,len(s)):
                string=s[i:k+1]
                if string==string[::-1]:
                    cache[i]=min(cache[i],1+dp(k+1,s,{}))
            return cache[i]
        return dp(0,s,{})

# iterative solution Time O(N^2) and space is linear

def minCut(self, s: str) -> int:
        n=len(s)
        dp=[float('inf')]*(n+1)
        dp[n]=0
        for i in range(n-1,-1,-1):
            if s[i:]==s[i:][::-1]:
                dp[i]=0
            else:
                for k in range(i+1,n):
                    if s[i:k]==s[i:k][::-1]:
                        dp[i]=min(dp[i],1+dp[k])
        return dp[0]
                