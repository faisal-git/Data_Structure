# in unbounded knapsack we can take multiple occurencec of same items
#hence state reduces to one ,just to keep track of W in call
#because at any given instance we can take any of items
# hence at any instance we need not to take into consideration about which items we have processed
# Time is O((W+1)*size of items)
# space is max(size of items ,W)


def recursive(W,wt,p,dp):
    if W==0:
        return 0
    elif dp.get(W):
        return dp[W]
    
    max_pro=0
    for  i,w in enumerate(wt):
        if w <=W:
            max_pro=max(max_pro,p[i]+recursive(W-w,wt,p,dp))
    dp[W]=max_pro
    return dp[W]

W = 100
val = [10, 30, 20] 
wt = [5, 10, 15] 
#print(recursive(W,wt,val,{}))

# iterative solution
# need only 1D array since there is only one state
dp=[0]*(W+1)
for w in range(W+1):
    for i,item in enumerate(wt):
        if item <=w:
            dp[w]=max(dp[w],val[i]+dp[w-item])
print(dp[-1])