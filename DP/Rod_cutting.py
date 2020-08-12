# rod cutting is a variation of unbounded knapsack
# since in this case we can make i cuts several times
# state is only the lenght of the rod 
# at any istance we can make any cuts we want if possibe cut<=length

# dp[j] represent the max value we can get out of length j

# time 

def recursive(l,val,dp):
    if not l:
        return 0
    elif dp.get(l):
        return dp[l]
    max_price=0
    for i in range(1,l+1):
        max_price=max(max_price,val[i-1]+recursive(l-i,val,dp))
    dp[l]=max_price
    return  max_price
val=arr = [1, 5, 8, 9, 10, 17, 17, 20] 
#print(recursive(len(val),val,{}))

# iterative solution 
n=len(val)
dp=[0]+val
for i in range(1,n+1):
    for cut in range(1,i+1):
        dp[i]=max(dp[i],val[cut-1]+dp[i-cut])
print(dp[-1])

# small variation in this problem
#   https://www.interviewbit.com/problems/rod-cutting/
