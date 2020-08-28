# https://leetcode.com/problems/palindrome-partitioning/
# https://www.interviewbit.com/problems/palindrome-partitioning/
# Time is O(N^3) since for each i we need n^2 for inner loop at max
# the idea here is to to try paritioning at every position such that left half is pallindrome for sure
# and the recursively call ,with right half
# can remove n from parameter list and use len(n) instead.
def pallindrome(i,n,s,dp):
    if i==n:
        return [[]]
    if dp.get(i):
        return dp[i]
    res=[]
    for k in range(i+1,n+1):
        string=s[i:k]
        if string==string[::-1]:
      
            for each in pallindrome(k,n,s,dp):
                res.append([string]+each)
    if res:
        dp[i]=res
        return res
    else:
        dp[i]=[[]]
        return [[]] 

print(pallindrome(0,4,'aabb',{}))