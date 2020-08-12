# https://www.geeksforgeeks.org/knapsack-with-large-weights/

# in this question we are basicallly forced to alter the state so be alble to solve the problem within time constraints
# here W (capacity of knapsak is huge ,like order 10^9)
# but the thing to be considered is the low value of price

# question of Atcoder https://atcoder.jp/contests/dp/tasks/dp_e
# submitted solution https://atcoder.jp/contests/dp/submissions/15839572

# here max profit is 10*3 and N<=100

n,W=map(int,input().split())
wt,values=[],[]
for _ in range(n):
    w,val=map(int,input().split())
    wt.append(w)
    values.append(val)
# since for an i we only need look at i-1 row hence 1D array can be used to memoise
# inner loop goes backward since we can take an item more then once (bounded Knapsack)
# dp[j] is gives the min weight required to earn j profit
max_profit=max(values)*n # not neccessary we can take it n*10^3
dp=[float('inf')]*(max_profit+1)
dp[0]=0

for i in range(n):
    for j in range(max_profit,values[i]-1,-1):
        dp[j]=min(dp[j],wt[i]+dp[j-values[i]])
    #print(dp)
ans=0

for i in range(1,max_profit+1):
    if dp[i]<=W:
        ans=i
print(ans)
    





