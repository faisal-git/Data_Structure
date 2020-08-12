# https://leetcode.com/problems/coin-change/submissions/
# here dp[i][j] is min number of coins required total i different denomination any number of time 
# so that their total becomes j
# recursive relation for top down is 
# dp[i][j]=min(min_coin(i-1,amt),1+coin(i,amt-coins[i])) fi coins[i]<=amt
# else dp[i][j]=min_coin(i-1,amt)
#time is O(len(coins)*amount)
#space is same as time
# recursive approach

# coins is global
def min_coin(i,amt,cache):
            if amt==0:
                return 0
            if i==0:
                return float('inf')
            if cache.get((i,amt)):
                return cache[(i,amt)]
            
            if coins[i-1]<=amt:
            
                cache[(i,amt)]=min(min_coin(i-1,amt,cache),1+min_coin(i,amt-coins[i-1],cache))
            else:
                cache[(i,amt)]=min_coin(i-1,amt,cache)
            return cache[(i,amt)]
            
        res= min_coin(len(coins),amount,{})
#-----------------------------------------------------------------------------------
# since for a given i we only need i-1 row hence we can solve this problem in linear space O(amount)
#below is iterative solution ,time complexity remain same as top down

dp=[float('inf')]*(amount+1)
dp[0]=0
for i in range(len(coins)):
    for j in range(coins[i],amount+1):
        dp[j]=min(dp[j],1+dp[j-coins[i]])
return dp[-1]
#-----------------------------------------------------------------------------------
# we can also approach this problem using BFS traversal with memoization
# the idea behind is Bfs can help us to find the shortest path between root here is 0 and and leaf here is amount 
# every a new  value is enountered ,it can asserted that the depth of the traversal is the min no coins required to make that value with given denomination
# below is the code
if not amount:
            return 0
if amount in coins:
    return 1
min_coin=[-1 for i in range(amount+1)] # index is amount and value is the min_coins count
visited=[False for i in range(amount+1)] # to keep track of amt,is encountered previously or not 
q=collecions.deque() # queue to implement bfs 
q.append(0)
visited[0]=True
min_coin[0]=0
# we push only those amt which is <=amount and is not encountered before
while q:
    val=q.popleft()
    for c in coins:
        if val+c==amount:
            return min_coin[val]+1
        if val+c<amount and not visited[val+c]:
            min_coin[val+c]=1+min_coin[val]
            visited[val+c]=True
            q.append(val+c)
return min_coin[amount]