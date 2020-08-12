# approach is similar  to subset subset sum
# dp[j] = how many ways to get reach to sum j
 
arr=[0,0,0,0,0,0,0,0,1]
n=len(arr)
target=1
dp=[0]*(target+1)
dp[0]=1 

for i in range(1,n+1):
    for j in range(target,arr[i-1]-1,-1):
        dp[j]=dp[j]+dp[j-arr[i-1]]
        
print(dp[-1])
        
# if arr also contains -ve number and target is +ve then we can consider including another case
# dp[i][j]= dp[i-1][j]+dp[i-1][j-arr[i-1]]+dp[i-1][j+arr[i-1]]
# dp[i-1][j-arr[i-1]] if j>=arr[i-1]
#dp[i-1][j+arr[i-1]]      