# https://practice.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1/

def maxLen(arr, N):
    _sum=0
    cache={}
    res=0
    for i,val in enumerate(arr):
        if val :
            _sum+=1
        else:
            _sum-=1
        if _sum==0:
            res=i+1
            
        elif _sum in cache:
            res=max(res,i-cache[_sum])
        else:
            cache[_sum]=i
    return res