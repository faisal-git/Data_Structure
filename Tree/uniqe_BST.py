# why dp?
# because of 2 reason :
# 1. solving for lower value of n can help to find larger n,put in other words,
# optimal solution for  val<n is helpful is arriving at solution for n (optimal substructure)
# 2. it has overlapping subproblem since solving for (1,2,3,4) is equal to (2,3,4,5). 
# type is combanitorics
# Decision to made at every stage is which val will be root node.
# the idea here is at every stage we need to make a decision of chosing 


def recursive(n,dp):
    if n<2:
        return 1
    elif dp[n]:
        return dp[n]
    for root in range(1,n+1):
        dp[n]+=recursive(root-1,dp)*recursive(n-root,dp)
    return dp[n]



def dp(n):
    dp={0:1,1:1}
    for x in range(2,n+1):
        dp[x]=0
        for y in range(x):
            dp[x]+=dp[y]*dp[x-y-1]
    return dp[n]
    