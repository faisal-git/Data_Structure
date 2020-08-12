# lookin at constraints can we say that max sum possible is 200*50 of whole
# the whole idea is to think about the sum we can have in one subset 
# can we say dp[j] that whether or not we have make sum equal to j 
def min_diff(arr,n,t_sum):
    global diff
    dp=[False]*(t_sum+1)
    dp[0]=True
    for i in range(n):
        for j in range(t_sum,arr[i]-1,-1):
            dp[j]=dp[j]or dp[j-arr[i]]
            if dp[j]:
                diff=min(diff,abs((t_sum-j)-j))
       
    
        


for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    diff=sum(arr)
  
    min_diff(arr,n,diff)
    print(diff)