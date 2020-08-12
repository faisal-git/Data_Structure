# https://leetcode.com/problems/coin-change-2/
# number of unique combination to make sum of denomination of coins equal to given target
# this falls in class unbounded knapsack since a coin can be chosen infinite number of time
# Also has relation to count the number of subset having sum equal to target
# dp[i][j]= the number of ways we can make sum j with i number of coins inlcuded
#time O(amount*len(coins)) space is same
def change( amount: int, coins):
        
        def dp(n,amt,cache):
            if amt==0:
                return 1
            elif n==0:
                return 1 if not amt else 0
            elif cache.get((n,amt)):
                return cache[(n,amt)]
            
            if coins[n-1]<=amt:
                
                cache[(n,amt)]=dp(n-1,amt,cache)+dp(n,amt-coins[n-1],cache) #line diff
            else:
                cache[(n,amt)]=dp(n-1,amt,cache)
            return cache[(n,amt)]
        return dp(len(coins),amount,{})
#line diff: repsent makes this solution unbounded knapsack
# dp(n,amt-coins[n-1],cache) in this problem where as is n-1 in case of bounded

#-------------------------------------------------------------
#iterative solutions 
# space reduces to O(amount+1) time remains same
def change(amount,coins):
        
        dp=[0]*(amount+1)
        dp[0]=1
        for i in range(len(coins)):
            for j in range(coins[i],amount+1): # line diff
                #if coins[i]<=j: since loop starts from coins[i]
                dp[j]=dp[j]+dp[j-coins[i]]
        return dp[-1]
#line diff: repsent makes this solution unbounded knapsack
# inner loop start from left so that it can leverage the fact that a coin can be inlucded multiple no. of time
#unlike bounded knapsack
